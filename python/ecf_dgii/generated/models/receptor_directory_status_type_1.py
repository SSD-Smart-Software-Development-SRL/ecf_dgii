from enum import StrEnum


class ReceptorDirectoryStatusType1(StrEnum):
    AVAILABLE = "Available"
    DESERIALIZATIONFAILED = "DeserializationFailed"
    INVALID = "Invalid"
    NOTFOUND = "NotFound"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
