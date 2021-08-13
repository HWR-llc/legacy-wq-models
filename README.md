
# legacy-wq-models

### Introduction
legacy-wq-models is a framework for accessing water quality models (e.g., STFATE) through [Python](https://www.python.org/). 

In the field of water resources, many of the numerical models that are still in regular use by practitioners were originally developed more than 30 years ago. The models themselves are scientifically sound and useful, but many of them were developed so long ago that they no longer work on modern computers because the executable files have not been updated to work on 64-bit operating systems. Even if a professional has a functional work around (e.g., [DOSBox](https://www.dosbox.com/) or an old laptop kept in a filing cabinet), development of new user interfaces is not possible and post-processing of model results requires custom scripting to read and write model output files.

legacy-wq-models aims to eliminate these problems by accessing the uncompiled source code for a host of numerical models. Many of the model were originally written in [Fortran](https://en.wikipedia.org/wiki/Fortran#:~:text=Fortran%20%28/%CB%88f%C9%94%CB%90rt,numeric%20computation%20and%20scientific%20computing.&text=It%20is%20a%20popular%20language,rank%20the%20world%27s%20fastest%20supercomputers.). legacy-wq-models uses the Python module [f2py](https://numpy.org/doc/stable/f2py/) to compile the models in Python-accessible [C language](https://en.wikipedia.org/wiki/C_%28programming_language%29). 

Using legacy-wq-models, the newly compiled models offer three primary benefits:

 - The models will work any computer regardless of operating system,
 - new user interfaces can be developed, and
 - direct post-processing of results is simplified.

legacy-wq-models includes a set of classes and functions that simplify the inclusion of numerical models into the project, facilitate pre-processing and post-processing code development, and provide **provenance** to the model source files.

legacy-wq-models currently includes the numerical models: 

 - [STFATE](https://dots.el.erdc.dren.mil/training/2019-03-06_DredgingSeminar/03_08_2019_1400_Schroeder_Hayes_STFATE.pdf)
 - other model

### Documentation
model documentation
- [pySTFATE](C:\HWR_source\legacy-wq-models\docs\build\html\pySTFATE.html)
- model 2

[legacy-wq-models](C:\HWR_source\legacy-wq-models\docs\build\html\index.html)

legacy-wq-models  documentation

*If you want to add a new model to legacy-wq-models, develop a new user interface, or post-processing function, you should read the documentation. If you want to run an existing model, you can read the model use documentation.*

### Installation
The legacy-wq-models package is being developed using [Anaconda](https://www.anaconda.com/). Assuming you are working with Anaconda and Python 3, the legacy-wq-models package can be installed by connecting to the [repo](https://github.com/HWR-llc/legacy-wq-models.git), navigating to the directory and running `python setup.py`.  You may need to conda a few supporting packages, but I will address this prior to releasing the first complete version. 

It is important to point out that installing legacy-wq-models will not make it possible to run any of the Fortran models. Instructions/an installer for that is forthcoming...

#### Disclaimer
This code is under active development. This project includes Fortran source files that were originally developed by organizations including the United States Army Corps of Engineers ERDC. Use of the source files should not be considered endorsement by the ERDC or any other organization.  


> Written with [StackEdit](https://stackedit.io/).