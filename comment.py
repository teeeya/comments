import os, sys, re
f=open(os.path.join(os.path.dirname(__file__), "comment.txt"))



## For gitlab
first = True
print("\nGITLAB COMMENT\n")
for line in f:
	if re.match("^[A-Z]", line) and (":" in line):
		test = line.split(":")
		if test[1].strip() :
			if "Expected" in test[0] :
				print("\n"+"**"+test[0]+"**: "+test[1].strip() + "<br />")
			else: 
				print("**"+test[0]+"**: "+test[1].strip() + "<br />")
		else : 
			if "Test Steps" in test[0] :
				print("\n"+"**"+test[0]+"**: "+test[1].strip() + "<br />")
			else:
				print ("i am here" + line)
				print("**"+test[0]+"**: "+ "<br />")
	elif re.match("(^[0-9]\.)", line) :
		test = line.split(".")
		print(test[0]+". "+test[1].strip()+ "<br />")
	elif "-" in line :
		if(first):
			test = line.split("-")
			print("\n" + "* "+test[1].strip())
			first = False
		else:
			test = line.split("-")
			print("* "+test[1].strip())
	else :
		print("**"+line.strip()+"**"+"<br />")


##For jira
print("\n\nJIRA COMMENT\n")
f.seek(0)

first = True
for line in f:
	if re.match("^[A-Z]", line) and (":" in line):
		test = line.split(":")
		if test[1].strip() : #check for empty string
			if "Expected" in line :
				print("\n*"+test[0]+"*: "+test[1].strip())
			else :
				print("*"+test[0]+"*: "+test[1].strip())
		else:
			if "Test Steps" in test[0] :
				print("\n"+"*"+test[0]+"*: "+test[1].strip())
	elif re.match("(^[0-9]\.)",line) :
		test = line.split(".")
		print("# "+test[1].strip())
	elif "-" in line :
		if(first) :
			test = line.split("-")
			print("\n"+"* "+test[1].strip())
			first=False
		else :
			test = line.split("-")
			print("* "+test[1].strip())
	else :
		print("*"+line.strip()+"*")
