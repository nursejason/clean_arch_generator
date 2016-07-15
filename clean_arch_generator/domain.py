""" Domain knowledge of what classes should look like. """
# TODO
# Create various common adapters
  # mysql
  # kafka
  # couchbase
  # elastic
# Create basic conf file setup
def create_classes_string(class_name):
    return """
class %s(object):
    pass
    """ % _format_class_name(class_name)

def _format_class_name(class_name):
    """ Like the capwords function, but gets rid of underscores """
    words = class_name.split('_')
    cap_words = []
    for word in words:
        cap_words.append(word.capitalize())
    return ''.join(cap_words)

class AdapterFile(object):
    def __init__(python_imports, external_imports, from_imports, adapters):
        pass

    def format_as_string(self):
        pass

    @classmethod
    def create(adapters_list):
        python_imports = []
        external_imports = []
        from_imports = []

        for adapter in adapters_list:
            python_imports.append(adapter.python_imports)
            external_imports.append(adapter.external_imports)
            from_imports.append(adapter.from_imports)
