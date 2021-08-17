"""
basic building blocks for file management for use in developing model
specific files (i.e., input and output files)

Features:
 - to be written
"""
# imports
import pdb
import os
    
# classes
class InOutFile():
    """
    Generic file class for inputs and outputs
    """    
    def __init__(self,
                 name='file',
                 location='',
                 extension='txt',
                 description=''):
        """      
        :name : name of file without extension
                type - str

        :location : directory where file exists or should be created
                  type - str
                  
        :extension : file name extension e.g., 'inp'
                       type - str

        :description : a written description of the file
                      type - str
        """
        # initialize attributes
        self.name = name
        self.location = location
        self._extension = extension
        self._description = description
        self._full_path = ''
        
        # check to make sure '.' is not in extension
        self.trim_extension()        
        # set full path for execution
        self.update_full_path()


    # input checking
    def update_full_path(self):
        full_name = self.name + '.' + self._extension
        if self.location == '':
            cur_dir = os.getcwd()
            full_path = os.path.join(cur_dir, full_name)
            self._full_path = full_path
        else:
            if os.path.isdir(self.location):
                full_path = os.path.join(self.location, full_name)
                self._full_path = full_path
            else:
                # will eventually need to be a warning in logging
                print(self.location + ' does not exist')                

    def trim_extension(self):
        ext_check = self.get_extension()
        if ext_check[0] == '.':
            self._extension = ext_check[1:]
            # will eventually need to be a warning in logging
            print('extension should not include "."')
        
    # getter methods
    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location
    
    def get_extension(self):
        return self._extension
    
    def get_description(self):
        return self._description
    
    def get_full_path(self):
        return self._full_path
    
    # setter methods
    def set_name(self, new_name):
        self.name = new_name
        self.update_full_path()
        
    def set_location(self, new_location):
        self.location = new_location
        self.update_full_path()

class InputFile(InOutFile):
    """
    File that will be read by model that includes model inputs
    """    
    def __init__(self,
                 name='input_file',
                 location='',
                 extension='txt',
                 description=''):
        super(InputFile, self).__init__(name,
                                        location,
                                        extension,
                                        description)
       
    # create file
    def create_file():
        """
        This is a placeholder method. Each model type (e.g., STFATE) will have
        a model specific version of this method.
        """
        print('placeholder function only')

class OutputFile(InOutFile):
    """
    File that will be read by model that includes model inputs
    """    
    def __init__(self,
                 name='output_file',
                 location='',
                 extension='txt',
                 description=''):
        super(OutputFile, self).__init__(name,
                                      location,
                                      extension,
                                      description)
       
    # create file
    def read_file():
        """
        This is a placeholder method. Each model type (e.g., STFATE) will have
        a model specific version of this method.
        """
        print('placeholder function only')
        
class Container():
    """
    container for all files for a articular model
    """     
    def __init__(self):
        self.contents = dict()
        self.size = 0
        
    def append(self, put):
        all_names = self.get_all_names()
        if put.get_name() not in all_names:
            self.contents[put.get_name()] = put
            self.size = len(self.contents)
        else:
            # eventually needs to be error/warning in logging
            print('file already in container')
        
    def multi_append(self, puts):
        for put in puts:
            self.append(put)
    
    def remove_by_name(self, put_name):
        all_names = self.get_all_names()
        if put_name in all_names:
            self.contents.pop(put_name)
            self.size = len(self.contents)
        else:
            # eventually needs to be error/warning in logging
            print('input not in container')        

    def get_all_names(self):
        return_list = []
        for key in self.contents:
            return_list.append(self.contents[key].get_name())
        return return_list
    
        
# functions
def hello():
    print('hello from filer!')