import os
import nbconvert
import nbformat
from nbconvert import HTMLExporter


def replaceReplacement(filename):
    return filename.replace(".ipynb", ".html")

def copyContentRepo():
    command = 'cp -R content/ html-pages/content'
    os.system(command)

def convert(directory):
    for root, _, files in os.walk(directory, topdown=False):
        for i in files:
            if 'content' in root:
                file_path = root + '/' + i
                if '.ipynb' in file_path:
                    print(file_path)
                    known_idex = file_path.rfind('/') + 1
                    ntb = nbformat.read(file_path, as_version=4)
                    (body, resources) = exporter.from_notebook_node(ntb)
                    file_path = replaceReplacement(file_path)
                    filename = file_path[known_idex:]
                    html_file = open(file_path, "w")
                    html_file.write(body)
            copyContentRepo()
    

if __name__ == "__main__":
    dsin100days_direct = 'content'
    exporter = HTMLExporter()
    convert(dsin100days_direct)



