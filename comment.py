import os, sys
f=open(os.path.join(os.path.dirname(__file__), "comment.txt"))



## For gitlab
print("\nGITLAB COMMENT\n")
for line in f:
	if ":" in line :
		test = line.split(":")
		if test[1].strip() :
			print("**"+test[0]+"**: "+test[1].strip() + "<br />")
	elif "." in line :
		test = line.split(".")
		print(test[0]+". "+test[1].strip()+ "<br />")
	else :
		print("**"+line.strip()+"**")


##For jira
print("\n\nJIRA COMMENT\n")
f.seek(0)
for line in f:
	if ":" in line :
		test = line.split(":")
		if test[1].strip() : #check for empty string
			if "Expected" in line :
				print("\n*"+test[0]+"*: "+test[1].strip())
			else :
				print("*"+test[0]+"*: "+test[1].strip())
	elif "." in line :
		test = line.split(".")
		print("# "+test[1].strip())
	else :
		print("*"+line.strip()+"*")
