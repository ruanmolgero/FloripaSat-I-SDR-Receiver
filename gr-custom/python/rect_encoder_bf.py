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

class rect_encoder_bf(gr.interp_block):
    """
    docstring for block rect_encoder_bf
    """
    def __init__(self, samples_per_symbol):
        gr.interp_block.__init__(self,
            name="rect_encoder_bf",
            in_sig=[numpy.int8],
            out_sig=[numpy.float32],
            interp = samples_per_symbol
        )
        self.samples_per_symbol = samples_per_symbol


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        for i in range(len(in0)):
            for j in range(self.samples_per_symbol):
                out[i*self.samples_per_symbol + j] = in0[i]*2 - 1
        return len(output_items[0])

