import subprocess
import getpass


command = 'sudo iptables -P INPUT ACCEPT'

password = getpass.getpass('this script uses sudo, please input your password: \n')

subprocess.run(command, input=password, shell=True) #this line sends the policy change into bash

subprocess.run('sudo iptables -L', shell=True) #this line simply shows all current policies 

