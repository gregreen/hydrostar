"""
Generates simulations of NHI, dust-to-gas ratios, and the stellar reddenings.


cl_sim = Sim()
cl_sim.generate()
"""

import os
import sys

import numpy as np
import healpy as hp

from this_project import PACKAGE_DIR


class Sim:
    """Generates NHI, dust-to-gas ratios, and the stellar reddenings, based on
    - the measured NHI values
    - a realization of the dust-to-gas ratio alms
    - the stellar reddenings

    """

    def __init__(self):
        ...


class SFDbased(Sim):

    _nhi = None

    def __init__(self):
        ...

    @property
    def mask(self):
        raise NotImplementedError()

    @property
    def ebv_sfd(self):
        ...

    @property
    def nhi(self):
        if self._nhi is None:
            self._nhi = hp.read_map(
                PACKAGE_DIR.joinpath('data/NHI_HPX.fits').as_posix()
                verbose=False,
            )

        return self._nhi

def main():
    print(P.PACKAGE_DIR)
    pass

if __name__ == '__main__':
    main()
