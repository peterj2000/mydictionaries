infile = open("sometext.txt") 
sep = infile.read().split(" ")


dic = {} 

for var in sep: 
    if var.isalnum(): 
        if var in dic:
            dic[var] = dic.get(var)+1
        else:
            dic[var] = 1 


dic = sorted(dic.items(), key=lambda x: x[1]) 


for var in dic: 
    print(var[0]+":"+str(var[1])+"\n") 