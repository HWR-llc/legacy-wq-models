"""
Tests of the filer classes.

Designed to be run with py.test
"""

import pytest
import os
import pdb

from legacy_wq_models import filer

class TestInOutFile:
    def test_file(self):
        f_in = filer.InOutFile(name='test_name',
                               location='',
                               extension='inp',
                               description='brief description of test_name file')
        assert f_in.get_name() == 'test_name'
        assert f_in.get_location() == ''
        assert f_in.get_extension() == 'inp'
        assert f_in.get_description() == 'brief description of test_name file'
    
    def test_period(self):
        f_in = filer.InOutFile(extension='inp')
        assert f_in.get_extension() == 'inp'

    def test_no_period(self):
        f_in2 = filer.InOutFile(extension='.inp')
        assert f_in2.get_extension() == 'inp'   

    def test_set(self):
        f_in = filer.InOutFile(name='test_name',
                               location='',
                               extension='inp',
                               description='brief description of test_name file')
        f_in.set_name('test_name2')
        assert f_in.get_name() == 'test_name2'
        f_in.set_location('location2')
        assert f_in.get_location() == 'location2'
        
    def test_full_path(self):
        f_in = filer.InOutFile(name='test_name',
                               location='',
                               extension='inp',
                               description='brief description of test_name file')
        cur_dir = os.getcwd()
        full_path = os.path.join(cur_dir, 'test_name.inp')
        assert f_in.get_full_path() == full_path
                
        