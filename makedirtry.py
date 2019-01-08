import os
directory=input("enter the name")
if not os.path.exists(directory):
	os.makedirs(directory)
