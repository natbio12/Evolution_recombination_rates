#!/usr/bin/env python

#Created March 16 2021 by Natalia
#Modified May 4 2021 by Nick
#Modified May 7 2021 by Nick and Natalia
#Modified by Natalia Sep-Nov 2021

#This will unify in a single file the segments that overlap in MultiIntersect and extract them from each map

#We define each of the inputs the first one should be our bed file, second all the maps and
#third the output name

# Define file names for the bed file, the map file, and the desired output

bed = "BedAll2.bed"
MAPS = ["DMIR.bed", "DPER.bed", "DPSE_AFC14.bed", "DPSE_AFC19.bed", "DPSE_AFC24.bed", "DPSE_AFC30.bed", "DPSE_AFC47.bed", "DPSE_AFC48.bed", "DPSE_AFC49.bed", "DPSE_AFC56.bed", "DPSE_AFC57.bed", "DPSE_AFC60.bed", "DPSE_Cirulli.bed", "DPSE_Flagstaff.bed", "DPSE_FlagstaffUtraFine.bed", "DPSE_Kulathinal.bed", "DPSE_MC13.bed", "DPSE_MC14.bed", "DPSE_MC15.bed", "DPSE_MC17.bed", "DPSE_MC20.bed", "DPSE_MC27.bed", "DPSE_MC6.bed", "DPSE_Pikespeak.bed"]
output="MasterSpreadSheet.bed"

# Read both bed and map input files

a_file = open(bed, 'r')

# Loop through the bed file, strip newline tags, split by tab, and then open the output file to write
for line in a_file:
	line=line.strip("\n")
	line_array = line.split("\t")
	out_1=open(output, 'a')
	temporal_array1=[]
	temporal_array1=["line_array[0]" + "\t" + "line_array[1]" + "\t" + "line_array[2]" + "\t"]
	cols=["line_array[5]", "line_array[6]", "line_array[7]", "line_array[8]", "line_array[9]", "line_array[10]", "line_array[11]", "line_array[12]", "line_array[13]", "line_array[14]", "line_array[15]", "line_array[16]", "line_array[17]", "line_array[18]", "line_array[19]", "line_array[20]", "line_array[21]", "line_array[22]", "line_array[23]", "line_array[24]", "line_array[25]", "line_array[26]", "line_array[27]", "line_array[28]"]
	print("Made it to print bed in output")
	for map, col in zip(MAPS, cols):
		map_file = open(map, 'r')
		if col == 1:
			
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
				temporal_array2=[]
				if int(LINE_array[1]) >= int(line_array[1]) and int(LINE_array[2]) <= int(line_array[2]):
					temporal_array2.append["LINE_array[3]"+"\t"+"LINE_array[4]"+"\t"+"LINE_array[5]"+"\n"]
				#for data in temporal_array2:
				#	sample=sum(LINE_array[4])/len(LINE_array[4])
				#	cross=sum(LINE_array[3])
				#	rec=(int(cross)/int(sample))*100
				with open(output, 'w') as file:
												
#out_1=open(output, 'a')	
					output.write(temporal_array1 + "\t" + temporal_array2 + "\n")
			map_file.seek(0)
		if col == 0:
                	with open(output, 'w') as file:
	                	output.write(temporal_array1 + "\t" + "NA" + "\t" + "NA" + "\n")
# Close all files

	out_1.close()
map_file.close()
a_file.close()
