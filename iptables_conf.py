import subprocess
import sys

def main(data):
    if not data:
        sys.exit()
    access_port, management_port = data['access_port'], data['management_port']

    commands = [
        ['sudo iptables -P INPUT DROP'],
        ['iptables -A INPUT -p tcp --dport 443 -j ACCEPT'],
        ['iptables -A INPUT -p tcp --dport 22869 -j ACCEPT'],
        ['iptables -A INPUT -p udp --dport 22869 -j ACCEPT'],
        ['sudo iptables -A INPUT -s 1.1.1.1 -j ACCEPT'],
        [f'iptables -A INPUT -p tcp --dport {management_port} -j ACCEPT'],
        [f'iptables -A INPUT -p tcp --dport {access_port} -j ACCEPT'],
        [f'iptables -A INPUT -p udp --dport {access_port} -j ACCEPT'],
    ]

    for command in commands:
        subprocess.run(command, shell=True, text=True) #this line sends the policy change into bash
    subprocess.run('sudo iptables -L', shell=True) #this line simply shows all current policies 

if __name__ == "__main__":
    main()