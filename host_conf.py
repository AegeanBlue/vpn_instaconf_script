import subprocess

def main(): 
    
    print('>>>Checking for Visudo...\n ')
    subprocess.run('sudo apt install visudo', text=True, shell=True) # check for visudo
    
    print('>>>Checking for Curl...\n ')
    subprocess.run('sudo apt install curl', text=True, shell=True) #check for curl
    
    print('>>>Checking for Iptables...\n ')
    subprocess.run('sudo apt install iptables', text=True, shell=True) #check for iptables

    user_input_hostname = input('>>>Change hostname (leave empty to keep default value): ') #change hostname
    if user_input_hostname:
        subprocess.run(f'sudo hostname {user_input_hostname}', text=True, shell=True)
    
    user_input_timezone = input('>>>Change timezone (leave empty to keep default value): ') #change timezone
    if user_input_timezone:
        subprocess.run(f'sudo timedatectl set-timezone {user_input_timezone}', text=True, shell=True)

    user_input_ssh_port = input('>>>change ssh port (leave empty to keep default value): ') #change SSH connection port
    if user_input_ssh_port: #checks for empty input
        new_port = f'Port {user_input_ssh_port}' 
        with open('/etc/ssh/sshd_config', 'r') as ssh_config: 
            ssh_text = ssh_config.read() #converts the thing to string
            new_text = ssh_text.replace('#Port 22', new_port)

        with open('/etc/ssh/sshd_config', 'w') as ssh_config:
            ssh_config.write(new_text)
        
    user_input_new_user = input('>>>New user (leave empty to skip this step): ') # create new sudo user
    if user_input_new_user:
        subprocess.run(f'sudo adduser {user_input_new_user}', text=True, shell=True)
        subprocess.run(f'sudo usermod -aG sudo {user_input_new_user}', text=True, shell=True)

    user_iput_disable_root_login = input('>>>Disable root login?(y/n): ') # Disable SSH root login.
    if user_iput_disable_root_login.lower() == 'y':  #!! this thing is re-writing sshd_config again. Maybe merge with port changing part?
        with open('/etc/ssh/sshd_config', 'r') as ssh_config: 
            ssh_text = ssh_config.read() #converts the thing to string
            new_text = ssh_text.replace('PermitRootLogin yes', 'PermitRootLogin no')  
            
        with open('/etc/ssh/sshd_config', 'w') as ssh_config:
            ssh_config.write(new_text)

    return user_input_ssh_port

if __name__ == "__main__":
    main()
