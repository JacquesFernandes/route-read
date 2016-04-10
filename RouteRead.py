#!/usr/bin/python3

import os;
try:
	import PyLin;
except ImportError:
	print("MISSING PyLin code! Please keep it in the same directory as this code...");
	print("exiting!");
	exit();
import sys;

print("Generating Traceroute file...");
if len(sys.argv) == 2:
	ip = sys.argv[1];
	output = PyLin.retSysComm("traceroute "+ip);
	f = open(ip+"_traceroute.txt","w");
	for line in output:
		f.write(line+"\n");
	f.close();

print("Traceroute complete, pick the .txt file with the name of the site...");
dir = os.listdir();

for i in range(0,len(dir)):
	try:
		if (".py" not in dir[i]):
			print(str(i)+" - "+dir[i]);
	except IndexError:
		print("...");

fnum = -1;

try:
	fnum = int(input("Enter number of file: "));
except ValueError:
	print("what did you enter?!");
	exit();

try:
	if ".py" in dir[fnum]:
		print("You selected an invalid file...");
		exit();
	f = open(dir[fnum]);
except IndexError:
	print("Invalid entry");

addr = list();

for line in f.readlines():
	addr.append(line[line.find("(")+1 : line.find(")")]);

try:
	os.mkdir(dir[fnum].strip(".txt"));
except FileExistsError:
	print("directory already exists, removing it...");
	PyLin.retSysComm("rm -r "+dir[fnum].strip(".txt"));
	os.mkdir(dir[fnum].strip(".txt"));
os.chdir(dir[fnum].strip(".txt"));

OrgName="";
OrgId="";
Address="";
City="";
StateProv="";
PostalCode="";
Country="";

for a in addr:
	print("checking whois "+a);
	res = PyLin.retSysComm("whois "+a);
	f = open("whois "+a+".txt","a+");
	for line in res:
		if "OrgName" in line:
			print(line);
			f.write(line+"\n");
		if "OrgId" in line:
			print(line);
			f.write(line+"\n");
		if "Address" in line:
			print(line);
			f.write(line+"\n");
		if "City" in line:
			print(line);
			f.write(line+"\n");
		if "StateProv" in line:
			print(line);
			f.write(line+"\n");
		if "PostalCode" in line:
			print(line);
			f.write(line+"\n");
		if "Country" in line:
			print(line);
			f.write(line+"\n");
	print("----------------------------------------");
	f.close();

print("RESULTS are also stored in "+dir[fnum].strip(".txt")+" folder...");
