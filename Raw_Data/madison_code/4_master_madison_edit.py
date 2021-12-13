#!/usr/bin/env python

#Created March 16 2021 by Natalia
#Modified May 4 2021 by Nick
#Modified May 7 2021 by Nick and Natalia
#Modified by Natalia Sep-Nov 2021
#This will unify in a single file the segments that overlap in MultiIntersect and extract the
#We define each of the inputs the first one should be .bed file, second all the maps and
#third the output name

import os

# Define file names for .bed file, the map file, and the desired output

bed = "BedAll.bed"
MAPS = ["DMIR_sorted.bed", "DPER_sorted.bed", "DPSE_AFC14_sorted.bed", "DPSE_AFC19_sorted.bed", "DPSE_AFC24_sorted.bed", "DPSE_AFC30_sorted.bed", "DPSE_AFC47_sorted.bed", "DPSE_AFC48_sorted.bed", "DPSE_AFC49_sorted.bed", "DPSE_AFC56_sorted.bed", "DPSE_AFC57_sorted.bed", "DPSE_AFC60_sorted.bed", "DPSE_Cirulli_sorted.bed", "DPSE_Flagstaff_sorted.bed", "DPSE_FlagstaffUtraFine_sorted.bed", "DPSE_Kulathinal_sorted.bed", "DPSE_MC13_sorted.bed", "DPSE_MC14_sorted.bed", "DPSE_MC15_sorted.bed", "DPSE_MC17_sorted.bed", "DPSE_MC20_sorted.bed", "DPSE_MC27_sorted.bed", "DPSE_MC6_sorted.bed", "DPSE_Pikespeak_sorted.bed"]
output="MasterSpreadSheet.bed"

if os.path.exists(output):
	os.remove(output)
	
# Read both_sorted.bed and map input files

a_file = open(bed, 'r')

# Loop through the_sorted.bed file, strip newline tags, split my tab, and then open the output file to write
for line in a_file:
	line=line.strip("\n")	
	line_array = line.split("\t")
	out_1=open(output, 'a')
	temp_tuple=(line_array[0], line_array[1], line_array[2])
	temp_h="\t".join(temp_tuple)
	cols=[line_array[5], line_array[6], line_array[7], line_array[8], line_array[9], line_array[10], line_array[11], line_array[12], line_array[13], line_array[14], line_array[15], line_array[16], line_array[17], line_array[18], line_array[19], line_array[20], line_array[21], line_array[22], line_array[23], line_array[24], line_array[25], line_array[26], line_array[27], line_array[28]]
	print("Made it to bed in output")
	for map, col in zip(MAPS, cols):
		map_file = open(map, 'r')
		if col == '1':
# Start a new loop through the map file and apply strip/split.
# Then, if the value coordinates fall inside of any of bed coordinates, print them to an output file
# seek command should allow loop to continue bed file 

			sample_list=[]
			cross_list=[]
	
			for LINE in map_file:
				LINE=LINE.strip("\n")
				LINE_array=LINE.split("\t")
				name=(LINE_array[3])
				sample_temp=(int(LINE_array[5])/int(len(LINE_array[5])))
				sample_list.append(sample_temp)
				sample=sum(sample_list)
				cross_temp=int(LINE_array[4])
				cross_list.append(cross_temp)
				cross=sum(cross_list)
				rec=(int(cross)/int(sample))*100
				to_print=["sample","cross","rec"]
				temp=[]
				if int(LINE_array[1]) >= int(line_array[1]) and int(LINE_array[2]) <= int(line_array[2]):
					temp.append(LINE_array[0]+"\t"+LINE_array[1]+"\t"+LINE_array[2]+"\t"+LINE_array[3]+"\t"+LINE_array[4]+"\t"+LINE_array[5]+"\n")
					sample_list_2=[]
					cross_list_2=[]
					for data in temp:
						sample_temp_2=(int(LINE_array[4])/int(len(LINE_array[4])))
						sample_list_2.append(sample_temp_2)
						sample=sum(sample_list_2)
						cross_temp_2=int(LINE_array[4])
						cross_list_2.append(cross_temp_2)
						cross=sum(cross_list_2)

						#Some sample numbers are 0, so define function to avoid error.
						def rec_zero(x,y):
							try:
								rec=(int(x)/int(y))*100
							except ZeroDivisionError:
								return 0

						rec=rec_zero(int(cross),int(sample))
						
				with open(output, 'a') as file:
												
#out_1=open(output, 'a')	
					file.write(str(temp_h)+"\t"+str(sample)+"\t"+str(cross)+"\t"+str(rec)+"\t"+name+"\n")							
			map_file.seek(0)
		if col == '0':
                	with open(output, 'a') as file:
				
	                	file.write(str(temp_h)+"\t"+"NA"+"\t"+"NA"+"\t"+"NA"+"\t"+name+"\n")
# Close all files

	out_1.close()
map_file.close()
a_file.close()
