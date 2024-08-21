import ast
import os
from collections import Counter
from itertools import chain

from nltk import pos_tag


def flat(xs: list) -> list:
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return list(chain(*xs))


def is_verb(word: str) -> bool:
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def split_snake_case_name_to_words(name: str) -> list:
    return [n for n in name.split('_') if n]


def is_magic_method(name: str) -> bool:
    return True if name.startswith('__') and name.endswith('__') else False


def is_ast_func(node: ast) -> bool:
    return True if isinstance(node, ast.FunctionDef) else False


def get_function_names_from_trees(trees: list) -> list:
    ret = []
    for t in trees:
        for node in ast.walk(t):
            if is_ast_func(node):
                ret.append(node.name.lower())
    return ret


def get_trees(path, with_filenames=False, with_file_content=False):
    # getting trees from up to 100 python files in directories

    filenames = []
    trees = []

    # walking through all directories and
    # filling a list with the first 100 Python files
    for dirname, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if len(filenames) == 100:
                break
            if file.endswith('.py'):
                filenames.append(os.path.join(dirname, file))
    print(f'total {len(filenames)} files')

    # looping through all python files and creating a tree for each file
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None
        if with_filenames:
            if with_file_content:
                trees.append((filename, main_file_content, tree))
            else:
                trees.append((filename, tree))
        else:
            trees.append(tree)
    print('trees generated')
    if len(trees) == 0:
        return None
    return trees


def get_all_names(tree):
    # iterate through the tree and return a list of node names
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_verbs_from_function_name(function_name):
    # iterate through the function_name and return a list of verbs
    return [word for word in function_name.split('_') if is_verb(word)]


def get_all_words_in_path(path):
    trees = [t for t in get_trees(path) if t]

    # getting function names from trees
    function_names = [get_all_names(t) for t in trees]
    function_names = [n for n in function_names if not is_magic_method(n)]

    # getting words from function_names
    words = []
    for function_name in function_names:
        words.append(split_snake_case_name_to_words(function_name))

    return flat(words)


def get_top_verbs_in_path(path, top_size=10):

    trees = get_trees(path)
    if trees is not None:

        names_f = get_function_names_from_trees(trees)
        fncs = [f for f in names_f if not is_magic_method(f)]
        print('functions extracted')

        verbs = [get_verbs_from_function_name(f_name) for f_name in fncs]

        return Counter(flat(verbs)).most_common(top_size)
    return Counter(None)


def get_top_functions_names_in_path(path, top_size=10):
    trees = get_trees(path)
    nms = (get_function_names_from_trees(trees))
    nms = [name for name in nms if not is_magic_method(name)]

    return Counter(nms).most_common(top_size)
