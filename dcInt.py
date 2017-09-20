import os
import collections
import functions as f

verbs = []
project_folders = [
    'django',
    'flask',
    'pyramid',
    'reddit',
    'requests',
    'sqlalchemy',
]
for project in project_folders:
    path = os.path.join('.', project)
    verbs += f.get_top_verbs_in_path(path)

top_size = 200
words_count = 0

for word, occurence in collections.Counter(verbs).most_common(top_size):
    words_count += word[1]

print('total %s verbs, %s unique' % (words_count, len(set(verbs))))
