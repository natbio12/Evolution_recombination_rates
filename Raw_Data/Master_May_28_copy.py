#!/usr/bin/env python

#Created March 16 2021 by Natalia
#Modified May 4 2021 by Nick
#Modified May 7 2021 by Nick and Natalia

#This will unify in a single file the segments that overlap in MultiIntersect and extract the
#We define each of the inputs the first one should be our bed file, second all the maps and
#third the output name

# Define file names for the bed file, the map file, and the desired output

bed = "FinalBed"
MAPS = ["CirulliDPSE.bed", "Dmiranda_MG.bed", "Dpersimilis_LS.bed", "DPSE_K.bed", "DPSE_S.bed", "FlagstaffDPSE_MG.bed", "PikesPeakDPSE_MG.bed"]
output="MasterSpreadSheet.bed"

# Read both bed and map input files

a_file = open(bed, 'r')

# Loop through the bed file, strip newline tags, split my tab, and then open the output file to write
for line in a_file:
	line=line.strip("\n")	
	line_array = line.split("\t")
	out_1=open(output, 'a')
	
	cols=[line_array[11], line_array[6], line_array[7], line_array[8], line_array[5], line_array[9], line_array[10]]
#	print("Made it to print bed in output")
	for map, col in zip(MAPS, cols):
		map_file = open(map, 'r') 
		print(type(col))
		if col == "1":
			print(col)
# Start a new loop through the map file and apply strip/split.
# Then, if the value coordinates fall inside of any of the bed coordinates, print them to an output file
# seek command should allow loop to continue through bed file 
	
			for LINE in map_file:
				LINE=LINE.strip("\n")
				LINE_array=LINE.split("\t")
				#sample=sum(LINE_array[6])/len(LINE_array[6])
				#cross=sum(LINE_array[5])
				#rec=(int(cross)/int(sample))*100
				#to_print=["sample",""cross","rec"]
	#			temp=[]
				if int(LINE_array[1]) >= int(line_array[1]) and int(LINE_array[2]) <= int(line_array[2]):
					temp=[LINE_array[0]+"\t"+LINE_array[1]+"\t"+LINE_array[2]+"\t"+LINE_array[3]+"\t"+LINE_array[4]+"\t"+LINE_array[5]+"\t"+LINE_array[6]+"\n"]
					for data in temp:
						sample=sum(LINE_array[6])/int((len(LINE_array[6]))
						cross=sum(LINE_array[5])
						rec=(int(cross)/int(sample))*100
												
#out_1=open(output, 'a')	
						out_1.write(line_array[0]+"\t"+line_array[1]+"\t"+line_array[2]+"\t"+sample+"\t"+cross+"\t"+rec+"\n")							
			map_file.seek(0)
		if col == "0":
	                	out_1.write(line_array[0]+"\t"+line_array[1]+"\t"+line_array[2]+"\t"+"NA"+"\t"+"NA"+"\t"+"NA"+"\n")
# Close all files

	out_1.close()
map_file.close()
a_file.close()
