""" App knowledge needed to create a project in Clean stlye """

def create_clean_project(context, **kwargs):
    """ Main driver to create a clean project """
    lib_path = kwargs['base']
    if kwargs.get('new', True):
        lib_path = create_project_dir(
            context, kwargs['base'], kwargs['parent'], kwargs['child'])

    create_project_files(context, kwargs['base'], kwargs['parent'], kwargs['child'])

    #add_adapter_classes(lib_path, kwargs.get('adapter', []))
    #add_handler_classes(lib_path, kwargs.get('handler', []))
    #add_domain_classes(lib_path, kwargs.get('domain', []))

def create_project_dir(context, base_repo, parent_project, child_project):
    """ Create the new project directory """
    path = '%s/lib/%s/' % (base_repo, parent_project)
    if child_project is not None:
        path = path + '%s/' % child_project
    print 'Creating directories. New lib path %s.' % path
    context.create_directory(path)

    return path

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


def add_adapter_classes(project_path, class_list):
    add_classes(project_path, class_list, 'adapters')

def add_handler_classes(project_path, class_list):
    add_classes(project_path, class_list, 'handlers')

def add_domain_classes(project_path, class_list):
    add_classes(project_path, class_list, 'domain')

def add_classes(project_path, class_list, class_file):
    pass
