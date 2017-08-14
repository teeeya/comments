import os, sys
f=open(os.path.join(os.path.dirname(__file__), "comment.txt"))



## For gitlab
print("\nGITLAB COMMENT\n")
for line in f:
	if ":" in line :
		test = line.split(":")
		if test[1].strip() : #check for empty string
			if "Expected" in line or "Actual" in line: 
				print("\n**"+test[0]+"**: "+test[1].strip())
			else :	
				print("**"+test[0]+"**: "+test[1].strip() + "<br />")
		elif "Test Steps" in test[0].strip() or "Pre-requisites" in test[0].strip() or "Expected" in line or "Actual" in line:
			print ("\n**" + test[0].strip()+ "**")
	elif "." in line :
		test = line.split(".")
		print(test[0]+". "+test[1].strip()+ "<br />")
	elif "-" in line :
		print("-"+line.strip()+ "<br />")
	else :
		print("**"+line.strip()+"**")

##For jira
print("\n\nJIRA COMMENT\n")
f.seek(0)
for line in f:
	if ":" in line :
		test = line.split(":")
		if test[1].strip() : #check for empty string
			if "Expected" in line or "Actual" in line:
				print("\n*"+test[0]+"*: "+test[1].strip())
			else :
				print("*"+test[0]+"*: "+test[1].strip())
		elif "Test Steps" in test[0].strip() or "Pre-requisites" in test[0].strip() or "Expected" in line or "Actual" in line:
			print ("\n*"+ test[0].strip()+ "*")		
	elif "." in line :
		test = line.split(".")
		print("# "+test[1].strip())
	elif "-" in line :
		print("-"+line.strip())	
	else :
		print("*"+line.strip()+"*")
