'''
Small module containing "useful" python commands to interface with linux
'''
import os;

#getting op from a command
def retSysComm(command):
	os.system(command+" > temp.txt");
	op_file = open("temp.txt","r");
	op = list();
	for line in op_file.readlines():
		line = line.strip("\n");
		op.append(line);
	op_file.close();
	os.system("rm temp.txt");
	return(op);

#print(retSysCom("free -m"));
