#! /bin/sh

for i in *.bed; do
	name=`echo ${i} | sed -e 's/.bed//'`
	sort -k 1,1 -k 2,2n ${i} > ${name}_sorted.bed
	echo "Finished $name..."
done
