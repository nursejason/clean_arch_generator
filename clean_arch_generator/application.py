""" App knowledge needed to create a project in Clean stlye """
from clean_arch_generator.domain import create_class_string

def create_clean_project(context, **kwargs):
    """ Main driver to create a clean project """
    lib_path = kwargs['base']
    if kwargs.get('new', True):
        lib_path = create_project_dir(
            context, kwargs['base'], kwargs['parent'], kwargs['child'])

    create_project_files(context, kwargs['base'], kwargs['parent'], kwargs['child'])

    add_adapter_classes(context, lib_path, kwargs.get('adapter', []))
    add_handler_classes(context, lib_path, kwargs.get('handler', []))
    add_domain_classes(context, lib_path, kwargs.get('domain', []))

def create_project_dir(context, base_repo, parent_project, child_project):
    """ Create the new project directory """
    path = '%s/lib/%s/' % (base_repo, parent_project)
    if child_project is not None:
        path = path + '%s/' % child_project
    print 'Creating directories. New lib path %s.' % path
    context.create_directory(path)

    return path

def create_project_files(context, base_repo, parent_project, child_project):
    files = ['domain.py', 'adapters.py', 'handlers.py',
             'application.py', 'main.py', '__init__.py']
    path = '%s/lib/%s/' % (base_repo, parent_project)
    if child_project is not None:
        path = path + '%s/' % child_project
    for file_ in files:
        context.touch_file(path, file_)
    # TODO
    ## Not all init files are being created
    ## Conf dir
    ## Conf files

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
