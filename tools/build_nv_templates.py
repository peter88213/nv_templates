"""Build a templates noveltree plugin.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the novxlib package.

The novxlib project (see https://github.com/peter88213/novxlib)
must be located on the same directory level as the nv_templates project. 

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/noveltree_templates
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../novxlib/src')
import inliner

SRC = '../src/'
BUILD = '../test/'
SOURCE_FILE = f'{SRC}nv_templates.py'
TARGET_FILE = f'{BUILD}nv_templates.py'


def main():
    inliner.run(SOURCE_FILE, TARGET_FILE, 'nvtemplateslib', '../../noveltree_templates/src/')
    inliner.run(TARGET_FILE, TARGET_FILE, 'noveltreelib', '../../noveltree/src/')
    print('Done.')


if __name__ == '__main__':
    main()
