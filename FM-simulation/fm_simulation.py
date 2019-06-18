#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fm Simulation
# Generated: Tue Jun 18 15:29:41 2019
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
from fm_modulator import fm_modulator  # grc-generated hier_block
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import sip
from gnuradio import qtgui


class fm_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fm Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fm Simulation")
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

        self.settings = Qt.QSettings("GNU Radio", "fm_simulation")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.pi = pi = numpy.pi
        self.kf = kf = 30e3
        self.fs_tx = fs_tx = samp_rate*25/6
        self.gain_FM = gain_FM = 2*pi*kf / fs_tx
        self.fs_SDR = fs_SDR = samp_rate*5
        self.delta_freq = delta_freq = 1e3

        ##################################################
        # Blocks
        ##################################################
        self._delta_freq_range = Range(0, 200e3, 200, 1e3, 200)
        self._delta_freq_win = RangeWidget(self._delta_freq_range, self.set_delta_freq, "delta_freq", "counter_slider", float)
        self.top_layout.addWidget(self._delta_freq_win)
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
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=25,
                decimation=6,
                taps=(firdes.low_pass(25,1,0.5/25,0.001)),
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0_1_0 = qtgui.freq_sink_f(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Antes", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_win)
        self.fm_modulator_0 = fm_modulator(
            modulation_sensitivity=30e3,
            samp_rate=200e3,
        )
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(2048, True)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((fs_SDR/(2*pi*kf), ))
        self.blocks_delay_1 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(240e3, analog.GR_COS_WAVE, delta_freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 440, 0.25, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1e-6, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_delay_1, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.rational_resampler_xxx_0_0_0_0_1_0, 0))
        self.connect((self.fm_modulator_0, 0), (self.rational_resampler_xxx_0_0_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.fm_modulator_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0_1_0, 0), (self.audio_sink_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0_1_0, 0), (self.qtgui_freq_sink_x_0_1_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fm_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_fs_SDR(self.samp_rate*5)
        self.qtgui_freq_sink_x_0_1_0.set_frequency_range(0, self.samp_rate)
        self.set_fs_tx(self.samp_rate*25/6)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_pi(self):
        return self.pi

    def set_pi(self, pi):
        self.pi = pi
        self.set_gain_FM(2*self.pi*self.kf / self.fs_tx)
        self.blocks_multiply_const_vxx_0_0.set_k((self.fs_SDR/(2*self.pi*self.kf), ))

    def get_kf(self):
        return self.kf

    def set_kf(self, kf):
        self.kf = kf
        self.set_gain_FM(2*self.pi*self.kf / self.fs_tx)
        self.blocks_multiply_const_vxx_0_0.set_k((self.fs_SDR/(2*self.pi*self.kf), ))

    def get_fs_tx(self):
        return self.fs_tx

    def set_fs_tx(self, fs_tx):
        self.fs_tx = fs_tx
        self.set_gain_FM(2*self.pi*self.kf / self.fs_tx)

    def get_gain_FM(self):
        return self.gain_FM

    def set_gain_FM(self, gain_FM):
        self.gain_FM = gain_FM

    def get_fs_SDR(self):
        return self.fs_SDR

    def set_fs_SDR(self, fs_SDR):
        self.fs_SDR = fs_SDR
        self.blocks_multiply_const_vxx_0_0.set_k((self.fs_SDR/(2*self.pi*self.kf), ))

    def get_delta_freq(self):
        return self.delta_freq

    def set_delta_freq(self, delta_freq):
        self.delta_freq = delta_freq
        self.analog_sig_source_x_0_0.set_frequency(self.delta_freq)


def main(top_block_cls=fm_simulation, options=None):

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
