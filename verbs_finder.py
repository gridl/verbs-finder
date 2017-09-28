import os
import collections
import sys
import verbs_functions as vf

verbs = []
project_folders = [
    'django',
    'flask',
    'pyramid',
    'reddit',
    'requests',
    'sqlalchemy',
]
start_path = sys.argv[1] if len(sys.argv) > 1 else '.'
for project in project_folders:
    path = os.path.join(start_path, project)
    print(path)
    verbs += vf.get_top_verbs_in_path(path)

top_size = 200
words_count = 0

for word, occurence in collections.Counter(verbs).most_common(top_size):
    words_count += word[1]

print('total %s verbs, %s unique' % (words_count, len(set(verbs))))
