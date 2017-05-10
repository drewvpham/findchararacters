l = ['hello','world','my','name','is','Anna']
char = 'o'

n=[]
count=0
for item in l:
    if item.find(char) != -1:
        n.append(item)
print n
