""" Main pass through to call app """
from clean_arch_generator.application import create_clean_project

def main(**kwargs):
    create_clean_project(**kwargs)
