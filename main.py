from word_analys import get_top_verbs_in_path
from collections import Counter
from clone_git import clone_rep
import sys

dir = "clone_dir"
url = "https://github.com/qwiio13/web_python.git"

if __name__ == '__main__':

    if 'clone' in sys.argv:
        clone_rep(url, dir)

    if '-clone_from' in sys.argv:
        url = sys.argv[2]
        clone_rep(url, dir)

    if 'verbs' in sys.argv:
        words = get_top_verbs_in_path(dir)
        top_size = 200
        print(f'total {len(words)} words, {len(set(words))} unique')
        for word, occurence in Counter(words).most_common(top_size):
            print(word, occurence)

    # wds = []
    # projects = [
    #     'django',
    #     'flask',
    #     'pyramid',
    #     'reddit',
    #     'requests',
    #     'sqlalchemy',
    # ]

    # for project in projects:
    #     path = os.path.join('.', project)
    #     wds += get_top_verbs_in_path(path)

    # top_size = 200
    # print(f'total {len(wds)} words, {len(set(wds))} unique')
    # for word, occurence in Counter(wds).most_common(top_size):
    #     print(word, occurence)
