user_input = input('Hello, please choose the option: \n 1)Configure host \n 2)Configure iptables \n 3)Install Outline Server\n 4)Full set up(recommended) \nEnter a number: ')

if user_input == 1:
    import host_conf
elif user_input == 2:
    from iptables_conf import iptables_conf.main()
elif user_input == 3:
    import outline_install
elif user_input == 4:
    import host_conf
    import outline_install
    import iptables_conf
# else:
#     print('No option like that')

# if name main? 