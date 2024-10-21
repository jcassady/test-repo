# logging.py

def log_info(message):
    print("INFO: " + message)  # Basic print, no formatting, hard to read.

def log_warning(message):
    print("WARNING: " + message)  # Mixing string concatenation with print, bad practice.

def log_error(message):
    print("ERROR: " + message)  # No error handling, just printing text.

log_info("This is an info message.")
log_warning("This is a warning message.")
log_error("This is an error message.")
