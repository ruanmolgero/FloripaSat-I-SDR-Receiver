#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FloripaSat-I Simulation
# Author: Rafael Alevato && Ruan Lopes
# Description: Radio simulation for the FloripaSat-I CubeSat
# Generated: Thu Jun 20 11:34:14 2019
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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from simple_channel import simple_channel  # grc-generated hier_block
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
        self.samp_rate = samp_rate = 240e3
        self.modulation_sensitivity = modulation_sensitivity = 4e3

        ##################################################
        # Blocks
        ##################################################
        self.simple_channel_0 = simple_channel(
            freq_shift=1e3,
            noise_amplitude=1e-12,
            noise_seed=1,
            phase_shift=0.1,
            samp_rate=samp_rate,
        )
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	8192, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
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
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.gfsk_modulator_0 = gfsk_modulator(
            BT=0.5,
            filter_taps=100,
            modulation_sensitivity=modulation_sensitivity,
            samp_rate=samp_rate,
            samples_per_symbol=20,
        )
        self.fm_demodulator_0 = fm_demodulator(
            modulation_sensitivity=modulation_sensitivity,
            samp_rate=samp_rate,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/rpa/Downloads/Telegram Desktop/binary_random.bin', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.gfsk_modulator_0, 0))
        self.connect((self.fm_demodulator_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.gfsk_modulator_0, 0), (self.simple_channel_0, 0))
        self.connect((self.simple_channel_0, 0), (self.fm_demodulator_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fsat_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.simple_channel_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.gfsk_modulator_0.set_samp_rate(self.samp_rate)
        self.fm_demodulator_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_modulation_sensitivity(self):
        return self.modulation_sensitivity

    def set_modulation_sensitivity(self, modulation_sensitivity):
        self.modulation_sensitivity = modulation_sensitivity
        self.gfsk_modulator_0.set_modulation_sensitivity(self.modulation_sensitivity)
        self.fm_demodulator_0.set_modulation_sensitivity(self.modulation_sensitivity)


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
