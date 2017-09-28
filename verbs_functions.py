import ast
import collections
import functions as func

from nltk import pos_tag


def is_verb(word):
    if word:
        pos_info = pos_tag([word])
        return pos_info[0][1] == 'VB'


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_top_verbs_in_path(path, top_size=10):
    trees = [t for t in func.get_trees(path) if t]
    functions = [f for f in func.flat(
        [[node.name.lower() for node in ast.walk(t) if
          isinstance(node, ast.FunctionDef)] for t in trees]) if
                 not (f.startswith('__') and f.endswith('__'))]
    verbs = func.flat([get_verbs_from_function_name(function_name) for
                  function_name in functions])
    return collections.Counter(verbs).most_common(top_size)