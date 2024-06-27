
*first part*
Would you like to install Docker? This will run \'curl https://get.docker.com/ | sh\'. [Y/n] 

*second part*

CONGRATULATIONS! Your Outline server is up and running.


To manage your Outline server, please copy the following line (including curly brackets) into Step 2 of the Outline Manager interface:


{"apiUrl":"https://178.71.153.78:11129/ag2ILWbNszsrnfwTf8Ko5A","certSha256":"970844C2DCF9C2779B4F09D4BB932D0793A99C98F967AD0F1B09507F5B9392DA"}


You won’t be able to access it externally, despite your server being correctly

set up, because there's a firewall (in this machine, your router or cloud

provider) that is preventing incoming connections to ports 11129 and 18150.

Make sure to open the following ports on your firewall, router or cloud provider:

- Management port 11129, for TCP

- Access key port 18150, for TCP and UDP

1) fin the line that starts with { and take all its contets

2) find lines that start with -

first is managementp TCP port

second is access udp tcp port



