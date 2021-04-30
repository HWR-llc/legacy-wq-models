"""
implementation of STFATE for legacy-wq-models

original developer: 
    United States Army Corps of Engineers, Waterways Experiment Station
    Billy Johnson and Paul Schroeder  
model documentation:
    https://dots.el.erdc.dren.mil/elmodels/pdf/inlandc.pdf
description:
    Short term fate model for open water barge and hopper discharges

Notes:
 - to be written
"""
# imports
import pdb
import os
from legacy_wq_models import in_out as io
from legacy_wq_models import filer
from legacy_wq_models import model

# build out inputs
due_in_flag = io.input0D(name='DUE_IN',
                         default='DUE',
                         description="""flag indictating file type, can 
                                          either be DUE (for barge/hopper) or 
                                          IN (for a SCOW.IN file) type=string""")
itype = io.input0D(name='ITYPE',
                   default = 3,
                   typical = '1, 3',
                   description="""integer inicating type of material discharge
                                    where 1: hopper and 3: barge type=integer""")
id_ = io.input0D(name='ID',
                   description="""one line description of model run, example: 
                                    BARGE DUMP WITHOUT SPECIFIED MIXING ZONE 
                                    (TIER II W.Q.) type=string""")
nmax = io.input0D(name='NMAX',
                  upper_bound=45,
                   description="""NUMBER OF GRID POINTS IN Z DIRECTION type=integer""")
mmax = io.input0D(name='MMAX',
                  upper_bound=45,
                   description="""NUMBER OF GRID POINTS IN X DIRECTION
                                  type=integer""")
ns = io.inut0D(name='NS',
               upper_bound=4,
               description="""NUMBER OF SOLIDS type=integer""")
nlayer = io.input0D(name='NLAYER',
                    description="""NUMBER OF SMALL CONVECTING CLOUDS
                                   type=integer""")
ibins = io.input0D(name='IBINS',
                   default=0,
                   description="""NUMBER OF HOPPER BINS OPENING SIMULTANEOUSLY
                                  type=integer""")
nzsect = io.input0D(name='NZSSECT',
                   default=0,
                   description="""N-LOCATION TO LOOK AT VERTICAL CONTOUR PLOT
                                  (NOT USED) type=integer""")
nzsect = io.input0D(name='MZSSECT',
                   default=0,
                   description="""M-LOCATION TO LOOK AT VERTICAL CONTOUR PLOT
                                  (NOT USED) type=integer""")
key1 = io.input0D(name='KEY1',
                  default=1,
                  lower_bound=0,
                  upper_bound=1,
                  description="""0 USE DEFAULT COEFFICIENTS, 1 INPUT COEFFICIENTS
                                 type=integer""")
key2 = io.input0D(name='KEY2',
                  default=0,
                  lower_bound=0,
                  upper_bound=2,
                  description="""0 COMPLETE RUN
                                 1 TERMINATE COMPUTATIONS AFTER CONVECTIVE DESCENT
                                 2 TERMINATE COMPUTATIONS AFTER DYNAMIC COLLAPSE
                                 type=integer""")
key3 = io.input0D(name='KEY3',
                  default=0,
                  lower_bound=0,
                  upper_bound=7,
                  description="""0 NO LONG TERM COMPUTATIONS OF TRACER
                                 1 PERFORM TRACER LONG TERM COMPUTATIONS
                                 2 INFO ABOUT INITIAL MIXING COMPUTED BASED ON WATER
                                   QUALITY STANDARDS.  FOR 103
                                 3 INFO ABOUT INITIAL MIXING COMPUTED BASED ON PERCENT
                                   OF ORIGINAL CONC OF FLUID FRACTION.  FOR 103
                                 4 INFO ABOUT INITIAL MIXING BASED ON CONCENTRATION OF
                                   CONTAMINANT IN SEDIMENT.  FOR 103
                                 5 INFO ABOUT INITIAL MIXING COMPUTED BASED ON WATER
                                   QUALITY STANDARDS.  FOR 404
                                 6 INFO ABOUT INITIAL MIXING COMPUTED BASED ON PERCENT
                                   OF ORIGINAL CONC OF FLUID FRACTION.  FOR 404
                                 7 INFO ABOUT INITIAL MIXING BASED ON CONCENTRATION OF
                                   CONTAMINANT IN SEDIMENT.  FOR 404
                                 type=integer""")
jbfc = io.input0D(name='JBFC',
                  default=0,
                  lower_bound=0,
                  upper_bound=1,
                  description="""0 ENTRAINMENT, DRAG, AND ADDED MASS COEFFS IN CONV DESC
                                   COME FROM INPUT OR DEFAULT VALUES
                                 1 EXPRESSIONS FROM JBF TANK TESTS USED TO COMPUTE COEFFS
                                 type=integer""")
isep = io.input0D(name='ISEP',
                  default='1',
                  lower_bound=0,
                  upper_bound=1,
                  description="""1 SOLID CONCENTRATIONS WILL VARY BETWEEN LAYERS
                                 0 OTHERWISE type=integer""")
izid = io.input0D(name='IZID',
                  default=0,
                  lower_bound=0,
                  upper_bound=1,
                  description="""1 ACUTE TOXICITY CRITERIA WILL BE CONSIDERED
                                 0 OTHERWISE type=integer""")
iprit = io.input0D(name='IPRIT',
                   default=0,
                   lower_bound=0,
                   upper_bound=1,
                   description="""0 VERTICAL DIFFUSION COEFFICIENT(AKY0),EITHER
                                    INPUT OR DEFAULT VALUE
                                  1 AKY0 COMPUTED USING EXPRESSION FROM PRITCHARD
                                  type=integer""")