import sys



if len(sys.argv) < 2:
    print ("id-gen [number of IDs] [Output file]")
    exit


f = open(sys.argv[2], "w")

i = int(sys.argv[1])

for j in range(1, i+1):
    f.write(str(j))
    f.write("\n")


f.close()






