import os
import django
from collections import defaultdict


def dir_indo():
    rood_dir = django.__path__[0]
    django_files = defaultdict(int)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat.join(root,file)).st_size)
            django_files[size] += 1

    for size, nums in sorted(django_files.items()):
        print(f'{size}: {nums}')

dir info()