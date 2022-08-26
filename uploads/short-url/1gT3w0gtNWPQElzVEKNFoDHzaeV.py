import requests,os,time
f=open('scimag_sr.txt','r');t=[eval(a)for a in f.read().split('\n')];f.close()
if not os.path.exists('scimag_sr'):os.makedirs('scimag_sr')
def main_cycle():time.sleep(1);main()
def main():
    n=0
    for a in t:
        n+=1
        if not os.path.exists('scimag_sr/%s.pdf'%a[8]):
            print(n,'/',len(t))
            print('https://sci-hub.se/%s'%a[1])
            g=requests.get('https://sci-hub.se/%s'%a[1]).text
            try:b='https://%s'%g.split('<button onclick = "location.href=\'//')[1].split('\'')[0]
            except:b='https://sci-hub.se/%s'%g.split('<button onclick = "location.href=\'/')[1].split('\'')[0]
            try:os.system('wget %s -O \'./scimag_sr/%s.pdf\''%(b,a[8]))
            except:main_cycle()
main()
