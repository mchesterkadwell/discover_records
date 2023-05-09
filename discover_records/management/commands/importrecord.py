"""
Management Command 'importrecord' to import a specified TNA record into the database.

Run the script on the command line with one argument 'id' of the record. It will:
    * Fetch the record by 'id' from The National Archives Discovery API 'get /records/v1/details/{id} '
    * Insert a minimal subset of the returned JSON record into the Record model.

Example:
--------
$ python manage.py importrecord a147aa58-38c5-45fb-a340-4a348efa01e6
"""

from collections import defaultdict, namedtuple

import requests
from django.core.management.base import BaseCommand, CommandError
from django.db import DatabaseError
from requests.exceptions import HTTPError

from discover_records.exceptions import NoIdInRecord, NoRecordFound
from discover_records.models import Record

# Namedtuple to represent minimal subset of TNA record
MiniRecord = namedtuple("MiniRecord", "id title scope_content_description citable_reference")


def get_record_by_id(record_id):
    """Get a JSON representation of a TNA record by id from the Discover API."""
    url = f"https://discovery.nationalarchives.gov.uk/API/records/v1/details/{record_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return defaultdict(str, response.json())
    if response.status_code == 204:
        raise NoRecordFound
    else:
        response.raise_for_status()


def minify_record(record):
    """Reduce the fields of a TNA record to match the Record model."""
    if not record["id"]:
        raise NoIdInRecord
    desc = (
        record["scopeContent"]["description"]
        if record["scopeContent"] and record["scopeContent"]["description"]
        else ""
    )
    title = record["title"] if record["title"] else ""
    ref = record["citableReference"] if record["citableReference"] else ""
    return MiniRecord(record["id"], title, desc, ref)


class Command(BaseCommand):
    help = "Imports the specified TNA record into the database."

    def add_arguments(self, parser):
        parser.add_argument("record_id")

    def handle(self, *args, **options):
        record_id = options["record_id"]

        # find record in TNA Discovery API
        try:
            record = get_record_by_id(record_id)
        except NoRecordFound:
            raise CommandError('Record "%s" does not exist.' % record_id)
        except HTTPError as err:
            raise CommandError(f"Problem accessing API for record {record_id}: {err}")

        # minify record to minimal subset of TNA record for example purposes
        try:
            mini_record = minify_record(record)
        except NoIdInRecord:
            raise CommandError('No "id" field present in JSON response for record %s' % record_id)

        # write record to database
        try:
            r = Record(**mini_record._asdict())
            r.save()
            self.stdout.write(self.style.SUCCESS('Wrote record "%s" to database.' % record_id))
        except (ValueError, DatabaseError) as err:
            raise CommandError(err)
