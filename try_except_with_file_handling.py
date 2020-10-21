fname=input("Enter the File name With Specific Extension: ")
count=0
try:
    hand=open(fname)
except:
      print("No file Exist with name => "+fname)
      quit()
for line in hand:
      count=count+1
      print("Number of the lines Present in the",fname,"File are:",count)
