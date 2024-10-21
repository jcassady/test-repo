# app.py

from logging import log_info, log_warning, log_error  # Importing logging functions
from module.tires import Tire  # Importing the Tire class

class PitStop:
    def __call__(self, *drivers):
        lap_times = ' '.join(drivers[::-1])
        log_info(f"Drivers entering the pit stop: {lap_times}")  # Using the log_info function
        # Referencing Tire class for demonstration
        tire = Tire(205, 55, 16)
        tire_size = tire.size()
        log_info(f"Measured tire size: {tire_size:.2f} inches")

if __name__ == "__main__":
    try:
        PitStop()("Hamilton", "Verstappen", "Leclerc")
        log_info("PitStop executed successfully.")
    except Exception as e:
        log_error(f"Error occurred: {e}")
