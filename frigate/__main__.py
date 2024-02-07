import faulthandler
import threading
import multiprocessing
from flask import cli

from frigate.app import FrigateApp
multiprocessing.set_start_method("spawn")
multiprocessing.set_executable("/snap/frigate/current/frigate/bin/python.sh")

faulthandler.enable()

threading.current_thread().name = "frigate"

cli.show_server_banner = lambda *x: None

if __name__ == "__main__":
    frigate_app = FrigateApp()

    frigate_app.start()
