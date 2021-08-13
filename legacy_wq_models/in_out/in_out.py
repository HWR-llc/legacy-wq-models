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
                 name='',
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''):
        """
        This class will only be called by dimensional inputs (e.g., Input_0D)
        
        :name: the name of the model input, for use in collection
                type - str
                
        :value: the value of the model input expect 0D, 1D, 2D, 3D, structured dataset
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
        self._name = name
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
    def get_name(self):
        return self._name
    
    def get_value(self):
        return self.value
    
    def get_default(self):
        return self._default
    
    def get_typical(self):
        return self._typical
    
    def get_description(self):
        return self._description
          
    def name_iter(self):
        if self._name.isnumeric():
            new_name_num = int(self._name)
            self._name = str(new_name_num + 1)

    def value_check(self):
        print('method for checking value')
            
class Input0D(Input):
    """
    0-dimensional model input i.e., a number
    """    
    def __init__(self,
                 name='',
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''):
        super(Input0D, self).__init__(name,
                                      value,
                                      default,
                                      lower_bound,
                                      upper_bound,
                                      typical,
                                      description)

        
    # setter methods only allowable property to set is value
    def set_value(self, new_value):
        # input validation can be completed for child classes
        self.value = new_value
        
    def value_check(self):
        if type(self.value) == int or float:
            if (type(self._Input__lwrbnd) == type(self.value)) and (type(self._Input__uprbnd) == type(self.value)):
                if self.value <= self._Input__uprbnd and self.value >= self._Input__lwrbnd:
                    return True
                else:
                    return False
            else:
                print('lower_bound or upper_bound is not defined consistent with value')
                return True
        else:
            print('value datatype is non-numeric')
            return True

class Input1D(Input):
    """
    1-dimensional model input i.e., an array
    """    
    def __init__(self,
                 n=0,
                 dtype='float',
                 name='',
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''): 
        super(Input1D, self).__init__(name,
                                      value,
                                      default,
                                      lower_bound,
                                      upper_bound,
                                      typical,
                                      description)
        
        if n > 0:
            self.set_value(n, dtype)
        
        
    def set_value(self, n, dtype):
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
                 name='',
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''): 
        super(Input2D, self).__init__(name,
                                      value,
                                      default,
                                      lower_bound,
                                      upper_bound,
                                      typical,
                                      description)
        
        if n > 0 and m > 0:
            self.set_value(m, n, dtype)
        
    def set_value(self, m, n, dtype):
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
                 name='',
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''): 
        super(Input3D, self).__init__(name,
                                      value,
                                      default,
                                      lower_bound,
                                      upper_bound,
                                      typical,
                                      description)
        
        if n > 0 and m > 0:
            self.set_value(m, n, t, dtype)
        
    def set_value(self, m, n, t, dtype):
        self.value = np.zeros((m, n, t), dtype=dtype)
        
    def value_check(self):
        print('method for checking values in array')

class InputStructured(Input):
    """
    A structured array model input i.e., a table per numpy structured array
    """    
    def __init__(self,
                 fields,
                 dtypes,
                 rows=0,
                 name='',
                 value=None,
                 default=None,
                 lower_bound=None,
                 upper_bound=None,
                 typical='',
                 description=''): 
        super(InputStructured, self).__init__(name,
                                      value,
                                      default,
                                      lower_bound,
                                      upper_bound,
                                      typical,
                                      description)
        self._fields = fields
        self._dtypes = dtypes
        self.set_rows(rows)

        
    def set_rows(self, rows):
        fld_dtp = dict(names = self._fields, formats=self._dtypes)
        self.value = np.zeros(rows, dtype=fld_dtp)
        
    def set_value(self, new_value):
        if len(new_value) == self.value.size:
            for i in range(0,len(new_value)):
                self.value[i] = new_value[i]
        else:
            print('raise error')
                
        
    def value_check(self):
        print('method for checking values in array')

class Output():
    """
    Basic model output, called to build inputs with dimensions
    """    
    def __init__(self,
                 name='',
                 value=None,
                 description=''):
        """
        This class will only be called by dimensional outputs (e.g., Output_0D)
        
        :name: name of output
                type - str 

        :value: the value of the model output expect 0D, 1D, 2D, 3D, 4D dataset
                type - str or number, array, matrix etc.

        :description: a written description of input
                      type - str
        """
        # initialize attributes
        self._name = name
        self.value = value
        self._description = description
        
    # getter methods
    def get_name(self):
        return self._name
    
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
                 name='',
                 value=None,
                 description=''):
        super(Output0D, self).__init__(name,
                                       value,
                                      description)

class Output1D(Output):
    """
    1-dimensional model output i.e., an array
    """    
    def __init__(self,
                 n=0,
                 dtype='float',
                 name='',
                 value=None,
                 description=''): 
        super(Output1D, self).__init__(name,
                                       value,
                                      description)
        
        if n > 0:
            self.set_value(n, dtype)
        
        
    def set_value(self, n, dtype):
        self.value = np.zeros(n, dtype=dtype)

class Output2D(Output):
    """
    2-dimensional model output i.e., a 2-D array/matrix
    """    
    def __init__(self,
                 m=0,
                 n=0,
                 dtype='float',
                 name='',
                 value=None,
                 description=''): 
        super(Output2D, self).__init__(name,
                                       value,
                                       description)
        
        if n > 0 and m > 0:
            self.set_value(m, n, dtype)
        
    def set_value(self, m, n, dtype):
        self.value = np.zeros((m, n), dtype=dtype)

class Output3D(Output):
    """
    3-dimensional model Output i.e., a 3-D array, matrix
    """    
    def __init__(self,
                 m=0,
                 n=0,
                 t=0,
                 dtype='float',
                 name='',
                 value=None,
                 description=''): 
        super(Output3D, self).__init__(name,
                                       value,
                                       description)
        
        if n > 0 and m > 0:
            self.set_value(m, n, t, dtype)
        
    def set_value(self, m, n, t, dtype):
        self.value = np.zeros((m, n, t), dtype=dtype)

class Container():
    """
    container for all inputs or outputs for a particular model
    """     
    def __init__(self,
                 name,
                 description=''):
        self.contents = dict()
        self.size = 0
        self.name = name
        self._description = description
        
    def append(self, put):
        all_names = self.get_contents_names()
        if put.get_name() not in all_names:
            self.contents[put.get_name()] = put
            self.size = len(self.contents)
        else:
            # eventually needs to be error/warning in logging
            print('input already in container')
        
    def multi_append(self, puts):
        for put in puts:
            self.append(put)
    
    def remove_by_name(self, put_name):
        all_names = self.get_contents_names()
        if put_name in all_names:
            self.contents.pop(put_name)
            self.size = len(self.contents)
        else:
            # eventually needs to be error/warning in logging
            print('input not in container')

    def get_name(self):
        return self.name

    def get_description(self):
        return self._description
    
    def get_contents_names(self):
        return_list = []
        for key in self.contents:
            return_list.append(self.contents[key].get_name())
        return return_list
    def get_contents(self):
        return self.contents
    
# functions
def hello():
    print('hello from in_out!')