import os
import signal
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ConfigChangeHandler(FileSystemEventHandler):
    def __init__(self, process):
        self.process = process

    def on_modified(self, event):
        if event.src_path.endswith("settings.json"):
            print(f"{event.src_path} has been modified, restarting the application...")
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            self.process = subprocess.Popen(["uvicorn", "app.main:app", "--reload"], preexec_fn=os.setsid)

def start_uvicorn():
    process = subprocess.Popen(["uvicorn", "app.main:app", "--reload"], preexec_fn=os.setsid)
    return process

if __name__ == "__main__":
    process = start_uvicorn()
    event_handler = ConfigChangeHandler(process)
    observer = Observer()
    observer.schedule(event_handler, path='./config', recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
