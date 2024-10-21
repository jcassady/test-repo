# app.py

from logging import log_info, log_warning, log_error  # Importing logging functions

class PitStop:
    def __call__(self, *drivers):
        lap_times = ' '.join(drivers[::-1])
        log_info(f"Drivers entering the pit stop: {lap_times}")  # Using the log_info function

if __name__ == "__main__":
    try:
        PitStop()("Hamilton", "Verstappen", "Leclerc")
        log_info("PitStop executed successfully.")
    except Exception as e:
        log_error(f"Error occurred: {e}")
