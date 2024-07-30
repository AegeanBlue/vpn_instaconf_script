import subprocess
import sys

def main(data, ssh_port):
    if not data:
        sys.exit()
    access_port, management_port = data['access_port'], data['management_port']

    commands = [
        
        ['sudo iptables -A INPUT -s 127.0.0.1 -j ACCEPT'],
        ['sudo iptables -A INPUT -s 1.1.1.1 -j ACCEPT'],
        ['iptables -A INPUT -p tcp --dport 443 -j ACCEPT'],
        [f'iptables -A INPUT -p tcp --dport {ssh_port} -j ACCEPT'],
        [f'iptables -A INPUT -p udp --dport {ssh_port} -j ACCEPT'],
        [f'iptables -A INPUT -p tcp --dport {management_port} -j ACCEPT'],
        [f'iptables -A INPUT -p tcp --dport {access_port} -j ACCEPT'],
        [f'iptables -A INPUT -p udp --dport {access_port} -j ACCEPT'],
        ['sudo systemctl restart ssh'],
        ['sudo iptables -P INPUT DROP'],
    ]

    for command in commands:
        subprocess.run(command, shell=True, text=True) #this line sends the policy change into bash
    subprocess.run('sudo iptables -L', shell=True) #this line simply shows all current policies 

if __name__ == "__main__":
    main()