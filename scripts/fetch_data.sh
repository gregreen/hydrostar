#!/usr/bin/env bash

# HI4PI
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd ${script_dir}/../data
url="https://lambda.gsfc.nasa.gov/data/foregrounds/HI4PI/NHI_HPX.fits"
echo `pwd`
wget ${url} 


# SFD

