#!/bin/sh

#CSVs here have UTF-8 endconding, which adds the unicode codepoint U+FEFF to the start of the file. This loops remove that tag.

for i in *.csv; do
	 sed -i $'1s/^\uFEFF//' $i
done

for i in *.csv; do
	name=`echo ${i} | sed -e 's/.csv//'`
	awk -v pop=$name -F, 'OFS="\t" {print $1, $2,$3,pop,$4,$5,$6}' ${i} > $name.bed
	echo "Finished $name..."
done
