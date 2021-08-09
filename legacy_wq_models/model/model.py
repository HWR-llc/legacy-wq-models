"""
basic building blocks for a model
specific execution

Features:
 - to be written
"""
# imports
import pdb

from legacy_wq_models import in_out as io
from legacy_wq_models import filer

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
        self.inputs = io.InOutContainer('all')
        self.outputs = io.InOutContainer('all')
        self.input_files = filer.FileContainer()
        self.output_files = filer.FileContainer()
        
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

# functions
def hello():
    print('hello from model')