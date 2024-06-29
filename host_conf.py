import subprocess

def main(): 
    subprocess.run('sudo apt install curl', text=True, shell='True')
    print()


if __name__ == "__main__":
    main()
