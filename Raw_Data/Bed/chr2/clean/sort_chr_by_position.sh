#! /bin/sh

for i in *.bed
do
name=`echo ${i} | sed -e 's/.bed//'`
sort -k1,1 -k2,2n ${i} > $name.bed
echo "Finished $name..."
done
