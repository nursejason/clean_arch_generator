""" Main pass through to call app """
from clean_arch_generator.application import create_clean_project
from clean_arch_generator.adapters import OsAdapter

def main(**kwargs):
    create_clean_project(OsAdapter(), **kwargs)
