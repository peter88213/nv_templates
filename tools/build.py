"""Build the nv_templates novelibre plugin package.
        
Note: VERSION must be updated manually before starting this script.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_templates
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys

sys.path.insert(0, f'{os.getcwd()}/../../novelibre/tools')
from package_builder import PackageBuilder

VERSION = '5.1.2'


class PluginBuilder(PackageBuilder):

    PRJ_NAME = 'nv_templates'
    LOCAL_LIB = 'nvtemplates'
    GERMAN_TRANSLATION = True

    def add_extras(self):
        self.add_sample()


def main():
    pb = PluginBuilder(VERSION)
    pb.run()


if __name__ == '__main__':
    main()
