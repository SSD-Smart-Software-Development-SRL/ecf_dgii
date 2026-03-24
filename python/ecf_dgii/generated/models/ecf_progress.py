from enum import Enum

class EcfProgress(str, Enum):
    ERROR = "Error"
    FINISHED = "Finished"
    NEW = "New"
    PROCESSING = "Processing"
    UPLOADEDTODGII = "UploadedToDgii"

    def __str__(self) -> str:
        return str(self.value)
