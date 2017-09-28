import ast
import os


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def get_trees(_path):
    filenames = []
    trees = []
    for dirname, dirs, files in os.walk(_path, topdown=True):
       fill_filenames_array(files, filenames, dirname)
    for filename in filenames:
        trees.append(generate_tree(filename))
    return trees


def fill_filenames_array(files, filenames, dirname):
    gen = (file for file in files if file.endswith('.py'))
    for file in gen:
        filenames.append(os.path.join(dirname, file))


def generate_tree(filename):
    tree = None
    with open(filename, 'r', encoding='utf-8') as attempt_handler:
        main_file_content = attempt_handler.read()
    try:
        tree = ast.parse(main_file_content)
    except SyntaxError as e:
        print(e)
    return tree






