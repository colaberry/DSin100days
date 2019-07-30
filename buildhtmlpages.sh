#!/bin/sh

find content -name '*.ipynb' > nbpaths
while IFS= read -r p;
do
    printf ">>> ${p}\n"
    jupyter nbconvert --log-level ERROR --output-dir content --to html_embed "$p" || exit 1
done < nbpaths
[ -f nbpaths ] && rm nbpaths
