"""
Generates simulations of NHI, dust-to-gas ratios, and the stellar reddenings.


cl_sim = Sim()
cl_sim.generate()
"""

import os
import sys

import numpy as np
import healpy as hp
from astropy.io import fits

from this_project import PACKAGE_DIR
from helpers import *


class Sim:
    """Generates NHI, dust-to-gas ratios, and the stellar reddenings, based on
    - the measured NHI values
    - a realization of the dust-to-gas ratio alms
    - the stellar reddenings

    """

    def __init__(self, nside=1024):
        self.nside = nside


class SFDbased(Sim):

    _mask = None
    _nhi = None
    _ebv_emission = None
    _stellar_ebv_map = None
    _dgr = None

    def __init__(self, nside=1024):
        super().__init__(
                nside=nside,
                )

    ### Properties
    ##############
    @property
    def mask(self):
        if self._mask is None:
            self._mask = np.logical_and.reduce((
                np.isfinite(self.nhi),
                self.nhi > 0.,
                self.nhi < 2.5,
                np.isfinite(self.ebv_emission),
                self.ebv_emission > 0.,
                ))

        return self._mask

    @property
    def ebv_emission(self):
        if self._ebv_emission is None:
            self._ebv_emission = hp.read_map(
                PACKAGE_DIR.joinpath(
                    'data/raw/lambda_sfd_ebv.fits.txt').as_posix(),
                verbose=False,
            )
            self._ebv_emission = hp.ud_grade(self._ebv_emission, self.nside) 

        return self._ebv_emission

    @property
    def dgr(self):
        if self._dgr is None:
            self._dgr = self.ebv_emission / self.nhi
        
        return self._dgr

    @property
    def stellar_ebv_map(self):
        if self._stellar_ebv_map is None:
            self._stellar_ebv_map = self.dgr * self.nhi

        return self._stellar_ebv_map
 
    @property
    def nhi(self):
        if self._nhi is None:
            self._nhi = fits.getdata(
                PACKAGE_DIR.joinpath('data/raw/NHI_HPX.fits.txt').as_posix(),
                ext=1,
            )['NHI'] / 1.e20
            
            self._nhi = hp.ud_grade(self._nhi, self.nside)

        return self._nhi

    ### Methods
    ###########
    def generate(self, nstars=10000):
        lons, lats = draw_from_mask(
                nstars,
                mask_map=self.mask,
                nest=False,
                )

        
def main():
    pass

if __name__ == '__main__':
    main()
