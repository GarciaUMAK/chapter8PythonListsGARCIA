myf = open("romeo.txt")

list = []

listRomeo = myf.read().split()

for word in listRomeo:
    list.append(word)

list.sort()
print(list)