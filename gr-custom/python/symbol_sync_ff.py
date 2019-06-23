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

class symbol_sync_ff(gr.sync_block):
    """
    Samples the input signal at the best timing by sinchronizing with the receiving signal.
    
    Arguments:
        Samples per Symbol (int): Expected number of samples per symbol.
        
        Max Samples per Symbol (int): Maximum expected number of samples per
            symbol.
        
        Sample Period (float): Inverse of sample frequency.
        
        Bandwidth (float): Bandwidth of loop filter in Hz.
        
        Damping Ratio (float): Damping factor for loop filter.
        
        Loop Gain (float): Adjustment gain for the loop filter.
        
    Returns:
        Sampled signal at the best timing.
    """
    def __init__(self, samples_per_symbol, max_samples_per_symbol, sample_period, bandwidth, damping_ratio, loop_gain):
        gr.sync_block.__init__(self,
            name="symbol_sync_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32]
        )
        self.clock_period = samples_per_symbol
        self.clock_step = 1
        self.clock_accumulator = 0
        self.max_samples_per_symbol = max_samples_per_symbol
        self.sample_buffer = []
        self.delay = 0
        ETA = (bandwidth*sample_period) / (damping_ratio + (1/(4*damping_ratio)))
        self.LOOP_FILTER_PROPORTIONAL = (4*ETA*damping_ratio) / (1 + 2*damping_ratio*ETA + ETA**2)
        self.LOOP_FILTER_INTEGRATOR = (4*ETA**2) / (1 + 2*damping_ratio*ETA + ETA**2)
        self.loop_filter_accumulator = 0


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        
        for i in range(len(in0)):
            # Delay for filling sample_buffer
            if self.delay < (self.max_samples_per_symbol-1):
                self.sample_buffer.append(in0[i])
                self.delay += 1
                out[i] = 0
            else:
                self.sample_buffer.append(in0[i])
                self.clock_accumulator += self.clock_step
                if self.clock_accumulator > self.clock_period:
                    self.clock_accumulator = 0
                    samples_per_symbol = int(self.clock_period / self.clock_step)
                    error = self.sample_buffer[-1] - self.sample_buffer[-samples_per_symbol]
                    error *= self.sample_buffer[-int(samples_per_symbol/2)]
                    out[i] = self.sample_buffer[-int(samples_per_symbol/2)]
                    self.loop_filter_accumulator += error * self.LOOP_FILTER_INTEGRATOR
                    loop_filter_result = self.loop_filter_accumulator + (error*self.LOOP_FILTER_PROPORTIONAL)
                    self.clock_step -= loop_filter_result
                else:
                    out[i] = 0
                self.sample_buffer.pop(0)

        return len(out)
