import os
import shutil
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "/Users/Shane/Downloads"

imagesFolder = "/Users/Shane/OneDrive/Desktop/Images"


def move(dest, entry, name):
  shutil.move(entry, dest)
  print("Moved " + name + " to "+ dest)
  

class MoverHandler(FileSystemEventHandler):
  def on_modified(self, event):
    with os.scandir(source_dir) as entries:
        for entry in entries:
          name = entry.name
          print(name)
          dest = source_dir
          if name.endswith(".png") or name.endswith(".jpg"):
            dest = imagesFolder
            move(dest, entry, name)

        
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
