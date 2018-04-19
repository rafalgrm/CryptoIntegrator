import operator

import matplotlib.pyplot as plt

TESTING_FIGURES_DICT = 'testing_figures'


def draw_distribution_file(filename, limit=100):
    counter_dict = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            word, count = line.split(':')
            counter_dict[word] = int(count)
    sorted_dic = sorted(counter_dict.items(), key=operator.itemgetter(1), reverse=True)[:limit]
    plt.plot(*list(zip(*sorted_dic)))
    plt.xticks(range(len(sorted_dic)), [item[0] for item in sorted_dic], rotation=90, fontsize=6)
    plt.savefig(TESTING_FIGURES_DICT+'/word_distribution', dpi=400)


def draw_plot_file(filename):
    y = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            y.append(int(line))
    plt.plot(y)
    plt.savefig(TESTING_FIGURES_DICT+'/word_completness', dpi=400)
