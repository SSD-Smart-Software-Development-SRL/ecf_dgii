from enum import StrEnum


class Ecf44VersionType(StrEnum):
    VERSION1_0 = "Version1_0"

    def __str__(self) -> str:
        return str(self.value)
