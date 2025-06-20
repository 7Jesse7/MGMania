import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # usado no PyInstaller
    except AttributeError:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # modo dev
    return os.path.join(base_path, relative_path)
