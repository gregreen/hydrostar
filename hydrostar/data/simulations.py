"""
Generates simulations of NHI, dust-to-gas ratios, and the stellar reddenings.


cl_sim = ..
cl_sim.generate()
>> realization
"""

import os
import sys
from pathlib import Path

import numpy as np
import healpy as hp

from .


class Sim:
    def __init__(self):
        ...


class SFDbased(Sim):

    def __init__(self):
        ...

    @property
    def mask(self):
        ...

    @property
    def ebv_sfd(self):
        ...

    @property
    def nhi(self):
        ...

def main():
    pass

if __name__ == '__main__':
    main()