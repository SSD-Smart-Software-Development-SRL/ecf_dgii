from enum import Enum

class Ecf33VersionType(str, Enum):
    VERSION1_0 = "Version1_0"

    def __str__(self) -> str:
        return str(self.value)
