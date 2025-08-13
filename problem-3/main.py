# file = "INPUT.txt"
# out = "OUTPUT.txt"

# with open(file, "r") as f:
#     a = f.readline()
#     b = f.readline()
#     ansint = int(a) + int(b)
#     fin = str(ansint)
    

#     with open(out, "a") as o:
#         o.write(fin)


file = "INPUT.txt"
out = "OUTPUT.txt"

with open(file, "r") as f:
    a = f.readline().strip()
    b = f.readline().strip()
    ansint = int(a) + int(b)
    fin = str(ansint)

with open(out, "w") as o:
    o.write(fin)

