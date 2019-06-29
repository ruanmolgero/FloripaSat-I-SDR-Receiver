#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fsat Simulation Test
# Generated: Sat Jun 29 00:14:12 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from fm_demodulator import fm_demodulator  # grc-generated hier_block
from fm_modulator import fm_modulator  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from simple_channel import simple_channel  # grc-generated hier_block
import custom
import numpy
import sip
from gnuradio import qtgui


class fsat_simulation_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fsat Simulation Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fsat Simulation Test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fsat_simulation_test")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 1.2e3
        self.samples_per_symbol = samples_per_symbol = 40
        self.sample_rate_tx = sample_rate_tx = symbol_rate*samples_per_symbol*25/6
        self.sample_rate_rx = sample_rate_rx = sample_rate_tx*6/5
        self.sample_rate = sample_rate = symbol_rate*samples_per_symbol
        self.modulation_sensitivity = modulation_sensitivity = 4e3

        ##################################################
        # Blocks
        ##################################################
        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, 'Spectrum')
        self.tabs_widget_1 = Qt.QWidget()
        self.tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_1)
        self.tabs_grid_layout_1 = Qt.QGridLayout()
        self.tabs_layout_1.addLayout(self.tabs_grid_layout_1)
        self.tabs.addTab(self.tabs_widget_1, 'Time')
        self.top_layout.addWidget(self.tabs)
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	11518, #size
        	symbol_rate*samples_per_symbol, #samp_rate
        	"Signal", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0.disable_legend()

        labels = ["Sampled", "Received", "Transmitted", '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 0, 0, 1, 1)
        [self.tabs_grid_layout_1.setRowStretch(r,1) for r in range(0,1)]
        [self.tabs_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	900, #size
        	symbol_rate*samples_per_symbol, #samp_rate
        	"Message", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1.2, 1.2)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_0_win, 1, 0, 1, 1)
        [self.tabs_grid_layout_1.setRowStretch(r,1) for r in range(1,2)]
        [self.tabs_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	8192, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	sample_rate, #bw
        	"Received Signal", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-180, 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_0_0_win, 1, 0, 1, 1)
        [self.tabs_grid_layout_0.setRowStretch(r,1) for r in range(1,2)]
        [self.tabs_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	8192, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	sample_rate, #bw
        	"Transmitted Signal", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-180, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 0, 1, 1)
        [self.tabs_grid_layout_0.setRowStretch(r,1) for r in range(0,1)]
        [self.tabs_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	8192, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	symbol_rate*samples_per_symbol, #bw
        	"Demodulated Signal", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-180, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 2, 0, 1, 1)
        [self.tabs_grid_layout_0.setRowStretch(r,1) for r in range(2,3)]
        [self.tabs_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(1, (firdes.gaussian(1, samples_per_symbol/4, 0.25, 100)))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fm_modulator_0 = fm_modulator(
            modulation_sensitivity=modulation_sensitivity,
            samp_rate=symbol_rate*samples_per_symbol,
        )
        self.fm_demodulator_0 = fm_demodulator(
            modulation_sensitivity=modulation_sensitivity,
            samp_rate=sample_rate,
        )
        self.custom_zero_decimator_ff_0 = custom.zero_decimator_ff(60, 0.05)
        self.custom_symbol_sync_gardner_ff_0 = custom.symbol_sync_gardner_ff(samples_per_symbol, 2*samples_per_symbol, 1/sample_rate, 0.01*sample_rate, 0.707, 3.22)
        self.custom_rect_encoder_bf_0 = custom.rect_encoder_bf(samples_per_symbol)
        self.custom_frame_sync_bb_0 = custom.frame_sync_bb(([0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0]), 32, 3)
        self.custom_binary_decisor_fb_0 = custom.binary_decisor_fb()
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, sample_rate,True)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/rpa/code/FloripaSat-I-SDR-Receiver/Binary-Files/fsat-hello.bin', True)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.fm_demodulator_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.custom_rect_encoder_bf_0, 0))
        self.connect((self.custom_binary_decisor_fb_0, 0), (self.custom_frame_sync_bb_0, 0))
        self.connect((self.custom_frame_sync_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.custom_rect_encoder_bf_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.custom_symbol_sync_gardner_ff_0, 0), (self.custom_zero_decimator_ff_0, 0))
        self.connect((self.custom_symbol_sync_gardner_ff_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.custom_zero_decimator_ff_0, 0), (self.custom_binary_decisor_fb_0, 0))
        self.connect((self.fm_demodulator_0, 0), (self.custom_symbol_sync_gardner_ff_0, 0))
        self.connect((self.fm_demodulator_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.fm_demodulator_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 1))
        self.connect((self.fm_modulator_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.fm_modulator_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 2))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fsat_simulation_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_sample_rate(self.symbol_rate*self.samples_per_symbol)
        self.set_sample_rate_tx(self.symbol_rate*self.samples_per_symbol*25/6)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.symbol_rate*self.samples_per_symbol)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.symbol_rate*self.samples_per_symbol)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.symbol_rate*self.samples_per_symbol)
        self.fm_modulator_0.set_samp_rate(self.symbol_rate*self.samples_per_symbol)

    def get_samples_per_symbol(self):
        return self.samples_per_symbol

    def set_samples_per_symbol(self, samples_per_symbol):
        self.samples_per_symbol = samples_per_symbol
        self.set_sample_rate(self.symbol_rate*self.samples_per_symbol)
        self.set_sample_rate_tx(self.symbol_rate*self.samples_per_symbol*25/6)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.symbol_rate*self.samples_per_symbol)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.symbol_rate*self.samples_per_symbol)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.symbol_rate*self.samples_per_symbol)
        self.interp_fir_filter_xxx_0.set_taps((firdes.gaussian(1, self.samples_per_symbol/4, 0.25, 100)))
        self.fm_modulator_0.set_samp_rate(self.symbol_rate*self.samples_per_symbol)

    def get_sample_rate_tx(self):
        return self.sample_rate_tx

    def set_sample_rate_tx(self, sample_rate_tx):
        self.sample_rate_tx = sample_rate_tx
        self.set_sample_rate_rx(self.sample_rate_tx*6/5)

    def get_sample_rate_rx(self):
        return self.sample_rate_rx

    def set_sample_rate_rx(self, sample_rate_rx):
        self.sample_rate_rx = sample_rate_rx

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.sample_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.sample_rate)
        self.fm_demodulator_0.set_samp_rate(self.sample_rate)
        self.blocks_throttle_0.set_sample_rate(self.sample_rate)

    def get_modulation_sensitivity(self):
        return self.modulation_sensitivity

    def set_modulation_sensitivity(self, modulation_sensitivity):
        self.modulation_sensitivity = modulation_sensitivity
        self.fm_modulator_0.set_modulation_sensitivity(self.modulation_sensitivity)
        self.fm_demodulator_0.set_modulation_sensitivity(self.modulation_sensitivity)


def main(top_block_cls=fsat_simulation_test, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
