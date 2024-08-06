import os
from pathlib import Path

path = Path("/here/your/path/file.txt")
print(path.parent.absolute())


SRC_DIR = Path(os.path.dirname(os.path.realpath(__file__))).parent.absolute()

BCK_DIR = os.path.join(SRC_DIR, "bck")

DATA_DIR = os.path.join(SRC_DIR, "data")
CLEAN_DIR = os.path.join(DATA_DIR, "clean")
RAW_DIR = os.path.join(DATA_DIR, "raw")
FINAL_DIR = os.path.join(DATA_DIR, "final")


