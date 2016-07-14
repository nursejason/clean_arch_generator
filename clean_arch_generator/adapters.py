""" Adapters to interact with OS and other functions """
import os

class OsAdapter(object):
    @staticmethod
    def create_directory(path):
        if not os.path.exists(path):
            print "created %s" % path
            os.makedirs(path)

    @staticmethod
    def touch_file(path, file_name):
        filep = path + file_name
        if not os.path.exists(filep):
            print "created file %s" % file_name
            open(filep, 'a').close()
