""" Adapters to interact with OS and other functions """
import os

class OsAdapter(object):
    @staticmethod
    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
