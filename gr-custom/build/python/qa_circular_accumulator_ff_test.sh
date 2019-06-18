#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/rpa/code/FloripaSat-I-SDR-Receiver/gr-custom/python
export PATH=/home/rpa/code/FloripaSat-I-SDR-Receiver/gr-custom/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/rpa/code/FloripaSat-I-SDR-Receiver/gr-custom/build/swig:$PYTHONPATH
/usr/bin/python2 /home/rpa/code/FloripaSat-I-SDR-Receiver/gr-custom/python/qa_circular_accumulator_ff.py 
