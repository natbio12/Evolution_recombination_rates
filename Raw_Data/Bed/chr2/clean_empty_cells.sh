#! /bin/sh

for i in *.bed
do
name=`echo ${i} | sed -e 's/.bed//'`
awk '$7!=""' ${i} > clean/$name.bed
echo "Finished $name..."
done
