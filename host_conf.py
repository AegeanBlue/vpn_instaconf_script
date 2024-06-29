import subprocess

def main(): 
    subprocess.run('sudo apt install curl', text=True, shell='True')


if __name__ == "__main__":
    main()
