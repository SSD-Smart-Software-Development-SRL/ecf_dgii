from enum import StrEnum


class EcfProgress(StrEnum):
    ERROR = "Error"
    FINISHED = "Finished"
    NEW = "New"
    PROCESSING = "Processing"
    UPLOADEDTODGII = "UploadedToDgii"

    def __str__(self) -> str:
        return str(self.value)
