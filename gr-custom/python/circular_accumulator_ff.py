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

class circular_accumulator_ff(gr.sync_block):
    """
    This blocks accumulates each sample and do a modulus with the number given. It applies the following equation: y[n] = (y[n-1] + x[n]) mod number.
    
    Arguments:
        Modulus (float): The number to apply the mod function
            (max number of the circular accumulator). Defaults to 2*pi.
    
    Returns:
        The value of each sample accumulated and with mod Modulus.
    """
    def __init__(self, modulus):
        gr.sync_block.__init__(self,
            name="circular_accumulator_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32]
        )
        self.modulus = modulus
        self.accum = 0


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        for i in range(0, len(input_items[0])):
        	self.accum += input_items[0][i]
        	self.accum = self.accum % self.modulus
        	output_items[0][i] = self.accum
        return len(output_items[0])

