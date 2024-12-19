#!/bin/bash
# file name: busy.sh

eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/setup.sh` 
/data/condor_shared/users/blaufuss/umd_computing_examples/condor/simple_example/busy.py $1
