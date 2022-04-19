st = input("Enter String : ")


dicts =  {}


for ch in st:
    if ch in dicts:
        dicts[ch]+=1
    else:
        dicts[ch]=1
    

l = len(set(st))

for i in range(0,l):
    maxli = [0,0]
    for key in dicts:
        if dicts[key]>maxli[1]:
            maxli[0] = key
            maxli[1] = dicts[key]
    print(maxli[0]+ " " +str(maxli[1]))
    dicts.pop(maxli[0])
