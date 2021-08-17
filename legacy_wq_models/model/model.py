"""
basic building blocks for a model
specific execution

Features:
 - to be written
"""
# imports
import sys
import pdb

from legacy_wq_models import in_out as io
from legacy_wq_models import filer

class Error(Exception):
    """
    Base class for exceptions in this module.
    """
    pass

class InputError(Error):
    """
    Exception raised for model input errors
    
    Attributes: 
        expression -- input expression in which the error occurred
        message - explanation of the error
    """
    
    def __init__(self, message):
        self.message = message

class Model():
    """
    Basic model, called to build speicific models
    """    
    def __init__(self,
                 name='model',
                 description=''):
        """        
        :name: the name of the model 
                type - str

        :description: a written description of the model
                      type - str
        """
        # initialize attributes
        self._name = name
        self._description = description
        self.inputs = io.Container('all')
        self.outputs = io.Container('all')
        self.input_files = filer.Container()
        self.output_files = filer.Container()
        
    # placeholder functions for the functions that every model will have
    def check_input_files(self):
        error_list = list()
        print('checking input files')
        return error_list
    
    def run_model(self):
        try:
            print('model specific run command')
        except:
            print('model did not execute correctly')
    def create_input_files(self):
        for f in self.input_files:
            f.create_file()
            
    def read_output_files(self):
        for f in self.output_files:
            f.read_file()
            
    def read_input_files(self, file_path_dict):
        """
        This method loads model inputs from existing files based on the keys 
        associated with the self.input_files dictionary.
        
        Each model type must have a related method called: read_input_file 
        (note the singular) that has rules for how to read each type of file.
        """
        # check to see file_path_dict matches files required by model
        for key in self.input_files.get_all_names():
            if key not in file_path_dict.keys():
                message = key + ' - input file required for model'
                raise InputError(message)
        if len(file_path_dict.keys()) > len(self.input_files.get_all_names()):
            message = ('additional input files specified will not be read\n' + 
                       'check Model.input_files.get_all_names()')
            print(message)
        for key, value in file_path_dict.items():
            try:
                self.read_input_file(key, value)
            except OSError:
                message = value + '\n does not exist'
                raise InputError(message)
    def read_input_file(self, key, path):
        """
        Placeholder method for model specific reading of files
        """
        print('placeholder function, no inputs read to Model')
        f = open(path, 'r')
        f.close()
        

# functions
def hello():
    print('hello from model')