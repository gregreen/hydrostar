#!/usr/bin/env bash

# HI4PI
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd ${script_dir}/../data/raw
url="https://lambda.gsfc.nasa.gov/data/foregrounds/HI4PI/NHI_HPX.fits"
echo `pwd`
wget ${url} 


# SFD
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd ${script_dir}/../data/raw
url="https://lambda.gsfc.nasa.gov/data/foregrounds/SFD/lambda_sfd_ebv.fits"
echo `pwd`
wget ${url} 

