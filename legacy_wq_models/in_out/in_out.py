"""
basic building blocks for inputs and outputs for use in developing model
specific input and output

Features:
 - to be written
"""
# imports
import pdb
import numpy as np

# classes
class Input():
    """
    Basic model input, called to build inputs with dimensions
    """    
    def __init__(self,
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''):
        """
        This class will only be called by dimensional inputs (e.g., Input_0D)
        
        :value: the value of the model input expect 0D, 1D, 2D, 3D, 4D dataset
                type - str or number, array, matrix etc.

        :default: a value that can be used if value not specified
                  type - see value
                  
        :lower_bound : lower end of range of values that are typical for the 
                       input, not always appicable (e.g., no typical depth)
                       type - str
            
        :upper_bound : upper end of range of values that are typical for the 
                       input, not always appicable (e.g., no typical depth)
                       type - str

        :description: a written description of input
                      type - str
        """
        # initialize attributes
        self.value = value
        self._default = default
        self.__lwrbnd = lower_bound
        self.__uprbnd = upper_bound
        self._typical = typical
        self._description = description
        if (self._typical == '') and (self.__lwrbnd is not None or
                                      self.__uprbnd is not None):
            if self.__lwrbnd is None:
                self._typical = 'N/A - ' + str(self.__uprbnd)
            elif self.__uprbnd is None:
                self._typical = str(self.__lwrbnd) + ' - N/A'
            elif self.__lwrbnd is not None and self.__uprbnd is not None:
                self._typical = str(self.__lwrbnd) + ' - ' + str(self.__uprbnd)
        
    # getter methods
    def get_value(self):
        return self.value
    
    def get_default(self):
        return self._default
    
    def get_typical(self):
        return self._typical
    
    def get_description(self):
        return self._description
    
    # setter methods only allowable property to set is value
    def set_value(self, new_value):
        # input validation can be completed for child classes
        self.value = new_value
            
class Input0D(Input):
    """
    0-dimensional model input i.e., a number
    """    
    def __init__(self,
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''):
        super(Input0D, self).__init__(value,
                                      default,
                                      lower_bound,
                                      upper_bound,
                                      typical,
                                      description)

        
    def value_check(self):
        print('method for checking value')

class Input1D(Input):
    """
    1-dimensional model input i.e., an array
    """    
    def __init__(self,
                 n=0,
                 dtype='float',
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''): 
        super(Input1D, self).__init__(value,
                                      default,
                                      lower_bound,
                                      upper_bound,
                                      typical,
                                      description)
        
        if n > 0:
            self.set_value_array(n, dtype)
        
        
    def set_value_array(self, n, dtype):
        self.value = np.zeros(n, dtype=dtype)
        
    def value_check(self):
        print('method for checking values in array')

class Input2D(Input):
    """
    2-dimensional model input i.e., a 2-D array/matrix
    """    
    def __init__(self,
                 m=0,
                 n=0,
                 dtype='float',
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''): 
        super(Input2D, self).__init__(value,
                                      default,
                                      lower_bound,
                                      upper_bound,
                                      typical,
                                      description)
        
        if n > 0 and m > 0:
            self.set_value_array(m, n, dtype)
        
    def set_value_array(self, m, n, dtype):
        self.value = np.zeros((m, n), dtype=dtype)
        
    def value_check(self):
        print('method for checking values in array')

class Input3D(Input):
    """
    3-dimensional model input i.e., a 3-D array, matrix
    """    
    def __init__(self,
                 m=0,
                 n=0,
                 t=0,
                 dtype='float',
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''): 
        super(Input3D, self).__init__(value,
                                      default,
                                      lower_bound,
                                      upper_bound,
                                      typical,
                                      description)
        
        if n > 0 and m > 0:
            self.set_value_array(m, n, dtype)
        
    def set_value_array(self, m, n, t, dtype):
        self.value = np.zeros((m, n, t), dtype=dtype)
        
    def value_check(self):
        print('method for checking values in array')

class Output():
    """
    Basic model output, called to build inputs with dimensions
    """    
    def __init__(self,
                 value=None,
                 description=''):
        """
        This class will only be called by dimensional outputs (e.g., Output_0D)
        
        :value: the value of the model output expect 0D, 1D, 2D, 3D, 4D dataset
                type - str or number, array, matrix etc.

        :description: a written description of input
                      type - str
        """
        # initialize attributes
        self.value = value
        self.description = description
        
    # getter methods
    def get_value(self):
        return self.value
    
    def get_description(self):
        return self._description
    
    # setter methods only allowable property to set is value
    def set_value(self, new_value):
        # input validation can be completed for child classes
        self.value = new_value

class Output0D(Output):
    """
    0-dimensional model output i.e., a number
    """    
    def __init__(self,
                 value=None,
                 description=''):
        super(Output0D, self).__init__(value,
                                      description)
        
    def value_check(self):
        print('method for checking value')

class Output1D(Output):
    """
    1-dimensional model output i.e., an array
    """    
    def __init__(self,
                 n=0,
                 dtype='float',
                 value=None,
                 description=''): 
        super(Input1D, self).__init__(value,
                                      description)
        
        if n > 0:
            self.set_value_array(n, dtype)
        
        
    def set_value_array(self, n, dtype):
        self.value = np.zeros(n, dtype=dtype)
        
    def value_check(self):
        print('method for checking values in array')

class Output2D(Output):
    """
    2-dimensional model output i.e., a 2-D array/matrix
    """    
    def __init__(self,
                 m=0,
                 n=0,
                 dtype='float',
                 value=None,
                 description=''): 
        super(Output2D, self).__init__(value,
                                      description)
        
        if n > 0 and m > 0:
            self.set_value_array(m, n, dtype)
        
    def set_value_array(self, m, n, dtype):
        self.value = np.zeros((m, n), dtype=dtype)
        
    def value_check(self):
        print('method for checking values in array')

class Output3D(Output):
    """
    3-dimensional model Output i.e., a 3-D array, matrix
    """    
    def __init__(self,
                 m=0,
                 n=0,
                 t=0,
                 dtype='float',
                 value=None,
                 description=''): 
        super(Output3D, self).__init__(value,
                                      description)
        
        if n > 0 and m > 0:
            self.set_value_array(m, n, dtype)
        
    def set_value_array(self, m, n, t, dtype):
        self.value = np.zeros((m, n, t), dtype=dtype)
        
    def value_check(self):
        print('method for checking values in array')

# functions
def hello():
    print('hello from in_out!')
    
# classes