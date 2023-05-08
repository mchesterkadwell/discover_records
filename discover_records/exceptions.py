class DiscoverRecordsException(Exception):
    pass


class NoRecordFound(DiscoverRecordsException):
    pass


class NoIdInRecord(DiscoverRecordsException):
    pass
