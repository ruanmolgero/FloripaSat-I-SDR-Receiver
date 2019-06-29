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
from binary_decisor_fb import binary_decisor_fb

class qa_binary_decisor_fb (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        src_data = (0, 0.001, 0.002, 0.5, -0.001, -20, 100, 1, -1)
        expected_result = (1, 1, 1, 1, -1, -1, 1, 1, -1)
        src = blocks.vector_source_f(src_data)
        bin_dec = binary_decisor_fb()
        snk = blocks.vector_sink_b()
        self.tb.connect(src, bin_dec)
        self.tb.connect(bin_dec, snk)
        self.tb.run()
        result_data = tuple([int((256-x)*-1) if x > 127 else int(x) for x in snk.data()])
        if result_data != expected_result:
            print "Error! Result != Expected Result"


if __name__ == '__main__':
    gr_unittest.run(qa_binary_decisor_fb, "qa_binary_decisor_fb.xml")
