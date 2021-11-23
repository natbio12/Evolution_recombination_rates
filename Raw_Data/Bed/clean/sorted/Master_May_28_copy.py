#!/usr/bin/env python

#Created March 16 2021 by Natalia
#Modified May 4 2021 by Nick
#Modified May 7 2021 by Nick and Natalia

#This will unify in a single file the segments that overlap in MultiIntersect and extract the
#We define each of the inputs the first one should be our bed file, second all the maps and
#third the output name

# Define file names for the bed file, the map file, and the desired output
import math
bed = "MultiBed_Chr2.bed"
MAPS = ["CirulliDPSE.bed", "Dmiranda_MG.bed", "Dpersimilis_LS.bed", "DPSE_K.bed", "DPSE_S_Original.bed", "FlagstaffDPSE_MG.bed", "PikesPeakDPSE_MG.bed"]
output="Chr2_Segments.bed"
output2="MasterSpreadSheet_Chr2Segments.bed"

# Read both bed and map input files

a_file = open(bed, 'r')

# Loop through the bed file, strip newline tags, split my tab, and then open the output file to write
for line in a_file:
	line=line.strip("\n")	
	line_array = line.split("\t")
	out_1=open(output, 'a')
	out_2=open(output2, 'a')
	out_3=open(output, 'r')		
	cols=[line_array[11], line_array[6], line_array[7], line_array[8], line_array[5], line_array[9], line_array[10]]

	for map, col in zip(MAPS, cols):
		map_file = open(map, 'r') 
		if col == "1":
			for LINE in map_file:
				LINE=LINE.strip("\n")
				LINE_array=LINE.split("\t")
				if int(LINE_array[1]) >= int(line_array[1]) and int(LINE_array[2]) <= int(line_array[2]):
					out_1.write(line_array[0]+"\t"+line_array[1]+"\t"+line_array[2]+"\t"+LINE_array[3]+"\t"+LINE_array[4]+"\t"+LINE_array[5]+"\t"+LINE_array[6]+"\n")
				
#			for seg in out_3:
#				seg=seg.strip("\n")
#				seg_array=seg.split("\t")
#				sam_1=[int(x) for x in seg_array[6]]
#				sample=int(seg_array[6])//len(seg_array[6])
#				sam_2=seg_array[5]
#				crosses=sum([int(i) for i in sam_2 if type(i)== int or i.isdigit()])
#				if crosses > "0":
#					rec=(int(crosses)//int(sample))*100
#				else:
#					rec=0	
#				out_2.write(line_array[0]+"\t"+line_array[1]+"\t"+line_array[2]+"\t"+LINE_array[3]+"\t"+str(sample)+"\t"+str(crosses)+"\t"+"\t"+"\n")
		
			map_file.seek(0)

		if col == "0":
			for LINE in map_file:
				LINE=LINE.strip("\n")
				LINE_array=LINE.split("\t")
			out_2.write(line_array[0]+"\t"+line_array[1]+"\t"+line_array[2]+"\t"+LINE_array[3]+"\t"+"NA"+"\t"+"NA"+"\t"+"NA"+"\n")

out_1.close()
out_2.close()
out_3.close()
map_file.close()
a_file.close()
