#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FloripaSat-I Simulation
# Author: Rafael Alevato && Ruan Lopes
# Description: Radio simulation for the FloripaSat-I CubeSat
# Generated: Mon Jul  8 17:51:59 2019
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
from gfsk_modulator import gfsk_modulator  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from simple_channel import simple_channel  # grc-generated hier_block
import custom
import numpy
import sip
from gnuradio import qtgui


class fsat_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FloripaSat-I Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FloripaSat-I Simulation")
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

        self.settings = Qt.QSettings("GNU Radio", "fsat_simulation")

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
        self.pi = pi = numpy.pi
        self.phase_shift = phase_shift = 0
        self.noise_amp = noise_amp = 1e-6
        self.modulation_sensitivity = modulation_sensitivity = 4e3
        self.freq_shift = freq_shift = 1e3

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
        self._phase_shift_range = Range(0, 2*pi, 0.01, 0, 200)
        self._phase_shift_win = RangeWidget(self._phase_shift_range, self.set_phase_shift, "Channel Phase Shift", "counter_slider", float)
        self.tabs_grid_layout_1.addWidget(self._phase_shift_win, 1, 0, 1, 1)
        [self.tabs_grid_layout_1.setRowStretch(r,1) for r in range(1,2)]
        [self.tabs_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self._noise_amp_range = Range(1e-6, 0.1, 1e-6, 1e-6, 200)
        self._noise_amp_win = RangeWidget(self._noise_amp_range, self.set_noise_amp, "Channel Noise Amplitude", "counter_slider", float)
        self.tabs_grid_layout_1.addWidget(self._noise_amp_win, 2, 0, 1, 1)
        [self.tabs_grid_layout_1.setRowStretch(r,1) for r in range(2,3)]
        [self.tabs_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self._freq_shift_range = Range(0, 100e3, 1e3, 1e3, 200)
        self._freq_shift_win = RangeWidget(self._freq_shift_range, self.set_freq_shift, "Channel Frequency Shift", "counter_slider", float)
        self.tabs_grid_layout_1.addWidget(self._freq_shift_win, 0, 0, 1, 1)
        [self.tabs_grid_layout_1.setRowStretch(r,1) for r in range(0,1)]
        [self.tabs_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self.simple_channel_0 = simple_channel(
            freq_shift=freq_shift,
            noise_amplitude=noise_amp,
            noise_seed=1,
            phase_shift=phase_shift,
            samp_rate=sample_rate_tx,
        )
        self.rational_resampler_xxx_0_0_0_0_1_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=5,
                taps=(firdes.low_pass(1,1,0.5/5,0.001)),
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0_0_0_0 = filter.rational_resampler_ccf(
                interpolation=6,
                decimation=5,
                taps=(firdes.low_pass(6,1,0.5/6,0.001)),
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccf(
                interpolation=25,
                decimation=6,
                taps=(firdes.low_pass(25, 1, 0.5/25, 0.001)),
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	11200, #size
        	symbol_rate*samples_per_symbol, #samp_rate
        	"Signal", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1.2, 1.2)

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

        labels = ["Received", "Received", '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
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
        self.tabs_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 3, 0, 7, 1)
        [self.tabs_grid_layout_1.setRowStretch(r,1) for r in range(3,10)]
        [self.tabs_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	280, #size
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
        self.tabs_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_0_win, 10, 0, 7, 1)
        [self.tabs_grid_layout_1.setRowStretch(r,1) for r in range(10,17)]
        [self.tabs_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	8192, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	sample_rate_rx, #bw
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
        	sample_rate_tx, #bw
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
        self.gfsk_modulator_0 = gfsk_modulator(
            BT=0.25,
            filter_taps=100,
            modulation_sensitivity=modulation_sensitivity,
            samples_per_symbol=samples_per_symbol,
            symbol_rate=1.2e3,
        )
        self.fm_demodulator_0 = fm_demodulator(
            modulation_sensitivity=modulation_sensitivity,
            samp_rate=sample_rate_rx,
        )
        self.custom_symbol_sync_gardner_fb_0 = custom.symbol_sync_gardner_fb(samples_per_symbol, 1/sample_rate, 0.01*sample_rate, 0.707, 3.22)
        self.custom_frame_sync_bb_0 = custom.frame_sync_bb(([0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0]), 32, 3)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, sample_rate,True)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/rpa/code/FloripaSat-I-SDR-Receiver/Binary-Files/fsat-hello.bin', True)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.gfsk_modulator_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.custom_frame_sync_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.custom_symbol_sync_gardner_fb_0, 0), (self.custom_frame_sync_bb_0, 0))
        self.connect((self.fm_demodulator_0, 0), (self.rational_resampler_xxx_0_0_0_0_1_0, 0))
        self.connect((self.gfsk_modulator_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.simple_channel_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0_0, 0), (self.fm_demodulator_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0_1_0, 0), (self.custom_symbol_sync_gardner_fb_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0_1_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0_1_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.simple_channel_0, 0), (self.rational_resampler_xxx_0_0_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fsat_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_sample_rate_tx(self.symbol_rate*self.samples_per_symbol*25/6)
        self.set_sample_rate(self.symbol_rate*self.samples_per_symbol)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.symbol_rate*self.samples_per_symbol)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.symbol_rate*self.samples_per_symbol)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.symbol_rate*self.samples_per_symbol)

    def get_samples_per_symbol(self):
        return self.samples_per_symbol

    def set_samples_per_symbol(self, samples_per_symbol):
        self.samples_per_symbol = samples_per_symbol
        self.set_sample_rate_tx(self.symbol_rate*self.samples_per_symbol*25/6)
        self.set_sample_rate(self.symbol_rate*self.samples_per_symbol)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.symbol_rate*self.samples_per_symbol)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.symbol_rate*self.samples_per_symbol)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.symbol_rate*self.samples_per_symbol)
        self.gfsk_modulator_0.set_samples_per_symbol(self.samples_per_symbol)

    def get_sample_rate_tx(self):
        return self.sample_rate_tx

    def set_sample_rate_tx(self, sample_rate_tx):
        self.sample_rate_tx = sample_rate_tx
        self.set_sample_rate_rx(self.sample_rate_tx*6/5)
        self.simple_channel_0.set_samp_rate(self.sample_rate_tx)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.sample_rate_tx)

    def get_sample_rate_rx(self):
        return self.sample_rate_rx

    def set_sample_rate_rx(self, sample_rate_rx):
        self.sample_rate_rx = sample_rate_rx
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.sample_rate_rx)
        self.fm_demodulator_0.set_samp_rate(self.sample_rate_rx)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.blocks_throttle_0.set_sample_rate(self.sample_rate)

    def get_pi(self):
        return self.pi

    def set_pi(self, pi):
        self.pi = pi

    def get_phase_shift(self):
        return self.phase_shift

    def set_phase_shift(self, phase_shift):
        self.phase_shift = phase_shift
        self.simple_channel_0.set_phase_shift(self.phase_shift)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.simple_channel_0.set_noise_amplitude(self.noise_amp)

    def get_modulation_sensitivity(self):
        return self.modulation_sensitivity

    def set_modulation_sensitivity(self, modulation_sensitivity):
        self.modulation_sensitivity = modulation_sensitivity
        self.gfsk_modulator_0.set_modulation_sensitivity(self.modulation_sensitivity)
        self.fm_demodulator_0.set_modulation_sensitivity(self.modulation_sensitivity)

    def get_freq_shift(self):
        return self.freq_shift

    def set_freq_shift(self, freq_shift):
        self.freq_shift = freq_shift
        self.simple_channel_0.set_freq_shift(self.freq_shift)


def main(top_block_cls=fsat_simulation, options=None):

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
