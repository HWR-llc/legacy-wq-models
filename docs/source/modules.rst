Modules
========================
Three modules makeup the basic building blocks of legacy-wq-models. These modules are invoked in model specific implementations of legacy-wq-models (e.g., STFATE). 

The modules are:

model_
   includes just one class, Model(). The class includes a set of attributes for storing all of the model inputs, model outputs, and references to model files. The class also includes a set of methods that can be run on the attributes of the class. For example, Model.check_input_files() checks al of the input files to make sure they are formatted correctly for the model to run.

filer_
  includes a generic file class and the inputFile class and outputFile class which are instantiations of the generic file class. The module also includes a FileContainer class. The FileContainer class stores all of the input and output files for a model.

in_out_
  includes a set of classes for various types of model inputs and outputs. These inputs/outputs can be 0-dimensional, 1-dimensional, 2-dimensional, 3-dimensional, or a numpy structured array. 

, an outputFile class, and a generic 

.. _model:

model
-----



.. _filer:

filer
-----

The filer module includes 

.. _in_out:

in_out
------


