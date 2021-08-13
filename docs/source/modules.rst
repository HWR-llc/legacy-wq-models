Class Reference
========================
Three modules makeup the basic building blocks of legacy-wq-models (l-wq-m). These modules are invoked in model specific implementations of legacy-wq-models (e.g., STFATE). 

The modules are:

model_
   includes just one class, Model(). The class includes a set of attributes for storing all of the model inputs, model outputs, and references to model files. The class also includes a set of methods that can be run on the attributes of the class. For example, Model.check_input_files() checks al of the input files to make sure they are formatted correctly for the model to run.

filer_
  includes a generic file class and the inputFile class and outputFile class which are instantiations of the generic file class. The module also includes a FileContainer class. The FileContainer class stores all of the input and output files for a model.

in_out_
  includes a set of classes for various types of model inputs and outputs. These inputs/outputs can be 0-dimensional, 1-dimensional, 2-dimensional, 3-dimensional, or a numpy structured array. 

.. _model:

model classes
-------------

Model()
^^^^^^^

This is the main class invoked for each numerical model.

``l-wq-m.model.Model(name='model', description='')``

*Parameters:*

- ``name`` - model name as string
- ``description`` - model description as string

*Attributes:*

- ``name`` - see parameter: name, protected
- ``description`` - see parameter: description, protected
- ``inputs`` - storage for model inputs [class in_out.InOutContainer('all')]
- ``outputs`` - storage for model outputs [class in_out.InOutContainer('all')]
- ``input_files`` - storage for references to input files [class filer.FileContainer()]
- ``output_files`` - storage for references to output files [class filer.FileContainer()]

*Methods:*

- ``check_input_files()`` - evaluates Model.inputs against configuration rules in xxxx, returns ___ if rules are followed, returns ____ if issue.
- ``run_model()`` - runs numerical model using Model.input_files
- ``create_input_files()`` - not sure what this will do yet
- ``read_output_files()`` - loads model output from Model.output_files to Model.outputs

.. _filer:

filer classes
-------------

InOutFile()
^^^^^^^^^^^

The base file class. 

``l-wq-m.filer.InOutFile(name='file', location='', extension='txt', description='')``

*Parameters:*

- ``name`` - file name [string]
- ``location`` - path to file excluding file name [string]
- ``extention`` - file type (e.g., txt) [string]
- ``description`` - file description [string]
 
*Attributes:*

- ``name`` - see parameter: name
- ``location`` - see parameter: location
- ``extension`` - see parameter: extension, protected
- ``description`` - see parameter: description, protected
- ``full_path`` - the full path, including file name to input file built from parameters, protected

*Methods:*

- ``update_full_path()`` - build full path based on arguments passed during intialization
- ``trim_extension()`` - remove '.' from beginning of extension if provided during initialization
- ``get_name()`` - returns InOutFile.name
- ``get_location()`` - returns inOutFile.location
- ``get_extension()`` - returns InOutFile._extension
- ``get_description()`` - returns InOutFile._description
- ``get_full_path()`` - returns InOutFile._full_path
- ``set_location(new_location)`` - sets InOutFile.location to new_location

InputFile()
^^^^^^^^^^^

Parent: l-wq-m.filer.InOutFile

``l-wq-m.filer.InputFile(name='file', location='', extension='txt', description='')``

*Parameters:*

See Parent class.

*Attributes:*

See Parent class.

*Methods:*

 - See Parent class.
 - ``create_file()`` - creates input file based on inputs in Model.inputs

OutputFile()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parent: l-wq-m.filer.InOutFile

``l-wq-m.filer.OutputFile(name='file', location='', extension='txt', description='')``

*Parameters:*

See Parent class.

*Attributes:*

See Parent class.

*Methods:*

 - See Parent class.
 - ``read_file()`` - loads information in output file into Model.outputs
 
FileContainer()
^^^^^^^^^^^^^^^
 
The base class for holding a set of input or output files
 
```l-wq-m.FileContainer()``

*Parameters:*
 
 None
 
*Attributes:*

 - ``contents`` - dictionary of InOutFile objects with keys as InOutFile.name
 - ``size`` - number of InOutFile objects in dictionary
 
*Methods:*
 
 - ``append(put)`` - add an InOutFile object (put) to container
 - ``multi_append(puts)`` - add multiple InOutFile objects from iterable (puts)
 - ``remove_by_name(put_name)`` - remove InOutFile object from container by InOutFile.name
 - ``get_all_names()`` - return list of all InOutFile.name in container

.. _in_out:

in_out classes
--------------

Input()
^^^^^^^

The base class for model inputs.

``l-wq-m.in_out.Input(name='', value=None, default=None, lower_bound=None, upper_bound=None, typical='', description='')``

*Parameters:*

 - ``name`` - input name
 - ``value`` - input value, parent class placeholder
 - ``default`` - input default value if not specified
 - ``lower_bound`` - lower bound of range of acceptable values for input
 - ``upper_bound`` - upper bound of range of acceptable values for input
 - ``typical`` - **check on if there is a difference between typical and default**
 - ``description`` - input description

*Attributes:*

 - ``name`` - see parameter: name
 - ``value`` - see parameter: value
 - ``default`` - see parameter: default
 - ``lower_bound`` - see parameter: lower_bound
 - ``upper_bound`` - see parameter: upper_bound
 - ``typical`` - **check on if there is a difference between typical and default**
 - ``description`` - see parameter: description

*Methods:*

 - ``get_name()`` - returns Input._name 
 - ``get_value()`` - returns Input.value
 - ``get_default()`` - returns Input._default
 - ``get_typical()`` - returns Input.typical
 - ``get_description()`` - returns Input.description
 - ``set_value(new_value)`` - sets Input.value to new_value
 - ``name_iter()`` - **need to research what this is supposed to do**
 - ``value_check()`` - compares Input.value to Input.lower_bound and Input.upper_bound and confirms value is appropriate for input, parent class placeholder
 
Input0D()
^^^^^^^^^

Parent: l-wq-m.in_out.Input

``Input0D(name='', value=None, default=None, lower_bound=None, upper_bound=None, typical='', description='')``
 
*Parameters:*
 
 - See Parent class
 - ``value`` - a single value of any non-iterable datatype (e.g., float, string, etc.)
 
*Attributes:*
 
See Parent class.

*Methods:*

See Parent class.

Input1D()
^^^^^^^^^
 
Parent: l-wq-m.in_out.Input

``l-wq-m.in_out.Input1D(n=0, dtype='float', name='', value=None, default=None, lower_bound=None, upper_bound=None, typical='', description='')``
 
*Parameters:*
 
 - See Parent class
 - ``n`` - length of numpy array in Input1D.value
 - ``dtype`` - datatype associated with numpy array in Input1D.value
 - ``value`` - numpy array of dimension n and datatype dtype
 
*Attributes:*
 
See Parameters.

*Methods:*

See Parent class.

Input2D()
^^^^^^^^^
 
Parent: l-wq-m.in_out.Input

``l-wq-m.in_out.Input2D(m=0, n=0, dtype='float', name='', value=None, default=None, lower_bound=None, upper_bound=None, typical='', description='')``
 
*Parameters:*
 
 - See Parent class
 - ``m`` - length of first dimension for numpy array in Input2D.value
 - ``n`` - length of second dimension for numpy array in Input2D.value
 - ``dtype`` - See Input1D.dtype
 - ``value`` - numpy array of dimension m by n and datatype dtype
 
*Attributes:*
 
See Parameters.

*Methods:*

See Parent class.

Input3D()
^^^^^^^^^
 
Parent: l-wq-m.in_out.Input

``l-wq-m.in_out.Input3D(m=0, n=0, t=0, dtype='float', name='', value=None, default=None, lower_bound=None, upper_bound=None, typical='', description='')``
 
*Parameters:*
 
 - See Parent class
 - ``m`` - length of first dimension for numpy array in Input3D.value
 - ``n`` - length of second dimension for numpy array in Input3D.value
 - ``t`` - length of third dimension for numpy array in Input3D.value
 - ``dtype`` - See Input1D.dtype
 - ``value`` - numpy array of dimension m by n by t and datatype dtype
 
*Attributes:*
 
See Parameters.

*Methods:*

See Parent class.

InputStructured()
^^^^^^^^^^^^^^^^^
 
Parent: l-wq-m.in_out.Input

``l-wq-m.in_out.InputStructured(fields, dtypes, rows=0, name='', value=None, default=None, lower_bound=None, upper_bound=None, typical='', description='')``
 
*Parameters:*
 
 - See Parent class
 - ``fields`` - list of names (as strings) for each field name to be used in a numpy structured array
 - ``dtypes`` - list of datatypes (as strings) to be used in a numpy structured array
 - ``rows`` - number of rows in a numpy structured array
 - ``dtype`` - See Input1D.dtype
 - ``value`` - numpy array of dimension m by n by t and datatype dtype
 
*Attributes:*
 
See Parameters.

*Methods:*

See Parent class.

Output()
^^^^^^^^

The base class for model outputs.

``l-wq-m.in_out.Output(name='', value=None, description='')``

*Parameters:*

 - ``name`` - output name
 - ``value`` - output value, parent class placeholder
 - ``description`` - output description

*Attributes:*

 - ``name`` - see parameter: name
 - ``value`` - see parameter: value
 - ``description`` - see parameter: description

*Methods:*

 - ``get_name()`` - returns Output._name 
 - ``get_value()`` - returns Output.value
 - ``get_description()`` - returns Output.description
 - ``set_value(new_value)`` - sets Output.value to new_value
 
Output0D()
^^^^^^^^^^
 
Parent: l-wq-m.in_out.Output

``l-wq-m.in_out.Output0D(name='', value=None, description='')``
 
*Parameters:*
 
 - See Parent class
 - ``value`` - a single value of any non-iterable datatype (e.g., float, string, etc.)
 
*Attributes:*
 
See Parameters.

*Methods:*

See Parent class.

Output1D()
^^^^^^^^^^
 
Parent: l-wq-m.in_out.Output

``l-wq-m.in_out.Output1D(n=0, dtype='float', name='', value=None, description='')``
 
*Parameters:*
 
 - See Parent class
 - ``n`` - length of numpy array in Output1D.value
 - ``value`` - a single value of any non-iterable datatype (e.g., float, string, etc.)
 - ``dtype`` - datatype associated with numpy array in Output1D.value
 - ``value`` - numpy array of dimension n and datatype dtype
 
*Attributes:*
 
See Parameters.

*Methods:*

See Parent class.

Output2D()
^^^^^^^^^^
 
Parent: l-wq-m.in_out.Output

l-wq-m.in_out.Output2D(m=0, n=0, dtype='float', name='', value=None, description='')
 
*Parameters:*
 
 - See Parent class
 - ``m`` - length of first dimension for numpy array in Output2D.value
 - ``n`` - length of second dimension for numpy array in Output2D.value
 - ``value`` - a single value of any non-iterable datatype (e.g., float, string, etc.)
 - ``dtype`` - See Output1D.dtype
 - ``value`` - numpy array of dimension m by n and datatype dtype
 
*Attributes:*
 
See Parameters.

*Methods:*

See Parent class.

Output3D()
^^^^^^^^^^
 
Parent: l-wq-m.in_out.Output

``l-wq-m.in_out.Output3D(m=0, n=0, t=0, dtype='float', name='', value=None, description='')``
 
*Parameters:*
 
 - See Parent class
 - ``m`` - length of first dimension for numpy array in Output3D.value
 - ``n`` - length of second dimension for numpy array in Output3D.value
 - ``t`` - length of third dimension for numpy array in Output3D.value
 - ``dtype`` - See Output1D.dtype
 - ``value`` - numpy array of dimension m by n by t and datatype dtype
 
*Attributes:*
 
See Parameters.

*Methods:*

See Parent class.

InOutContainer()
^^^^^^^^^^^^^^^^

The base class for holding a set of inputs or outputs. 

``l-wq-m.in_out.InOutContainer(name, description='')``

*Parameters:*

 - ``name`` - container name as a string
 - ``description`` - container description

*Attributes:*

 - ``name`` - See Parameters: name
 - ``_descriptin`` - See Parameters: description
 - ``contents`` - dictionary of Input or Output objects with keys as Input/Output.name
 - ``size`` - number of InOutFile objects in dictionary
 
*Methods:*

 - ``append(put)`` - add an input or output object (put) to container
 - ``multi_append(puts)`` - add multiple InOutFile objects from iterable (puts) 
 - ``remove_by_name(put_name)`` - remove input or output from container by Input/Output.name
 - ``get_name()`` - return name of container
 - ``get_description()`` - return description of in_out.InOutContainer
 - ``get_contents_names()`` - return names of inputs/outputs in in_out.Container
 - ``get_contents()`` - return Container.contents
 
 