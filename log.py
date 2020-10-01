from getpass import getpass
import os,sys,time

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.06)

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

def menu():
    while True:
        print("")
        os.system("clear")
        print(logo)
        try:
            x = str(input('\033[1;34mUsername \033[1;33m: '))
            print("")
            e = getpass('\033[1;34mPassword \033[1;33m: ')
            print("")
            if x == "python" and e == "life":
                jalan('wait........')
                time.sleep(1)
                os.system('clear')
                break
            else:
                print("")
                print("")
                print("")
                print("")
                print("\033[1;31m     Wrong Password")
                time.sleep(2)
                print("")
        except Exception:

            print("")
            print("")
            print("")
            print("")
            print("")
            print("\033[1;31m     Wrong Password")
            time.sleep(2)
        except KeyboardInterrupt:
            print("")
            os.system('killall -9 com.termux')
            print("")
            print("")
            print("")
            print("")
            print("\033[1;31m     Wrong Password")
            time.sleep(2)


menu()