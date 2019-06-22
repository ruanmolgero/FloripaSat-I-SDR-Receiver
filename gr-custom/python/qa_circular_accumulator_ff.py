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
from circular_accumulator_ff import circular_accumulator_ff

class qa_circular_accumulator_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        src_data = (0, 0.001, 0.002, 0.004, 0.006, 0.010, 0.1, 10.25, 2.1)
        expected_result = (0, 0.001, 0.003, 0.007, 0.013, 0.023, 0.123, 1.373, 0.473)
        src = blocks.vector_source_f(src_data)
        acc = circular_accumulator_ff(3)
        snk = blocks.vector_sink_f()
        self.tb.connect(src, acc)
        self.tb.connect(acc, snk)
        self.tb.run()
        result_data = snk.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 5)


if __name__ == '__main__':
    gr_unittest.run(qa_circular_accumulator_ff, "qa_circular_accumulator_ff.xml")
