import os,sys,time
from libgen_uploader import LibgenUploader
from returns.pipeline import is_successful
from libgen_uploader import LibgenMetadata

u = LibgenUploader()
def main_cycle():time.sleep(1);main()
def main():
    try:
        lf=[]
        lf2=[]
        upurl=[]
        if os.path.exists('lf.txt'):
            f=open('lf.txt','r');lf=eval(f.read());f.close()
        if os.path.exists('lf2.txt'):
            f=open('lf2.txt','r');lf2=eval(f.read());f.close()
        
        for a,b,c in os.walk(sys.path[0]):
            for d in c:
                if d[-3:]!='jpg' and d[-2:]!='py' and d[-3:]!='txt' and d[-3:]!='swp':
                    print(lp:='%s/%s'%(a,d))
                    if lp not in lf:
                        m = LibgenMetadata(title='.'.join(lp.split('/')[-1:][0].split('.')[:-1]), language='Chinese')
                        result = u.upload_scitech(lp,metadata=m)
                        if is_successful(result):
                            upload_url = result.unwrap()
                            if lp not in lf:lf.append([lp])
                            if upload_url not in lf2:lf2.append([lp,upload_url])

                            f=open('lf.txt','w+')
                            for line in lf: {
                                f.write(line[0] + '\n')
                            }
                            f.close()

                            f=open('lf2.txt','w+')
                            for line in lf2: {
                                f.write(line[0] + '\n' + line[1] + '\n')
                            }
                            f.close()

                            print(len(lf),upload_url)
                        else:
                            failure = result.failure()
                            print(failure)
                            if lp not in lf:lf.append([lp])

                            f=open('lf.txt','w+')
                            for line in lf: {
                                f.write(line[0] + '\n')
                            }
                            f.close()
    except:main_cycle()
main()
