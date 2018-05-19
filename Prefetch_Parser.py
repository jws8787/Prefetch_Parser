import os
import sys
import glob
import datetime
from XPRESS_decompress import *

def LittleEndian_Int(buf):
	Val = 0
	for i in range(0, len(buf)):
		Multi = 1
		for j in range(0, i):
			Multi *= 256
		Val += buf[i] * Multi
	return Val

Dir_path=sys.argv[1]
PF_file_list =  glob.glob(Dir_path+'/*.pf')

PF_file_Name, PF_file_Size, PF_file_Last_Run_Time = [],[],[]

for PF_file in PF_file_list:
	Data = decompress(PF_file)
	PF_file_Name.append(Data[16:75])
	PF_file_Size.append(LittleEndian_Int(Data[12:15]))
	