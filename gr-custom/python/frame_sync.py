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
import bitarray
from gnuradio import gr
from struct import pack

class frame_sync(gr.sync_block):
    """
    docstring for block frame_sync
    """
    def __init__(self, sync_word, threshold, bytes_message_size):
        gr.sync_block.__init__(self,
            name="frame_sync",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32]
        )
        #self.sync_word = [1,-1,1,-1, 1,-1,1,-1, 1,-1,1,-1, 1,-1,1,-1, \
        #                 -1,1,-1,1, 1,1,-1,1, 1,1,1,-1, -1,1,1,-1 -1,-1,1,-1, 1,-1,1,-1, -1,1,1,1, 1,1,1,-1]
        #sync_word = [1,0,1,0,1,0,1,0,1,0,1,0]
        self.sync_word = sync_word
        self.threshold = threshold
        self.bits_message_size = 8*bytes_message_size
        self.sync_word_size = len(self.sync_word)
        self.delay = 0
        self.correlation = 0
        self.multiplication_buffer = []
        self.message_length_string = ""
        self.message_length_int = 0
        self.message = ""

        # Clean old file
        self.file = open("message.bin", "wb")
        # Open file for writing
        self.file = open("message.bin", "ab")

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        for i in range(len(in0)):
            # Delay for filling the buffers
            if self.delay < (self.sync_word_size-1):
                self.multiplication_buffer.append(in0[i]*sync_word[i])
                self.correlation += multiplication_buffer[-1]
                out[i] = 0
                self.delay += 1
            else:
                self.multiplication_buffer.append(in0[i]*sync_word[i])
                self.correlation += multiplication_buffer[-1]

                if (!detected):
                    out[i] = 0
                    if self.correlation >= self.threshold:
                        detected = True
                else:
                    out[i] = in0[i]
                    if in0[i] < 0:
                        in0[i] = 0

                    if(len(message_length_string) < bits_message_size):
                        self.message_length_string += str(in0[i])
                        if (len(message_length_string) == bits_message_size):
                            message_length_int = int(message_length_string, 2)
                    else:
                        if(len(message) < message_length_int):
                            self.message += str(in0[i])
                        else:
                            number_bytes = len(self.messsage) % 8
                            for i in range(number_bytes):
                                self.file.write(pack('i', int(self.message[i*8: i*8+8], 2)))
                            self.file.write(pack('i', int(self.message[number_bytes:], 2)))
                            self.detected = False
                            self.message = ""
                            self.message_length_string = ""
                            self.message_length_int = 0

                self.correlation += (-1)*multiplication_buffer[0]
                self.multiplication_buffer.pop(0)


        out[:] = in0
        return len(output_items[0])

