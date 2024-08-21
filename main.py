from word_analys import get_top_verbs_in_path
from collections import Counter
import os

if __name__ == '__main__':

    wds = []
    projects = [
        'django',
        'flask',
        'pyramid',
        'reddit',
        'requests',
        'sqlalchemy',
    ]

    for project in projects:
        path = os.path.join('.', project)
        wds += get_top_verbs_in_path(path)

    top_size = 200
    print(f'total {len(wds)} words, {len(set(wds))} unique')
    for word, occurence in Counter(wds).most_common(top_size):
        print(word, occurence)
