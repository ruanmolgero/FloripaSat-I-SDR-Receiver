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

class symbol_sync_gardner_new_fb(gr.basic_block):
    """
    docstring for block symbol_sync_gardner_new_fb
    """
    def __init__(self, samples_per_symbol, sample_period, bandwidth, damping_ratio, loop_gain):
        gr.basic_block.__init__(self,
            name="symbol_sync_gardner_new_fb",
            in_sig=[numpy.float32],
            out_sig=[numpy.int8]
        )
        self.samples_per_symbol = samples_per_symbol
        self.clock_step = 1
        self.clock_accumulator = 0
        self.max_samples_per_symbol = int(1.5 * samples_per_symbol)
        self.sample_buffer = []
        self.delay = 0
        ETA = 1 / (damping_ratio + (1/(4*damping_ratio)))
        self.LOOP_FILTER_PROPORTIONAL = loop_gain*(4*damping_ratio/ETA)*(bandwidth*sample_period)
        self.LOOP_FILTER_INTEGRATOR = loop_gain*(4/(ETA)**2)*(bandwidth*sample_period)**2
        self.loop_filter_accumulator = 0

    def forecast(self, noutput_items, ninput_items_required):
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = self.max_samples_per_symbol * noutput_items

    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        number_outputs = 0
        
        for number_inputs in range(len(in0)):
            # Delay for filling sample_buffer
            if self.delay < (self.max_samples_per_symbol-1):
                self.sample_buffer.append(in0[number_inputs])
                self.delay += 1
            else:
                self.sample_buffer.append(in0[number_inputs])
                self.clock_accumulator += self.clock_step
                if self.clock_accumulator >= self.samples_per_symbol:
                    # Gardner Method
                    self.clock_accumulator %= self.samples_per_symbol
                    error = self.sample_buffer[-1] - self.sample_buffer[-self.samples_per_symbol - 1]
                    error *= self.sample_buffer[-int(self.samples_per_symbol/2) - 1]
                    self.loop_filter_accumulator += error * self.LOOP_FILTER_INTEGRATOR
                    self.clock_step = 1 + self.loop_filter_accumulator + (error*self.LOOP_FILTER_PROPORTIONAL)
                    # Add warning to clock step too low or too high
                    if self.clock_step < 0.7:
                        self.clock_step = 0.7
                        self.loop_filter_accumulator = 0
                        print "Clock Step Too Low!!!"
                    elif self.clock_step > 1.3:
                        self.clock_step = 1.3
                        self.loop_filter_accumulator = 0
                        print "Clock Step Too High!!!"
                    # Binary Decisor
                    if (self.sample_buffer[-1] > 0):
                        out[number_outputs] = 1
                    else:
                        out[number_outputs] = -1
                    number_outputs += 1
                    if number_outputs >= len(out):
                        break;
                self.sample_buffer.pop(0)

        self.consume_each(number_inputs+1)
        return len(out)
