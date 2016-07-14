
def create_clean_project(**kwargs):
    if kwargs.get('new', True):
        create_project_dir(kwargs['base'], kwargs['parent'], kwargs['child'])

    create_project_files(kwargs['base'], kwargs['parent'], kwargs['child'])

    path = '%s/lib/%s/%s/' % (kwargs['base'], kwargs['parent'], kwargs['child'])
    add_adapter_classes(path, kwargs.get('adapter', []))
    add_handler_classes(path, kwargs.get('handler', []))
    add_domain_classes(path, kwargs.get('domain', []))

def create_project_dir(base_repo, parent_project, child_project):
    pass

def create_project_files(base_repo, parent_project, child_project):
    pass

def add_adapter_classes(project_path, class_list):
    add_classes(project_path, class_list, 'adapters')

def add_handler_classes(project_path, class_list):
    add_classes(project_path, class_list, 'handlers')

def add_domain_classes(project_path, class_list):
    add_classes(project_path, class_list, 'domain')

def add_classes(project_path, class_list, class_file):
    pass

#def validate_args(**kwargs):
#    domain
#    adapter
#    handler
#
#    base
#    child
#    parent
#
#    flask
