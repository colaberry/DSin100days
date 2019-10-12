import glob
import nbformat
from traitlets.config import Config
from ds100nbconvert import EmbedHTMLExporter



def get_html(p):
    with open(p, 'r') as f:
        d = f.read()
    n = nbformat.reads(d, as_version=4)
    e = EmbedHTMLExporter()
    b, r = e.from_notebook_node(n)
    return b


def build(p):
    hp = p.replace('.ipynb', '.html')
    with open(hp, 'w') as f:
        f.write(get_html(p))


def main():
    content_notebooks = []
    micro_courses_notebooks = []

    for p in glob.iglob('content/**/*.ipynb', recursive=True):
        content_notebooks.append(p)

    for p in glob.iglob('micro_courses/**/*.ipynb', recursive=True):
        micro_courses_notebooks.append(p)

    total = len(content_notebooks) + len(micro_courses_notebooks)

    print('>>> Generating html pages from content notebooks')
    c = 0
    f = 0
    for p in content_notebooks:
        c += 1
        s = '>>> %d/%d' % (c, total)
        print(s, p)
        try:
            build(p)
        except FileNotFoundError as e:
            f += 1
            print('EEEEEEEEEEEE', e)

    c = 0
    print('>>> Generating html pages from micro_courses notebooks')
    for p in micro_courses_notebooks:
        c += 1
        s = '>>> %d/%d' % (c, total)
        print(s, p)
        try:
            build(p)
        except FileNotFoundError as e:
            f += 1
            print('EEEEEEEEEEEE', e)

    print(f)
main()
