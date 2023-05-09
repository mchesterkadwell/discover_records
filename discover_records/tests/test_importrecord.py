"""
Tests for the Management Command 'importrecord'
"""
import pytest
from django.core.management import call_command
from django.core.management.base import CommandError

from discover_records.exceptions import NoIdInRecord, NoRecordFound
from discover_records.management.commands.importrecord import get_record_by_id, minify_record


@pytest.fixture()
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.mark.usefixtures("no_requests")
class TestGetRecordById:
    def test_code_200_returns_json(self, mock_response_200):
        result = get_record_by_id("valid-id")
        assert result == {"mock_key": "mock_value"}

    def test_code_204_raises_exception(self, mock_response_204):
        with pytest.raises(NoRecordFound):
            get_record_by_id("invalid-id")


@pytest.mark.usefixtures("no_requests")
class TestMinifyRecord:
    def test_mini_record_has_4_keys(self, tna_record_example_json):
        mini_record = minify_record(tna_record_example_json)
        assert len(mini_record) == 4

    def test_mini_record_matches_expected_keys(self, tna_record_example_json, tna_record_example_mini):
        mini_record = minify_record(tna_record_example_json)
        for field in tna_record_example_mini._fields:
            assert getattr(mini_record, field)

    def test_mini_record_matches_expected_values(self, tna_record_example_json, tna_record_example_mini):
        mini_record = minify_record(tna_record_example_json)
        assert mini_record.id == tna_record_example_mini.id
        assert mini_record.title == tna_record_example_mini.title
        assert mini_record.scope_content_description == tna_record_example_mini.scope_content_description
        assert mini_record.citable_reference == tna_record_example_mini.citable_reference

    def test_handles_missing_optional_json_keys(self, tna_record_example_missing_optional_fields):
        try:
            minify_record(tna_record_example_missing_optional_fields)
        except KeyError as err:
            pytest.fail("KeyError: %s" % str(err))

    def test_none_value_converts_to_empty_string(self, tna_record_example_json):
        record_none_value = tna_record_example_json.copy()
        record_none_value["title"] = None
        record_none_value["scopeContent"]["description"] = None
        record_none_value["citableReference"] = None
        mini_record = minify_record(record_none_value)
        assert mini_record.title == ""
        assert mini_record.scope_content_description == ""
        assert mini_record.citable_reference == ""

    def test_missing_id_key_raises_exception(self, tna_record_example_missing_optional_fields):
        record_missing_id = tna_record_example_missing_optional_fields.copy()
        record_missing_id.pop("id")
        with pytest.raises(NoIdInRecord):
            minify_record(record_missing_id)


class TestCommandIntegration:
    def test_no_record_raises_exception(self, capsys):
        record_id = "invalid-id"
        with pytest.raises(CommandError):
            call_command("importrecord", record_id)
            msg = capsys.readouterr().err
            assert msg == f'Record "{record_id}" does not exist.\n'

    @pytest.mark.django_db
    def test_valid_record_write_to_database(self, capsys):
        record_id = "a147aa58-38c5-45fb-a340-4a348efa01e6"
        call_command("importrecord", record_id)
        msg = capsys.readouterr().out
        assert msg == f'Added record "{record_id}" to database.\n'
