import os

from pathlib import Path


class PathDB:
    def __init__(self):
        self.path = Path(__file__).resolve().parent.parent / "database"