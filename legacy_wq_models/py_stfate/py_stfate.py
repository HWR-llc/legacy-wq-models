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

# STFATE specific inputs
due_in_flag = io.Input0D(name='DUE_IN',
                         default='DUE',
                         description="""flag indictating file type, can 
                                          either be DUE (for barge/hopper) or 
                                          IN (for a SCOW.IN file) type=string""")
itype = io.Input0D(name='ITYPE',
                   default = 3,
                   typical = '1, 3',
                   description="""integer inicating type of material discharge
                                    where 1: hopper and 3: barge type=integer""")
id_ = io.Input0D(name='ID',
                   description="""one line description of model run, example: 
                                    BARGE DUMP WITHOUT SPECIFIED MIXING ZONE 
                                    (TIER II W.Q.) type=string""")
nmax = io.Input0D(name='NMAX',
                  upper_bound=45,
                   description="""NUMBER OF GRID POINTS IN Z DIRECTION type=integer""")
mmax = io.Input0D(name='MMAX',
                  upper_bound=45,
                   description="""NUMBER OF GRID POINTS IN X DIRECTION
                                  type=integer""")
ns = io.Input0D(name='NS',
               upper_bound=4,
               description="""NUMBER OF SOLIDS type=integer""")
nlayer = io.Input0D(name='NLAYER',
                    description="""NUMBER OF SMALL CONVECTING CLOUDS
                                   type=integer""")
ibins = io.Input0D(name='IBINS',
                   default=0,
                   description="""NUMBER OF HOPPER BINS OPENING SIMULTANEOUSLY
                                  type=integer""")
nzsect = io.Input0D(name='NZSECT',
                   default=0,
                   description="""N-LOCATION TO LOOK AT VERTICAL CONTOUR PLOT
                                  (NOT USED) type=integer""")
mzsect = io.Input0D(name='MZSECT',
                   default=0,
                   description="""M-LOCATION TO LOOK AT VERTICAL CONTOUR PLOT
                                  (NOT USED) type=integer""")
key1 = io.Input0D(name='KEY1',
                  default=1,
                  lower_bound=0,
                  upper_bound=1,
                  description="""0 USE DEFAULT COEFFICIENTS, 1 INPUT COEFFICIENTS
                                 type=integer""")
key2 = io.Input0D(name='KEY2',
                  default=0,
                  lower_bound=0,
                  upper_bound=2,
                  description="""0 COMPLETE RUN
                                 1 TERMINATE COMPUTATIONS AFTER CONVECTIVE DESCENT
                                 2 TERMINATE COMPUTATIONS AFTER DYNAMIC COLLAPSE
                                 type=integer""")
key3 = io.Input0D(name='KEY3',
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
jbfc = io.Input0D(name='JBFC',
                  default=0,
                  lower_bound=0,
                  upper_bound=1,
                  description="""0 ENTRAINMENT, DRAG, AND ADDED MASS COEFFS IN CONV DESC
                                   COME FROM INPUT OR DEFAULT VALUES
                                 1 EXPRESSIONS FROM JBF TANK TESTS USED TO COMPUTE COEFFS
                                 type=integer""")
isep = io.Input0D(name='ISEP',
                  default='1',
                  lower_bound=0,
                  upper_bound=1,
                  description="""1 SOLID CONCENTRATIONS WILL VARY BETWEEN LAYERS
                                 0 OTHERWISE type=integer""")
izid = io.Input0D(name='IZID',
                  default=0,
                  lower_bound=0,
                  upper_bound=1,
                  description="""1 ACUTE TOXICITY CRITERIA WILL BE CONSIDERED
                                 0 OTHERWISE type=integer""")
iprit = io.Input0D(name='IPRIT',
                   default=0,
                   lower_bound=0,
                   upper_bound=1,
                   description="""0 VERTICAL DIFFUSION COEFFICIENT(AKY0),EITHER
                                    INPUT OR DEFAULT VALUE
                                  1 AKY0 COMPUTED USING EXPRESSION FROM PRITCHARD
                                  type=integer""")
mds1 = io.Input0D(name='MDS1',
                  description="""DISPOSAL SITE BOUNDARIES
                                 BEGINNING M INDEX type=integer""")
mds2 = io.Input0D(name='MDS2',
                  description="""DISPOSAL SITE BOUNDARIES
                                 LAST M INDEX type=integer""")
nds1 = io.Input0D(name='NDS1',
                  description="""DISPOSAL SITE BOUNDARIES
                                 BEGINNING N INDEX type=integer""")
nds2 = io.Input0D(name='NDS2',
                  description="""DISPOSAL SITE BOUNDARIES
                                 LAST N INDEX type=integer""")
xmds1 = io.Input0D(name='XMDS1',
                  description="""type=float""")
xmds2 = io.Input0D(name='XMDS2',
                  description="""type=float""")
xnds1 = io.Input0D(name='XNDS1',
                  description="""type=float""")
xnds2 = io.Input0D(name='XNDS2',
                  description="""type=float""")
mzd1 = io.Input0D(name='MZD1',
                  description="""ZONE OF INITIAL DILUTION BOUNDARIES [FOR ACUTE TOX]
                                 BEGINNING M INDEX type=integer""")
mzd2 = io.Input0D(name='MZD2',
                  description="""ZONE OF INITIAL DILUTION BOUNDARIES [FOR ACUTE TOX]
                                 LAST M INDEX type=integer""")
nzd1 = io.Input0D(name='NZD1',
                  description="""ZONE OF INITIAL DILUTION BOUNDARIES [FOR ACUTE TOX]
                                 BEGINNING N INDEX type=integer""")
nzd2 = io.Input0D(name='NZD2',
                  description="""ZONE OF INITIAL DILUTION BOUNDARIES [FOR ACUTE TOX]
                                 LAST N INDEX type=integer""")
ipcn = io.Input0D(name='IPCN',
                  default=1,
                  lower_bound=0,
                  upper_bound=1,
                  description="""1 CONVECTIVE DESCENT RESULTS ARE PRINTED, 0 IF NOT
                                 type=integer""")
ipcl = io.Input0D(name='IPCL',
                  default=1,
                  lower_bound=0,
                  upper_bound=1,
                  description="""1 COLLAPSE RESULTS ARE PRINTED, 0 IF NOT,
                                 type=integer""")
iplt = io.Input0D(name='IPLT',
                  default=1,
                  lower_bound=0,
                  upper_bound=1,
                  description="""0 LONG TERM COMPUTATIONS ARE PRINTED AT 1/4,
                                 1/2, 3/4, 1 OF TOTAL SIMULATION TIME
                                 type=integer""")
n = io.Input0D(name='N',
               default=0,
               description="""USER WILL REQUEST LONG TERM PRINT AT N TIMES
                              type=integer""")
nverts = io.Input0D(name='NVERTS',
                    description="""NUMBER OF VERTICAL POSITIONS WHERE CONCS
                                   DESIRED type=integer""")
ypos = io.Input1D(name='YPOS',
                  description="""VERTICAL POSITION IN FEET WHERE OUTPUT IS DESIRED
                                 type=1-D numpy array""")
depc = io.Input0D(name='DEPC',
                  description="""CONSTANT WATER DEPTH (FT) RELATIVE TO DATUM
                                 type=float""")
dx = io.Input0D(name='DX',
                description="""SPATIAL STEP OF GRID (FT) FROM TOP TO BOTTOM
                               type=float""")
dz = io.Input0D(name='DZ',
                description="""SPATIAL STEP OF GRID (FT) FROM LEFT TO RIGHT
                               type=float""")
idep = io.Input0D(name='IDEP',
                  lower_bound=0,
                  upper_bound=1,
                  description="""0 INPUT ACTUAL WATER DEPTHS
                                 1 CONSTANT WATER DEPTH type=integer""")
depth = io.Input2D(name='DEPTH',
                   description="""WATER DEPTH (FT) RELATIVE TO DATUM
                                  DEPTH(N,M) type=2-D numpy array""")
xbarge = io.Input0D(name='XBARGE',
                    description="""LOCATION OF BARGE (FT) FROM TOP OF THE GRID
                                   type=float""")
zbarge = io.Input0D(name='ZBARGE',
                    description="""LOCATION OF BARGE (FT) FROM LEFT SIDE OF THE GRID
                                   type=float""")
slopex = io.Input0D(name='SLOPEX',
                    description="""AVG. SLOPE (DEG) IN THE X DIRECTION AT THE
                                   DISPOSAL SITE type=float""")
slopey = io.Input0D(name='SLOPEY',
                    description="""AVG. SLOPE (DEG) IN THE Y DIRECTION AT THE
                                   DISPOSAL SITE type=float""")
xhole = io.Input0D(name='XHOLE',
                   description="""X DIMENSION (FT) OF BOTTOM DISPOSAL HOLE
                                  type=float""")
zhole = io.Input0D(name='ZHOLE',
                   description="""Z DIMENSION (FT) OF BOTTOM DISPOSAL HOLE
                                  type=float""")
dhole = io.Input0D(name='DHOLE',
                   description="""DEPTH (FT) OF THE BOTTOM DISPOSAL HOLE
                                  type=float""")
z0 = io.Input0D(name='Z0',
                description="""HEIGHT OF BOTTOM ROUGHNESS FT. type=float""")
nroa = io.Input0D(name='NROA',
                  description="""NUMBER OF POINTS IN VERTICAL DENSITY PROFILE 
                                 type=integer """)
y = io.Input1D(name='Y',
               description="""VERTICAL DISTANCE FROM FREE SURFACE (FT)
                              Y(NROA) type=1-D numpy array""")
roa = io.Input1D(name='ROA',
                 description="""AMBIENT WATER DENSITY (GM/CC)
                                ROA(NROA) type=1-D numpy array""")
iform = io.Input0D(name='IFORM',
                   lower_bound=1,
                   upper_bound=4,
                   description="""1 DEPTH AVERAGED VELOCITIES CONSTRUCTED FROM
                                    SINGLE OBSERVATION - TIME INVARIANT
                                  2 DEPTH AVERAGED VELOCITIES CONSTRUCTED FROM
                                    SINGLE OBSERVATION - LOG DISTRIBUTION APPLIED
                                    - TIME INVARIANT
                                  3 CONSTANT DEPTH AND TIME INVARIANT VELOCITY
                                    PROFILE
                                  4 DEPTH AVERAGED VELOCITIES READ IN - TIME INVARIANT
                                  type=integer""")
du1 = io.Input0D(name='DU1',
                 description="""DEPTH FROM FREE SURFACE OF FIRST X VELOCITY 
                                POINT (FT) type=float""")
du2 = io.Input0D(name='DU2',
                 description="""DEPTH FROM FREE SURFACE OF SECOND X VELOCITY 
                                POINT (FT) type=float""")
uu1 = io.Input0D(name='UU1',
                 description="""X VELOCITY AT DU1 (FT/SEC) type=float""")
uu2 = io.Input0D(name='UU2',
                 description="""X VELOCITY AT DU2 (FT/SEC) type=float""")
dw1 = io.Input0D(name='DW1',
                 description="""DEPTH FROM FREE SURFACE OF FIRST Z VELOCITY
                                POINT (FT) type=float""")
dw2 = io.Input0D(name='DW2',
                 description="""DEPTH FROM FREE SURFACE OF SECOND Z VELOCITY
                                POINT (FT) type=float""")
ww1 = io.Input0D(name='WW1',
                 description="""Z VELOCITY AT DW1 (FT/SEC) type=float""")
ww2 = io.Input0D(name='WW2',
                 description="""Z VELOCITY AT DW2 (FT/SEC) type=float""")
vax = io.Input0D(name='VAX',
                 description="""VERTICAL AVERAGED VELOCITY IN X-DIRECTION
                                type=float""")
vaz = io.Input0D(name='VAZ',
                 description="""VERTICAL AVERAGED VELOCITY IN Z-DIRECTION
                                type=float""")
d = io.Input0D(name='D',
               description="""DEPTH AT LOCATION OF VELOCITY MEASURMENT
                              type=float""")
tstop = io.Input0D(name='TSTOP',
                   description="""TIME (SEC) OF THE SIMULATION. IF KEY3=2,3,4,
                                  SET TO 14400. IF KEY3=5,6,7 AND EITHER A 
                                  DISPOSAL SITE OR A ZONE OF INITIAL DILUTION
                                  HAVE BEEN SPECIFIED, SET TO 3600 OR GREATER.
                                  MAKE SURE TSTOP IS SOME MULTIPLE OF DTL.
                                  type=integer""")
dtl = io.Input0D(name='DTL',
                 description="""LONG TERM TIME STEP (SEC)..(X-VEL*DTL .LE. DX)
                                (Z-VEL*DTL .LE. DZ) type=integer""")
bargl = io.Input0D(name='BARGL',
                   description="""LENGTH OF BARGE (FT) type=float""")
bargw = io.Input0D(name='BARGW',
                   description="""WIDTH OF BARGE (FT) type=float""")
drel1 = io.Input0D(name='DREL1',
                   description="""LOADED DRAFT OF THE BARGE (FT) type=float""")
drel2 = io.Input0D(name='DREL2',
                   description="""UNLOADED DRAFT OF THE BARGE (FT) type=float""")
fden = io.Input0D(name='FDEN',
                  description="""DENSITY OF WATER AT DREDGING SITE type=float""")
alpha0 = io.Input0D(name='ALPHA0',
                    default=0.235,
                    description="""CONV DESCENT ENTRAINMENT COEFF..(0.235)
                                   type=float""")
beta = io.Input0D(name='BETA',
                  default=0.000,
                  description="""SETTLING COEFF..(0.0) type=float""")
cm = io.Input0D(name='CM',
                default=1.0,
                description="""APPARENT MASS COEFF..(1.0) type=float""")
cd = io.Input0D(name='CD',
                default=.5,
                description="""DRAG COEFF FOR A SPHERE..(0.50) type=float""")
gama = io.Input0D(name='GAMA',
                  default=0.25,
                  description="""RATIO OF CLOUD DEN GRAD TO AMBIENT 
                                 DEN GRAD..(0.25) type=float""")
cdrag = io.Input0D(name='CDRAG',
                   default=1.0,
                   description="""FORM DRAG COEFF FOR OBLATE SPHEROID..
                                  (1.0) type=float""")
cfric = io.Input0D(name='CFRIC',
                   default=0.01,
                   description="""SKIN FRICTION FOR OBLATE SPHEROID..(0.01)
                                  type=float""")
cd3 = io.Input0D(name='CD3',
                 default=0.10,
                 description="""DRAG COEFF FOR ELLIPSOIDAL WEDGE..(0.10)
                                type=float""")
cd4 = io.Input0D(name='CD4',
                 default=1.0,
                 description="""RAG COEFF FOR A PLATE..(1.0) type=float""")
alphac = io.Input0D(name='ALPHAC',
                    default=0.100,
                    description="""ENTRAINMENT COEFF IN COLLAPSE PHASE..(0.100)
                                   type=float""")
frictn = io.Input0D(name='FRICTN',
                    default=0.01,
                    description="""BOTTOM FRICTION COEFF..(0.01) type=float""")
alamda = io.Input0D(name='ALAMDA',
                    default=0.001,
                    description="""DISSIPATION PARAMETER IN HORIZ DIFFUSION ..
                                   (0.001) type=float""")
aky0 = io.Input0D(name='AKY0',
                  default=0.025,
                  description="""VERTICAL DIFFUSION COEFF FOR UNSTRATIFIED 
                                 CASE..(0.025) type=float""")
cstrip = io.Input0D(name='CSTRIP',
                    description="""COEFIEIENT CONTROLLING STRIPPING OF FINES
                                   DURING CONVECTIVE DESCENT type=float""")
cu = io.Input0D(name='CU',
                description="""X VELOCITY OF THE BARGE (FT/SEC) type=float
                               note: identified as CU(1) in DIFID, may be
                               1-D array""")
cw = io.Input0D(name='CW',
                description="""Z VELOCITY OF THE BARGE (FT/SEC) type=float
                               note: identified as CW(1) in DIFID, may be
                               1-D array""")
volm = io.Input1D(name='VOLM',
                  description="""VOLUME OF MATERIAL IN THE CONVECTING CLOUD
                                 (CU YD) type=1-d numpy array""")
amll = io.Input0D(name='AMLL',
                  description="""MULTIPLE OF THE LIQUID LIMIT OF MATERIAL
                                 - ONLY USED IF JBFC = 1 type=float""")
param = io.InOutContainer(name='PARAM',
                          description="""includes multiple inputs that are 
                                         grouped together:
                                         PARAM = IDENTIFIER OF THE SEDIMENT FRACTION
                                                 type=string
                                         ROAS = DENSITY OF THIS FRACTION (GM/CC)
                                                type=float
                                         CS = CONCENTRATION OF THIS SEDIMENT
                                              FRACTION (VOL/VOL) type=float
                                         VFALL = PARTICLE FALL VELOCITY (FT/SEC)
                                                 type=float
                                         VOIDS = VOIDS RATIO OF THIS SEDIMENT FRACTION.
                                                 USED TO COMPUTE DEPTH OF BOTTOM DEPOSITION
                                                 type=float
                                         TAUCR = CRITICAL SHEAR STRESS FOR DEPOSITION.
                                                 TYPICAL VALUES
                                                 CLAY = .0006 - .0003  SILT  = .003 - .02
                                                 SAND = .02   - .30  (POUNDS FORCE/SQ. FT.)
                                                 type=float
                                         ICOHES = 0 SEDIMENT FRACTION SETTLES WITH
                                                    PARTICLE VELOCITY
                                                  1 SEDIMENT IS COHESIVE AND FALL
                                                    VELOCITY IS COMPUTED
                                                  type=integer (0 or 1)
                                         IMIX = 0 SEDIMENT FRACTION SETTLES WITH
                                                  PARTICLE VELOCITY
                                                1 SEDIMENT IS COHESIVE AND FALL
                                                  VELOCITY IS COMPUTED
                                                type=integer (0 or 1)
                                         ISTRIP = 1 SEDIMENT FRACTION CAN BE 
                                                    STRIPPED AWAY DURING CONVECTIVE DESCENT
                                                  0 NO STRIPPING
                                                  type=integer (0 or 1)
                                        type=numpy structured array""")
param_1 = io.InputStructured(['PARAM', 'ROAS', 'CS', 'VFALL', 'VOIDS', 'TAUCR', 'ICOHES', 'IMIX', 'ISTRIP'],
                             ['<U10', 'float', 'float','float', 'float', 'float', 'int',   'int',  'int'],
                             name='1',
                             description='see container')
param.append(param_1)
paramtr = io.Input1D(name='PARAMTR',
                     description="""IDENTIFIER OF CONSERVATIVE TRACER
                                    type=1-D numpy array (string)""")
cinit = io.Input0D(name='CINIT',
                   description="""CONCENTRATION OF THE TRACER IN THE BARGE (MG/L)
                                  type=float""")
cback = io.Input1D(name='CBACK',
                   description="""AMBIENT BACKGROUND CONC OF THE TRACER (MG/L)
                                  IF KEY3=3 OR 6 PROGRAM WILL SET CINIT AND CBACK =0.0
                                  type=1-D numpy array (float)""")
tprt = io.Input1D(name='TPRT',
                  description="""TIME (SEC) IN THE SIMULATION WHEN LONG TERM RESULTS
                                 ARE TO BE PRINTED type=1-D numpy array (integer)""")
                                 
# list of all model inputs
all_inputs = [due_in_flag, itype, id_, nmax, mmax, ns, nlayer, ibins, nzsect,
              mzsect, key1, key2, key3, jbfc, isep, izid, iprit, mds1, mds2, 
              nds1, nds2, xmds1, xmds2, xnds1, xnds2, mzd1, mzd2, nzd1, nzd2,
              ipcn, ipcl, iplt, n, nverts, ypos, depc, dx, dz, idep, depth,
              xbarge, zbarge, slopex, slopey, xhole, zhole, dhole, z0, nroa,
              y, roa, iform, du1, du2, uu1, uu2, dw1, dw2, ww1, ww2, vax, vaz,
              d, tstop, dtl, bargl, bargw, drel1, drel2, fden, alpha0, beta,
              cm, cd, gama, cdrag, cfric, cd3, cd4, alphac, frictn, alamda, aky0,
              cstrip, cu, cw, volm, amll, param, paramtr, cinit, cback, tprt]

# STFATE model class
class PySTFATE(model.Model):
    """
    implementation of model class for the STFATE dredging disposal model...
    
    """
    def __init__(self):
        super(PySTFATE, self).__init__(name='STFATE',
                                   description="""Short Term Fate of Dredged
                                                  Material in Open Water Model""")
        self.inputs.multi_append(all_inputs)