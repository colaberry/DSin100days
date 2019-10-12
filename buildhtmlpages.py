'''
NOTE:
Install nbformat and ds100nbconvert packages, to install run:
pip install nbformat ds100nbconvert
'''

import warnings
import glob
import nbformat
from traitlets.config import Config
from ds100nbconvert import EmbedHTMLExporter


def get_notebook_paths():
    content_notebooks = []
    micro_courses_notebooks = []
    for p in glob.iglob('content/**/*.ipynb', recursive=True):
        content_notebooks.append(p)
    for p in glob.iglob('micro_courses/**/*.ipynb', recursive=True):
        micro_courses_notebooks.append(p)
    total = len(content_notebooks) + len(micro_courses_notebooks)
    notebook_paths = content_notebooks + micro_courses_notebooks
    return notebook_paths


def build(p):
    with open(p, 'r') as f:
        d = f.read()
    e = EmbedHTMLExporter()
    n = nbformat.reads(d, as_version=4)
    try:
        b, r = e.from_notebook_node(n)
    except FileNotFoundError as e:
        print('>>>', p)
        print(e, '\n')
    else:
        hp = p.replace('.ipynb', '.html')
        with open(hp, 'w') as f:
            f.write(b)


warnings.filterwarnings("ignore")
notebook_paths = get_notebook_paths()
for p in notebook_paths:
    build(p)
