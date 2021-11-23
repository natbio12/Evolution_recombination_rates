#! /bin/sh

for i in *.csv
do
name=`echo ${i} | sed -e 's/.csv//'`
awk -v pop=$name -F, 'OFS="\t" {print $1, $2,$3,pop,$4,$5,$6}' ${i} > Bed/$name.bed
echo "Finished $name..."
done
