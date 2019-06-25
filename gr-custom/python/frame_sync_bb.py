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
from struct import pack
from os.path import expanduser

class frame_sync_bb(gr.sync_block):
    """
    docstring for block frame_sync_bb
    """
    def __init__(self, sync_word, threshold, bytes_message_size):
        gr.sync_block.__init__(self,
            name="frame_sync_bb",
            in_sig=[numpy.int8],
            out_sig=[numpy.int8]
        )
        self.sync_word = [2*x - 1 for x in sync_word]
        self.threshold = threshold
        self.bits_message_size = 8*bytes_message_size
        self.delay = 0
        self.message_length_string = ""
        self.message_length_int = 0
        self.message = ""
        self.detected = False
        self.input_buffer = []
        self.home = expanduser("~")
        # Clean old file
        message_file = open(self.home + "/code/message.bin", "wb")
        message_file.close()

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        for i in range(len(in0)):
            self.input_buffer.append(in0[i])
            # Delay for filling the buffer
            if self.delay < (len(self.sync_word) - 1):
                out[i] = 0
                self.delay += 1
            else:
                if (not self.detected):
                    out[i] = 0
                    correlation = 0
                    sync_word_size = len(self.sync_word)
                    for j in range(sync_word_size):
                        correlation += self.sync_word[j] * self.input_buffer[j-sync_word_size]
                    if correlation >= self.threshold:
                        self.detected = True
                else:
                    out[i] = in0[i]
                    if in0[i] < 0:
                        in0[i] = 0
                    if(len(self.message_length_string) < self.bits_message_size):
                        self.message_length_string += str(int(in0[i]))
                        if (len(self.message_length_string) == self.bits_message_size):
                            self.message_length_int = int(self.message_length_string, 2)
                    else:
                        if(len(self.message) < self.message_length_int):
                            self.message += str(int(in0[i]))
                        else:
                            # Open file for writing
                            message_file = open(self.home + "/code/message.bin", "ab")
                            number_bytes = int(len(self.message) / 8)
                            for j in range(number_bytes):
                                message_file.write(pack('i', int(self.message[j*8: j*8+8], 2)))
                            if (len(self.message) % 8) > 0:
                                message_file.write(pack('i', int(self.message[number_bytes*8:], 2)))
                            message_file.close()
                            self.detected = False
                            self.message = ""
                            self.message_length_string = ""
                            self.message_length_int = 0
                self.input_buffer.pop(0)
        return len(out)

