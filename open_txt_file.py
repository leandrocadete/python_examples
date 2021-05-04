import os

f = open("myfile.txt", "w")
for i in range(10):    
    f.write("line -> " + str(i) + "\n")   
f.close()

fo = open("myfile.txt", "r")
for s in  fo.readlines():
    print(s)
fo.close()
