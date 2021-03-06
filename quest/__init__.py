"""
The primary init for the project.
"""

from . import molecule
from . import scf_module
from . import jk
from . import solvers
from . import core
from . import mp2
from . import plots
from .mollib import mollib
from . import lj
from .molecule import Molecule
from .wavefunction import Wavefunction


# Make sure Psi4 respects the global OMP_NUM_THREADS
import psi4
import os
if "OMP_NUM_THREADS" in list(os.environ):
    psi4.set_num_threads(int(os.environ["OMP_NUM_THREADS"]))
psi4.set_output_file("psi_output.out")
