""" Domain knowledge of what classes should look like. """
def create_class_string(class_name):
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
