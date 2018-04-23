import operator

import matplotlib.pyplot as plt

TESTING_FIGURES_DICT = 'testing_figures'


def draw_distribution_file(filename, limit=100):
    counter_dict = {}
    with open(filename, 'r', encoding='windows-1252') as f:
        for line in f.readlines():
            if len(line.split(':')) == 2:
                word, count = line.split(':')
            counter_dict[word] = int(count)
    sorted_dic = sorted(counter_dict.items(), key=operator.itemgetter(1), reverse=True)[:limit]
    plt.plot(*list(zip(*sorted_dic)))
    plt.title('Most popular words distribution: top {}'.format(limit))
    plt.ylabel('Number of occurences')
    plt.xticks(range(len(sorted_dic)), [item[0] for item in sorted_dic], rotation=90, fontsize=6)
    plt.xlabel('Words')
    plt.savefig(TESTING_FIGURES_DICT+'/word_distribution', dpi=400)
    plt.clf()


def draw_plot_file(filename):
    y = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            y.append(int(line))
    fig = plt.figure(1)
    plot = fig.add_subplot(111)
    plt.plot(y)
    plt.title('Distinct words vs Number of tweets processed')
    plt.xlabel('Tweets processed', fontsize=7)
    plt.ylabel('Distinct words', fontsize=7)
    plot.tick_params(labelsize=8)
    plt.savefig(TESTING_FIGURES_DICT+'/word_completness', dpi=400)
    plt.clf()
