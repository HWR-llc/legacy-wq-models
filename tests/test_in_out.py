"""
Tests of the input output classes.

Designed to be run with py.test
"""

import pytest
import pdb

from legacy_wq_models import in_out as io

class TestInput:
    def test_input(self):
        t_in = io.Input(value=5,
                           default=7,
                           lower_bound=1,
                           upper_bound=20,
                           typical='test typical range',
                           description='test description')
        assert t_in.get_value() == 5
        assert t_in.get_default() == 7
        assert t_in.get_typical() == 'test typical range'
        assert t_in.get_description() == 'test description'
    
    def test_lwrbnd_uprbnd(self):
        t_in = io.Input(lower_bound=7, upper_bound=15)
        assert t_in.get_typical() == '7 - 15'
        
    def test_lwrbnd(self):
        t_in = io.Input(lower_bound=7)
        assert t_in.get_typical() == '7 - N/A'

    def test_uprbnd(self):
        t_in = io.Input(upper_bound=15)
        assert t_in.get_typical() == 'N/A - 15'
    
    def test_set_value(self):
        t_in = io.Input(value=15)
        t_in.set_value(6)
        assert t_in.get_value() == 6
        
    def test_value_str(self):
        t_in = io.Input(value='DUE')
        assert t_in.get_value() == 'DUE'
        

class TestInput1D:
    def test_input1d(self):
        t_in = io.Input1D(n=8)
        assert t_in.get_value().size == 8
        assert t_in.get_value().dtype == 'float'
        
    def test_dtype(self):
        t_in = io.Input1D(n=8, dtype='int')
        assert t_in.get_value().dtype == 'int'
        

class TestInput2D:
    def test_input2d(self):
        t_in = io.Input2D(m=8, n=3)
        assert t_in.get_value().shape == (8, 3)

    def test_dtype(self):
        t_in = io.Input2D(m=8, n=3, dtype='int')
        assert t_in.get_value().dtype == 'int'

class TestInput3D:
    def test_input3d(self):
        t_in = io.Input3D(m=8, n=3, t=5)
        assert t_in.get_value().shape == (8, 3, 5) 
        
    def test_dtype(self):
        t_in = io.Input3D(m=8, n=3, t=5, dtype='int')
        assert t_in.get_value().dtype == 'int'
        
class TestOutput:
    def test_output(self):
        t_out = io.Output(value=5,
                           description='test description')
        assert t_out.get_value() == 5
        assert t_out.get_description() == 'test description'
    
    def test_set_value(self):
        t_out = io.Output(value=15)
        t_out.set_value(6)
        assert t_out.get_value() == 6

class TestOutput1D:
    def test_output1d(self):
        t_out = io.Output1D(n=8)
        assert t_out.get_value().size == 8
        assert t_out.get_value().dtype == 'float'
        
    def test_dtype(self):
        t_out = io.Output1D(n=8, dtype='int')
        assert t_out.get_value().dtype == 'int'
        

class TestOutput2D:
    def test_output2d(self):
        t_out = io.Output2D(m=8, n=3)
        assert t_out.get_value().shape == (8, 3)

    def test_dtype(self):
        t_out = io.Output2D(m=8, n=3, dtype='int')
        assert t_out.get_value().dtype == 'int'

class TestOutput3D:
    def test_output3d(self):
        t_out = io.Output3D(m=8, n=3, t=5)
        assert t_out.get_value().shape == (8, 3, 5) 
        
    def test_dtype(self):
        t_out = io.Output3D(m=8, n=3, t=5, dtype='int')
        assert t_out.get_value().dtype == 'int'