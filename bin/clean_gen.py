import argparse
import os
import sys

sys.path.append(os.path.realpath('..'))
from clean_arch_generator.main import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_dir", action="store",
                        dest="base", help="Base repo directory")
    parser.add_argument("--parent", action="store",
                         dest="parent", help="Parent project name")
    parser.add_argument("--child", action="store",
                        dest="child", help="Child project name")
    parser.add_argument("--domain", action="store",
                        dest="domain", help="Domain classes", default=[])
    parser.add_argument("--adapter", action="store", default=[],
                        dest="adapter", help="Services being used i.e MySQL")
    parser.add_argument("--handler", action="store",
                        dest="handler", help="Handler classes", default=[])
    parser.add_argument("-flask", action="store_true",
                        dest="flask", help="Add Flask API bootstrapping")
    parser.add_argument("-new", action="store_true",
                        dest="new", help="Create new directory")
    args = parser.parse_args()
    main(**args.__dict__)
