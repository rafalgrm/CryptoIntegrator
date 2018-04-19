from unittest import TestCase

from tools.visualizer import draw_distribution_file, draw_plot_file


class TestVisualizer(TestCase):

    def test_distribution_plot(self):
        draw_distribution_file('word_frequencies_v1.rxt')

    def test_line_plot(self):
        draw_plot_file('word_completness.txt')
