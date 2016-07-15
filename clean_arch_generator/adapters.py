""" Adapters to interact with OS and other functions """
import os

class OsAdapter(object):
    @staticmethod
    def create_directory(path):
        if not os.path.exists(path):
            print "Created %s" % path
            os.makedirs(path)

    @staticmethod
    def touch_file(path, file_name):
        filep = path + file_name
        if not os.path.exists(filep):
            print "Created file %s" % file_name
            open(filep, 'a').close()

    @staticmethod
    def write_text(text, filename):
        with open(filename, "a") as file_:
            file_.write(text)
