# engine.py

def start_engine():
print("Starting engine...") # No indentation

def stop_engine():
    print("Stopping engine...") # Correct indentation but inconsistent with start_engine

def get_engine_status():
status = "Running"
return status # No indentation and inconsistent

# Calling functions outside any main guard
start_engine()
print(get_engine_status())
stop_engine()
