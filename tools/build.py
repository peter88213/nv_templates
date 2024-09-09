"""Build the nv_templates novelibre plugin package.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the novxlib package.

The novxlib project (see see https://github.com/peter88213/novxlib)
must be located on the same directory level as the nv_templates project. 

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/nv_templates
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from shutil import copytree
import sys

sys.path.insert(0, f'{os.getcwd()}/../../novelibre/tools')
from package_builder import PackageBuilder

VERSION = '4.1.1'


class PluginBuilder(PackageBuilder):

    PRJ_NAME = 'nv_templates'
    LOCAL_LIB = 'nvtemplateslib'
    GERMAN_TRANSLATION = True

    def add_extras(self):
        self.add_sample()

    def add_sample(self):
        print('\nAdding sample files ...')
        SAMPLE_DIR = '../sample'
        copytree(SAMPLE_DIR, f'{self.buildDir}/sample')


def main():
    pb = PluginBuilder(VERSION)
    pb.run()


if __name__ == '__main__':
    main()
