#!/bin/sh

[ -d "html-pages/content" ] && rm -r html-pages/content
cp -r content html-pages/
find html-pages/content -name '*.ipynb' > nbpaths
while IFS= read -r p;
do
    printf ">>> ${p}\n"
    jupyter nbconvert --log-level ERROR --output-dir html-pages --to html_embed "$p" || exit 1
done < nbpaths
[ -f nbpaths ] && rm nbpaths
