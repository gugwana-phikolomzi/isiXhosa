#!/bin/bash

cd data/01_raw/2008 || { echo "Directory not found"; exit 1; }

for f in *.pdf; do
  # Build new filename
  new=$(echo "$f" | \
    sed 's/ /_/g' | \
    sed 's/(/_/g' | \
    sed 's/)/_/g' | \
    sed 's/__/_/g' | \
    sed 's/.PDF$/.pdf/' | \
    sed 's/.Pdf$/.pdf/' | \
    sed 's/^IsXhosa_/isiXhosa_/' | \
    sed 's/^isxhosa_/isiXhosa_/' \
  )

  # Skip if filename doesn't change
  if [ "$f" != "$new" ]; then
    echo "Renaming: $f → $new"
    mv -i "$f" "$new"
  fi
done
