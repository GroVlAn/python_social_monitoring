import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        print("File changed: ", event.src_path)
        os.system("docker-compose up --build")


if __name__ == "__main__":
    os.system("docker-compose up --build")
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='./', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


