import os
from os import getlogin


class HostUtils:
    def __init__(self):
        self._username = getlogin()

    def get_username(self):
        return self._username

    def get_current_path(self):
        return os.curdir
