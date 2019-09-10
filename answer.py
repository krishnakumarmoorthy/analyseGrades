import os
# [Example] Read datasets
import pandas as pd
import numpy as np
f=open("data/training/testcaseStudent.txt",'r')
n=int(f.readline().rstrip())
o=1
outstr=""
def check(v,value):
	value=int(value)
	if v == "lessthan50":
		if(value < 5):
			return True
	elif v == "between50and60":
		if(value >= 5 and value < 6):
			return True
	elif v == "between60and70":
		if(value >= 6 and value <7):
			return True
	elif v == "between70and80":
		if(value >=7 and value <8):
			return True
	elif v == "greaterthan80":
		if(value >= 8):
			return True
	return False
			
while(n>0):
	filestr="code/output"+str(o)+".txt"
	o+=1
	outfile = open(filestr,'w')
	b = "data/training/batchwiselist/" + str(f.readline().rstrip())
	cond = str(f.readline().rstrip())
	batchfile = pd.read_csv(b)
	q1 = pd.read_csv("data/training/quiz/quiz1.csv", names=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'])
	count = 0
	lst = []
	for val in batchfile.studentName:
		lst.append(val)
	sf = (q1.b).tolist()
	sfs = (q1.k).tolist()
	leniter = len(sf)
	for val in lst:
		for i in range(leniter):
			if val == sf[i]:
				count+=check(cond,sfs[i])
	outstr=str(count)+"\n"
	q2 = pd.read_csv("data/training/quiz/quiz2.csv", names=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'])
	count = 0
	lst = []
	for val in batchfile.studentName:
		lst.append(val)
	sf = (q2.b).tolist()
	sfs = (q2.k).tolist()
	leniter = len(sf)
	for val in lst:
		for i in range(leniter):
			if val == sf[i]:
				count+=check(cond,sfs[i])
	outstr=outstr + str(count)
	outfile.write(outstr)
	n-=1
	outfile.close()
