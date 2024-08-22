from word_analys_func import get_top_type_word_in_path
from clone_git import clone_rep
import sys
import json
import csv

dir = "clone_dir"
url = "https://github.com/qwiio13/web_python.git"


def write_to_file(words, stream='print', path='logs/log.txt'):
    if stream == 'print':
        print(f'total {len(words)} words, {len(set(words))} unique')
        for word, occurence in words.items():
            print(word, occurence, sep=', ')

    if stream == 'txt':
        print(f'log to txt {path}')
        with open(path, 'w') as file:
            file.write(f'total {len(words)} words, {len(set(words))} unique\n')
            for word, occurence in words.items():
                file.write(f'{word}, {occurence}\n')

    if stream == 'csv':
        path_csv = path.replace('.txt', '.csv')
        print(f'log to csv {path_csv}')
        with open(path_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Occurrence'])
            for word, occurrence in words.items():
                writer.writerow([word, occurrence])

    elif stream == 'json':
        path_json = path.replace('.txt', '.json')
        print(f'log to json {path_json}')
        data = {
            'total_words': len(words),
            'unique_words': len(set(words))
        }
        data.update(dict(words))
        with open(path_json, 'w') as file:
            json.dump(data, file, indent=4)


def call_get_top(type_word, stream, inner):
    words = get_top_type_word_in_path(dir, type_word=type_word, inner=inner)
    write_to_file(words, stream)


if __name__ == '__main__':

    if '-clone' in sys.argv:
        index = sys.argv.index('-clone')
        try:
            url = sys.argv[index + 1]
            clone_rep(url, dir)
        except IndexError:
            clone_rep(url, dir)

    if '-clone_from' in sys.argv:
        url = sys.argv[2]
        clone_rep(url, dir)

    if '-stream' in sys.argv:
        index = sys.argv.index('-stream')
        try:
            stream = sys.argv[index + 1]
        except IndexError:
            print('после флага -stream не указано значение')
    else:
        stream = 'print'

    if 'inner' in sys.argv:
        inner = True
    else:
        inner = False

    if 'vb' in sys.argv:
        call_get_top('VB', stream=stream, inner=inner)

    if 'nn' in sys.argv:
        call_get_top('NN', stream=stream, inner=inner)

    if 'all' in sys.argv:
        call_get_top('ALL', stream=stream, inner=inner)
