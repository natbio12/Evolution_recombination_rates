#! /bin/sh

for i in *.bed
do
name=`echo ${i} | sed -e 's/.bed//'`
grep -w chr2 ${i} > chr2/$name.bed
echo "Finished $name..."
done


