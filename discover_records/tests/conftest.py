from collections import defaultdict

import pytest
import requests

from discover_records.management.commands.importrecord import MiniRecord


@pytest.fixture
def tna_record_example_json():
    record_json = defaultdict(
        str,
        {
            "accessRegulation": {
                "closureCriteria": ["string"],
                "closureSetId": 0,
                "signedDate": "2023-05-07T11:34:59.353Z",
                "reviewDate": "2023-05-07T11:34:59.353Z",
                "reconsiderDueInDate": "2023-05-07T11:34:59.353Z",
                "lordChancellorsInstrument": "string",
                "explanation": "string",
                "procatTitleText": "string",
            },
            "accruals": "string",
            "accumulationDates": "string",
            "administrativeBackground": "string",
            "appraisalInformation": "string",
            "arrangement": "string",
            "batchId": "string",
            "copiesInformation": [
                {
                    "description": "string",
                    "endDate": 0,
                    "firstName": "string",
                    "preTitle": "string",
                    "startDate": 0,
                    "surname": "string",
                    "title": "string",
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "corporateNames": [
                {
                    "description": "string",
                    "endDate": 0,
                    "firstName": "string",
                    "preTitle": "string",
                    "startDate": 0,
                    "surname": "string",
                    "title": "string",
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "creatorName": [
                {
                    "description": "string",
                    "endDate": 0,
                    "firstName": "string",
                    "preTitle": "string",
                    "startDate": 0,
                    "surname": "string",
                    "title": "string",
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "custodialHistory": "string",
            "detailedRelatedMaterial": [
                {
                    "description": "string",
                    "endDate": 0,
                    "firstName": "string",
                    "preTitle": "string",
                    "startDate": 0,
                    "surname": "string",
                    "title": "string",
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "detailedSeparatedMaterial": [
                {
                    "description": "string",
                    "endDate": 0,
                    "firstName": "string",
                    "preTitle": "string",
                    "startDate": 0,
                    "surname": "string",
                    "title": "string",
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "dimensions": "string",
            "formerReferenceDep": "string",
            "formerReferencePro": "string",
            "immediateSourceOfAcquisition": [
                {
                    "description": "string",
                    "endDate": 0,
                    "firstName": "string",
                    "preTitle": "string",
                    "startDate": 0,
                    "surname": "string",
                    "title": "string",
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "language": "string",
            "legalStatus": "string",
            "links": [
                {
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "locationOfOriginals": [
                {
                    "description": "string",
                    "endDate": 0,
                    "firstName": "string",
                    "preTitle": "string",
                    "startDate": 0,
                    "surname": "string",
                    "title": "string",
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "mapDesignation": "string",
            "mapScaleNumber": 0,
            "note": "string",
            "otherReferences": [{"key": "NRA_CATALOGUE", "value": "string"}],
            "people": [
                {
                    "description": "string",
                    "endDate": 0,
                    "firstName": "string",
                    "preTitle": "string",
                    "startDate": 0,
                    "surname": "string",
                    "title": "string",
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "physicalCondition": "string",
            "physicalDescriptionExtent": "string",
            "physicalDescriptionForm": "string",
            "places": [
                {
                    "country": "string",
                    "countryID": 0,
                    "county": "string",
                    "countyID": 0,
                    "description": "string",
                    "displayName": "string",
                    "endDate": 0,
                    "grid": "string",
                    "locationType": "string",
                    "newCounty": "string",
                    "newCountyID": 0,
                    "oldCounty": "string",
                    "oldCountyID": 0,
                    "parish": "string",
                    "placeName": "string",
                    "region": "string",
                    "regionID": 0,
                    "startDate": 0,
                    "town": "string",
                    "townID": 0,
                    "validation": "string",
                }
            ],
            "publicationNote": ["string"],
            "registryUrl": "string",
            "restrictionsOnUse": "string",
            "scannedLists": [
                {
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "subjects": ["string"],
            "unpublishedFindingAids": ["string"],
            "accessConditions": "string",
            "catalogueId": 0,
            "citableReference": "ref_string",
            "closureCode": "string",
            "closureStatus": "string",
            "closureType": "string",
            "coveringDates": "string",
            "coveringFromDate": 0,
            "coveringToDate": 0,
            "scopeContent": {
                "placeNames": ["string"],
                "description": "desc_string",
                "ephemera": "string",
                "schema": "string",
            },
            "digitised": True,
            "heldBy": [
                {
                    "xReferenceId": "string",
                    "xReferenceCode": "string",
                    "xReferenceName": "string",
                    "xReferenceType": "string",
                    "xReferenceURL": "string",
                    "xReferenceDescription": "string",
                    "xReferenceSortWord": "string",
                }
            ],
            "id": "id_string",
            "isParent": True,
            "catalogueLevel": 0,
            "parentId": "string",
            "recordOpeningDate": "string",
            "referencePart": "string",
            "referenceParentId": "string",
            "sortKey": "string",
            "source": "string",
            "title": "title_string",
        },
    )
    return record_json


@pytest.fixture
def tna_record_example_missing_optional_fields(tna_record_example_json):
    record_missing_fields = tna_record_example_json.copy()
    record_missing_fields.pop("citableReference", None)
    record_missing_fields.pop("scopeContent", None)
    record_missing_fields.pop("title", None)
    return record_missing_fields


@pytest.fixture
def tna_record_example_mini():
    return MiniRecord("id_string", "title_string", "desc_string", "ref_string")


class MockResponse200:
    """Mock return value of requests.get() for successful request"""

    @staticmethod
    def json():
        return {"mock_key": "mock_value"}

    @property
    def status_code(self):
        return 200


class MockResponse204:
    """Mock return value of requests.get() for 'record not found'"""

    @property
    def status_code(self):
        return 204


@pytest.fixture
def mock_response_200(monkeypatch):
    """Requests.get() mocked to return valid json record."""

    def mock_get(*args, **kwargs):
        return MockResponse200()

    monkeypatch.setattr(requests, "get", mock_get)


@pytest.fixture
def mock_response_204(monkeypatch):
    """Requests.get() mocked to return no request body."""

    def mock_get(*args, **kwargs):
        return MockResponse204()

    monkeypatch.setattr(requests, "get", mock_get)


@pytest.fixture
def tna_record_real_json():
    record_json = {
        "accessRegulation": None,
        "accruals": None,
        "accumulationDates": None,
        "administrativeBackground": None,
        "appraisalInformation": None,
        "arrangement": None,
        "batchId": None,
        "copiesInformation": [],
        "corporateNames": [],
        "creatorName": [],
        "custodialHistory": None,
        "detailedRelatedMaterial": [],
        "detailedSeparatedMaterial": [],
        "dimensions": None,
        "formerReferenceDep": None,
        "formerReferencePro": None,
        "immediateSourceOfAcquisition": [],
        "language": "English",
        "legalStatus": None,
        "links": [],
        "locationOfOriginals": [],
        "mapDesignation": None,
        "mapScaleNumber": 0,
        "note": None,
        "otherReferences": [],
        "people": [],
        "physicalCondition": None,
        "physicalDescriptionExtent": None,
        "physicalDescriptionForm": None,
        "places": [],
        "publicationNote": [],
        "registryUrl": "",
        "restrictionsOnUse": None,
        "scannedLists": [],
        "subjects": [],
        "unpublishedFindingAids": [],
        "accessConditions": None,
        "catalogueId": 0,
        "citableReference": "BD 20/97/DRAWER 1/204",
        "closureCode": None,
        "closureStatus": None,
        "closureType": None,
        "coveringDates": "n.d",
        "coveringFromDate": 0,
        "coveringToDate": 0,
        "scopeContent": {
            "placeNames": [],
            "description": "<p>Titan Tractor</p>",
            "ephemera": None,
            "schema": None,
        },
        "digitised": False,
        "heldBy": [
            {
                "xReferenceId": "A13530872",
                "xReferenceCode": "44",
                "xReferenceName": "Herefordshire Archive and Records Centre",
                "xReferenceType": None,
                "xReferenceURL": None,
                "xReferenceDescription": None,
                "xReferenceSortWord": None,
            }
        ],
        "id": "a147aa58-38c5-45fb-a340-4a348efa01e6",
        "isParent": False,
        "catalogueLevel": 9,
        "parentId": "6791f929-85ac-4e43-b2b4-0c1a6d687cbe",
        "recordOpeningDate": None,
        "referencePart": None,
        "referenceParentId": None,
        "sortKey": "09 0 2539 0#539",
        "source": "A2A",
        "title": None,
    }
    return record_json
