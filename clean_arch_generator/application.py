""" App knowledge needed to create a project in Clean stlye """
from clean_arch_generator.domain import create_class_string

def create_clean_project(context, **kwargs):
    """ Main driver to create a clean project """
    lib_path = _get_lib_path(kwargs.get('new', True),
                             kwargs['base'], kwargs['parent'], kwargs['child'])
    conf_path = _get_conf_path(kwargs['base'])
    if kwargs.get('new', True):
        create_project_dir(context, lib_path, conf_path)
        create_conf_files(context, conf_path)

    create_project_files(context, kwargs['base'], kwargs['parent'], kwargs['child'])

    add_adapter_classes(context, lib_path, kwargs.get('adapter', []))
    add_handler_classes(context, lib_path, kwargs.get('handler', []))
    add_domain_classes(context, lib_path, kwargs.get('domain', []))

def create_project_dir(context, path, conf_path):
    """ Create the new project directory and conf dir """
    print 'Creating directories:'
    print 'New lib path %s.' % path
    context.create_directory(path)

    conf_path = '%s/conf' % base_repo
    print 'Creating conf at %s' % conf_path
    context.create_directory(conf_path)


def create_project_files(context, base_repo, parent_project, child_project):
    print 'Creating files in directories'
    files = ['domain.py', 'adapters.py', 'handlers.py',
             'application.py', 'main.py', '__init__.py']

    path = '%s/lib/' % base_repo
    context.touch_file(path, '__init__.py')
    path += '/' + parent_project + '/'
    context.touch_file(path, '__init__.py')

    if child_project is not None:
        path = path + '%s/' % child_project
    for file_ in files:
        context.touch_file(path, file_)

def create_conf_files(context, conf_path):
    context.touch_file(conf_path, 'config.py')

def add_adapter_classes(context, project_path, class_list):
    add_classes(context, project_path, class_list, 'adapters')

def add_handler_classes(context, project_path, class_list):
    add_classes(context, project_path, class_list, 'handlers')

def add_domain_classes(context, project_path, class_list):
    add_classes(context, project_path, class_list, 'domain')

def add_classes(context, project_path, class_list, class_file):
    filename = '%s/%s.py' % (project_path, class_file)

    if len(class_list) == 0:
        print 'No classes to be created for %s.' % class_file
        return

    print 'Creating classes %s in %s.' % (class_list, class_file)
    file_string = ''
    for class_ in class_list:
        file_string += create_class_string(class_)

    context.write_text(file_string, filename)

def _get_lib_path(new_project, base_repo, parent_project, child_project):
    lib_path = base_repo
    if new_project:
        lib_path = '%s/lib/%s/' % (base_repo, parent_project)
        if child_project is not None:
            lib_path = lib_path + '%s/' % child_project
    return lib_path

def _get_conf_path(base_repo):
    return '%s/conf' % base_repo
