import subprocess
import sys


def main():
    #checks if docker is installed, prompt the user to install if necessary
    def is_docker():

        docker_check = subprocess.run('docker -v', shell=True, text=True, capture_output=True)
        user_prompt = ''
        if 'Docker' not in docker_check.stdout[:7]:
            
            while user_prompt.lower() not in ['y','n']:
                user_prompt = input('Docker is not installed on this machine, but is required for this script to run. Do you want to install Docker? [y/n]: ')

            if user_prompt in ['n','N']:
                print("No Docker no script. Exiting the program. \n")
                sys.exit()
        else:
            print('Docker is detected. Intalling Outline server... \n')

        return 0

    #installs docker and outline server
    def run_outline_install():
        outline_install_script = 'sudo bash -c \"$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)\"'
        user_prompt = 'y\n' #gotta be careful with this, because in case of a accidentall repeated execution - it nukes the 'watch tower' docker and reconfigures the server completely. So for now the script is in 'clean install mode' only. 
        installation_result = subprocess.run(outline_install_script, shell=True,  capture_output=True, text=True, input=user_prompt)
        
        print('Server is intalled. Or not. I haven\'t written any tests yet, so you have to believe me. Now parsing output data... \n')
        return installation_result.stdout

    #parses the output for server key and ports
    # def parse_script_result(output: str) -> dict:
        
    #     script_data = {}
    #     lines = output.splitlines()
        
    #     for line in lines:
    #         if '{' in line:
    #             script_data['vpn_key'] = line[7:-4] #test this out, getting rid of ANSI 
    #         elif 'Management' in line:
    #             grab_numbers = line.split(' ')
    #             script_data['management_port'] = grab_numbers[3] #hardcoded because output seems to be static and !Management! port number always has index = 3
    #         elif 'Access' in line:
    #             grab_numbers = line.split(' ')
    #             script_data['access_port'] = grab_numbers[4] #hardcoded because output seems to be static and !Access! port number always has index = 4
    #     print('Here is your server data! Make sure to copy the VPN key into Outline Manager. Proceeding with port configuration... \n')
    #     return script_data


    is_docker() 

    output = run_outline_install()

    return output

def parse_script_result(output: str) -> dict:
    
    script_data = {}
    lines = output.splitlines()
    
    for line in lines:
        if '{' in line:
            script_data['vpn_key'] = line[7:-4] #test this out, getting rid of ANSI 
        elif 'Management' in line:
            grab_numbers = line.split(' ')
            script_data['management_port'] = grab_numbers[3] #hardcoded because output seems to be static and !Management! port number always has index = 3
        elif 'Access' in line:
            grab_numbers = line.split(' ')
            script_data['access_port'] = grab_numbers[4] #hardcoded because output seems to be static and !Access! port number always has index = 4
    print('Here is your server data! Make sure to copy the VPN key into Outline Manager. Proceeding with port configuration... \n')
    return script_data

if __name__ == "__main__":
   output = main()
   parse_script_result(output)


# def get_parsed_data(): what is this 
#     return main()



