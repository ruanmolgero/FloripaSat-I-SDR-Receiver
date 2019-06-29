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

class symbol_sync_early_late_ff(gr.sync_block):
    """
    Samples the input signal at the best timing by sinchronizing with the receiving signal. It uses Early-Late TED method for synchronization. More about Early-Late method at https://www.nutaq.com/blog/symbol-timing-recovery-methods-digital-iq-demodulator.
    
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
            name="symbol_sync_early_late_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32]
        )
        self.samples_per_symbol = samples_per_symbol
        self.clock_step = 1
        self.clock_accumulator = 0
        self.max_samples_per_symbol = max_samples_per_symbol
        self.sample_buffer = []
        self.delay = 0
        ETA = 1 / (damping_ratio + (1/(4*damping_ratio)))
        self.LOOP_FILTER_PROPORTIONAL = loop_gain*(4*damping_ratio/ETA)*(bandwidth*sample_period)
        self.LOOP_FILTER_INTEGRATOR = loop_gain*(4/(ETA)**2)*(bandwidth*sample_period)**2
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
                if self.clock_accumulator >= self.samples_per_symbol:
                    # Gardner Method
                    self.clock_accumulator %= self.samples_per_symbol
                    error = self.sample_buffer[-int(self.samples_per_symbol/2) - 1] - self.sample_buffer[-int(3*self.samples_per_symbol/2) - 1]
                    error *= self.sample_buffer[-self.samples_per_symbol - 1]
                    error *= -1
                    out[i] = self.sample_buffer[-self.samples_per_symbol - 1]
                    self.loop_filter_accumulator += error * self.LOOP_FILTER_INTEGRATOR
                    self.clock_step = 1 + self.loop_filter_accumulator + (error*self.LOOP_FILTER_PROPORTIONAL)

                    # Add warning to clock step too low or too high
                    if self.clock_step < 0.65:
                        self.clock_step = 0.65
                        self.loop_filter_accumulator = 0
                        print "Clock Step Too Low!!!"
                    elif self.clock_step > 1.6:
                        self.clock_step = 1.6
                        self.loop_filter_accumulator = 0
                        print "Clock Step Too High!!!"
                    # # Print clock_step for filter configuration
                    # print self.clock_step
                else:
                    out[i] = 0
                self.sample_buffer.pop(0)

        return len(out)