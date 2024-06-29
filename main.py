import host_conf
import outline_install
import iptables_conf


user_input = input('Hello, please choose the option: \n 1)Configure host \n 2)Configure iptables \n 3)Install Outline Server\n 4)Full set up(recommended) \nEnter a number: ')

if user_input == '1':
    host_conf.main()
elif user_input == '2':
    iptables_conf.main()
elif user_input == '3':
    outline_install.main()
elif user_input == "4":
    host_conf.main()
    parsed_data = outline_install.main()
    iptables_conf.main()

