import os,sys,time
######################################################################
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.06)
######################################################################
logo = """
\033[1;34m                       dP   dP                         
\033[1;34m                       88   88                         
\033[1;37m   88d888b. dP    dP d8888P 88d888b. .d8888b. 88d888b. 
\033[1;37m   88'  `88 88    88   88   88'  `88 88'  `88 88'  `88 
\033[1;33m   88.  .88 88.  .88   88   88    88 88.  .88 88    88 
\033[1;33m   88Y888P' `8888P88   dP   dP    dP `88888P' dP    dP 
\033[1;34m   88            .88                                   
\033[1;34m   dP        d8888P           

\033[1;34m   dP    8888b          
\033[1;37m   88 o  88             
\033[1;33m   88 dP 88aaa  .d8888b. 
\033[1;33m   88 88 88     88ooood8 
\033[1;37m   88 88 88     88 \033[1;31m    Created by Riad
\033[1;34m   dP dP dP     `88888P

"""
######################################################################
os.system('clear')
os.system('git pull https://github.com/python-life/login')
os.system('clear')
print(logo)
print("\033[1;31m[1] \033[1;34mTermux login")
time.sleep(0.3)
print("\033[1;31m[2] \033[1;34mRemove termux login")
time.sleep(0.3)
print("\033[1;31m[3] \033[1;34mMy instagram")
time.sleep(0.3)
print("\033[1;31m[0] \033[1;34mExit")
time.sleep(0.3)
print("")
######################################################################
choose = input("\033[1;31m[?]\033[1;34mChoose an option : ")
time.sleep(0.3)
######################################################################
if choose == '1':
    os.system('cp log.py $HOME')
    os.chdir('/data/data/com.termux/files/usr/etc')
    os.system('rm -rf bash.bashrc')
    os.system('cd $HOME;cd login/log;cp bash.bashrc /data/data/com.termux/files/usr/etc')
    os.system('clear')
    print(logo)
    jalan("\033[1;33mRestart the application")
    time.sleep(0.5)
    os.system('exit')
######################################################################
elif choose == '2':
    jalan("\033[1;31mplease wait...")
    os.system('cd /data/data/com.termux/files/usr/etc;rm -rf bash.bashrc')
    os.system('cd $HOME;cd login/original ;cp bash.bashrc /data/data/com.termux/files/usr/etc')
    os.system('clear')
    print(logo)
    print("\033[1;33mRestart the application")
    time.sleep(0.5)
    os.system('exit')
######################################################################
elif choose == '3':
    os.system('xdg-open https://www.instagram.com/pyth0nlife')
    os.system('clear')
    print(logo)
    time.sleep(0.3)
    os.system('exit')
######################################################################
elif choose =='0':
    os.system('exit')






