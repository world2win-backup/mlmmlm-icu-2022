import os,sys
st=[]
s='Sodium Chlorate'
n=0
for a in os.walk('new_scimag_2020-05-30'):
    for b in a[2]:
        n+=1
        print('%d / %d'%(n,len(a[2])))
        f=open(ld:='%s/%s'%(a[0],b));t=[c.split('),(')for c in f.read().split('\n')if'VALUES'in c];f.close()
        for c in range(len(t)):
            if'VALUES ('in t[c][0]:
                keys=t[c][0].split('VALUES')[0].replace('INSERT INTO `scimag` (','[').replace(') ',']').replace('\'','\\\'').replace('`','\'')
                t[c][0]='[%s]'%t[c][0].split('VALUES (')[1]
            for d in range(len(t[c])-1):
                if d+1==len(t[c])-1:t[c][d+1]=t[c][d+1][:-2]
                t[c][d+1]='[%s]'%t[c][d+1]
        t2=[]
        for c in t:
            for d in c:
                t2.append(d)
        t=t2
        for c in t:
            if c.find(s)!=-1:st.append(c)
        print(len(st))
tt=[keys]
tt.extend(st)
tt='\n'.join(tt)
f=open('scimag_search_result.txt','w+');f.write(tt);f.close()
