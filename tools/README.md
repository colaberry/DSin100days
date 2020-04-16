# notebook checks
- notebook changes are merged to master branch, only if:
1. image links in notebook are correct
2. notebook is in valid format
- these checks ensure converting ipynb formats to html
- to verify checks locally, install required packages and run buildhtmlpages.py file located in tools directory
```sh
pip install nbformat ds100nbconvert
python tools/buildhtmlpages.py
```
- when the script is run, html pages are generated without any error. If error occurs, resolve it and rerun the script.
- commit these html files and push to repo.
