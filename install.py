import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 DBC.py')
    run('mkdir /usr/share/dbc')
    run('cp DBC.py /usr/share/dbc/DBC.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/dbc/DBC.py "$@"')
    with open('/usr/bin/dbc','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/dbc & chmod +x /usr/share/dbc/DBC.py')
    print('''\n\done install dutchbro ip changer \nfrom now just type \x1b[6;30;42mdbc\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/dbc ')
    run('rm /usr/bin/dbc ')
    print('[!] Done install IP Changer DutchBro')
