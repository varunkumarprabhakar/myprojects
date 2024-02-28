n=["Varunes","Varuneed","arunies","aruned"]
a=[]
b="aeiouAEIOU"
for t in n:
    x=t.endswith("es")
    y=t.endswith("ed")
    if x is True:
        z=t.strip("es")
        a.append(z)
    elif y is True:
        v=t.strip("ed")
        a.append(v)

count=0
counta=0
for x in a:
    for i in b:
        if i in x:
            count+=1
    if count>2:
        counta+=1
    count=0
print(counta)



        

    


