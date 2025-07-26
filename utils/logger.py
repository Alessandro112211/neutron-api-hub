import datetime

def log_event(message):
    timestamp = datetime.datetime.now().isoformat()
    with open("logs/system.log", "a") as log_file:
        log_file.write(f"{timestamp} - {message}\n")
