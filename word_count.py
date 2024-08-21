from word_analys_func import get_top_type_word_in_path
from collections import Counter
from clone_git import clone_rep
import sys

dir = "clone_dir"
url = "https://github.com/qwiio13/web_python.git"


def call_get_top(type_word, top_size=200):
    words = get_top_type_word_in_path(dir, type_word=type_word)
    print(f'total {len(words)} words, {len(set(words))} unique')
    for word, occurence in Counter(words).most_common(top_size):
        print(word, occurence)


if __name__ == '__main__':

    if 'clone' in sys.argv:
        clone_rep(url, dir)

    if '-clone_from' in sys.argv:
        url = sys.argv[2]
        clone_rep(url, dir)

    if 'verbs' in sys.argv:
        call_get_top('VB')

    if 'nouns' in sys.argv:
        call_get_top('NN')

    if len(sys.argv) == 1:
        call_get_top('ALL')
