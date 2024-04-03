def create_logger(level):
    """Function to create a logger function for a specific severity level."""

    def logger(log_message):
        """The logger function for a specific level."""
        print(f"[{level.upper()}] {log_message}")

    return logger


# Create different loggers for info, warning, and error levels
info_logger = create_logger("info")
info_logger("This is an informational message.")
warning_logger = create_logger("warning")
warning_logger("This is a warning message.")
error_logger = create_logger("error")
error_logger("This is an error message.")
