# logging.py

def log_info(message):
    print(f"PITSTOP INFO: {message}")  # Improved format for readability.

def log_warning(message):
    print(f"PITSTOP WARNING: {message}")  # Consistent formatting with string interpolation.

def log_error(message):
    print(f"PITSTOP ERROR: {message}")  # Consistent formatting and clearer error indication.

log_info("Driver entering the pit stop.")
log_warning("Pit crew delay.")
log_error("Engine failure in the pit stop.")
