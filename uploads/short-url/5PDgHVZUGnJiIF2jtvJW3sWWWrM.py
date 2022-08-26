f=open('scimag_search_result.txt','r');t=[eval(a)for a in f.read().split('\n')][1:];f.close()
t2=[]
for a in t:
    t2.append(repr([a[3],a[1],a[2],a[5],a[6],a[7],a[13],a[20]]))
t2='\n'.join(t2)
f=open('scimag_sr.txt','w+');f.write(t2);f.close()
