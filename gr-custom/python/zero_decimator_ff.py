#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class zero_decimator_ff(gr.basic_block):
    """
    Decimate all zeros in a signal based on a threshold.
    
    Arguments:
        Zeros Max Interval (int): The maximum number of consecutive zeros between two
            numbers that aren't zeroes.

        Zero Threshold (float): The number which defines what is a zero.
            Any input that has an absolute value below this number, is a zero.
        
    Returns:
        A sequence of all non-zero input values.
    """
    def __init__(self, zeros_max_interval, zero_threshold):
        gr.basic_block.__init__(self,
            name="zero_decimator_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32]
        )
        self.zeros_max_interval = zeros_max_interval
        self.zero_threshold = zero_threshold

    def forecast(self, noutput_items, ninput_items_required):
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = self.zeros_max_interval*noutput_items

    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        number_outputs = 0

        for number_inputs in range(len(in0)):
            if abs(in0[number_inputs]) > self.zero_threshold:
                out[number_outputs] = in0[number_inputs]
                number_outputs += 1
                if number_outputs >= len(out):
                    break;

        self.consume_each(number_inputs+1)
        return len(out)
