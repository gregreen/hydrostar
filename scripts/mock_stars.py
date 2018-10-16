#!/usr/bin/env python


import numpy as np
import healpy as hp


def draw_from_mask(n, mask_map, nest=False):
    nside = hp.pixelfunc.npix2nside(mask_map.size)

    mult = 2
    n_points = 0

    lon_chunks, lat_chunks = [], []

    while n_points < n:
        # Draw points from sphere
        lon = np.random.random(n*mult) * 360.
        lat = np.degrees(np.arccos(np.random.random(n*mult)*2. - 1.)) - 90.

        # Check that points lie in mask
        pix_idx = hp.pixelfunc.ang2pix(nside, lon, lat, lonlat=True, nest=nest)
        mask_idx = mask_map[pix_idx]
        lon = lon[mask_idx]
        lat = lat[mask_idx]

        lon_chunks.append(lon)
        lat_chunks.append(lat)
        
        n_points += lon.size

    return np.hstack(lon_chunks), np.hstack(lat_chunks)


def star_cat_powerspec(n_stars, mask_map, a_lm, nest=False):
    pass
    # Draw stars from mask region

