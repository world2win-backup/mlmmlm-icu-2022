f=open('scimag_search_result.txt','r');t=[eval(a)for a in f.read().split('\n')][1:];f.close()
t2=[]
for a in t:
    t2.append(repr([a[3],'https://sci-hub.se/%s'%a[1]]))
t2='\n'.join(t2)
f=open('scimag_sr_links.txt','w+');f.write(t2);f.close()
