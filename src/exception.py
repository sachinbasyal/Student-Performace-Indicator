import sys

def error_message_detail(error: Exception, error_detail=sys) -> str:
    """Generates a detailed error message (file + line) for the current exception."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "unknown"
    line_number = exc_tb.tb_lineno if exc_tb else "unknown"
    return f"Error occurred in file: {file_name} at line: {line_number} | {type(error).__name__}: {error}"


class CustomException(Exception):
    """Custom exception class that includes detailed error information."""
    def __init__(self, error: Exception, error_detail=sys, message: str = "An error occurred"):
        self.error_message = f"{message} | {error_message_detail(error, error_detail)}"
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message


