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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from symbol_sync_gardner_ff import symbol_sync_gardner_ff
import numpy as np

class qa_symbol_sync_gardner_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        xt = np.arange(0*np.pi, 100*np.pi, 0.1)
        src_data = np.zeros(len(xt))
        for i in range(100):
            x = np.arange((i - 100)*np.pi, i*np.pi, 0.1)
            if np.random.rand() > 0.5:
                src_data += np.sinc(x)
            else:
                src_data -= np.sinc(x)
        src = blocks.vector_source_f(src_data)
        sym_sync = symbol_sync_gardner_ff(31, 50, (1/200000), 0.05, 0.707, 3.22)
        snk = blocks.vector_sink_f()
        self.tb.connect(src, sym_sync)
        self.tb.connect(sym_sync, snk)
        self.tb.run()
        result_data = snk.data()
        print result_data


if __name__ == '__main__':
    gr_unittest.run(qa_symbol_sync_gardner_ff, "qa_symbol_sync_gardner_ff.xml")
