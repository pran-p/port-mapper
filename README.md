# P0rt M4pp3r: 4 simpl3 p0rt sc4nn3r t00l...
This is a simple port scanning script that can be used to scanning for open ports on a given IP address. It uses the simple concept of socket programming.

### Functionalities of this script
This script provides three functionalities currently
+ Check if a given port of a given ip is open
+ Check for open ports in a list of given ports of a ip
+ Check for open ports in a range of given ports of given ip addresses (can be one or more)

### How to get this up and running?
First clone this repo.
```bash
virtualenv ENV_NAME
source ENV_NAME/bin/activate
pip3 install requirements.txt
python3 script.py -h
```
Once the above instructions are completed you will have a help screen something like the one below displayed.

```console
___  ____ ____ ___    _  _ ____ ___  ___  ____ ____ 
|__] |  | |__/  |     |\/| |__| |__] |__] |___ |__/ 
|    |__| |  \  |     |  | |  | |    |    |___ |  \ 
                                                    


P0rt M4pp3r: 4 simpl3 p0rt sc4nn3r t00l...
F1nds 0p3n p0rts

usage: script.py [-h] [-s port ip] [-m port1,port2,... ip]
                 [-r start-port end-port ip1,ip2,...]

P0rt M4pp3r: 4 simpl3 p0rt sc4nn3r t00l...

optional arguments:
  -h, --help            show this help message and exit
  -s port ip, --simple port ip
                        enter the port number followed by the ip of the system
                        for port scan
  -m port1,port2,... ip, --multiple port1,port2,... ip
                        enter the list of port number separated by comma and
                        the ip of the system for port scan
  -r start-port end-port ip1,ip2,..., --range start-port end-port ip1,ip2,...
                        enter the start port and the end port range and the ip
                        of the system for port scan

```

#### Usecase 1
We need to enter a port number and the ip address.  
Command to hit.
```bash
python3 script.py -s 22 localhost
```
Result.
```console

___  ____ ____ ___    _  _ ____ ___  ___  ____ ____ 
|__] |  | |__/  |     |\/| |__| |__] |__] |___ |__/ 
|    |__| |  \  |     |  | |  | |    |    |___ |  \ 
                                                    


P0rt M4pp3r: 4 simpl3 p0rt sc4nn3r t00l...
F1nds 0p3n p0rts

[+] 4tt3mpting t0 c0nn3ct t0 localhost:22
    [.] Port open: 22


```

#### Usecase 2
We need to enter a list of port numbers and the ip address  
Command to hit.
```bash
python3 script.py -m 22,80 localhost
```
Result
```console
___  ____ ____ ___    _  _ ____ ___  ___  ____ ____ 
|__] |  | |__/  |     |\/| |__| |__] |__] |___ |__/ 
|    |__| |  \  |     |  | |  | |    |    |___ |  \ 
                                                    


P0rt M4pp3r: 4 simpl3 p0rt sc4nn3r t00l...
F1nds 0p3n p0rts

[+] 4tt3mpting t0 c0nn3ct t0 localhost:22
    [.] Port open: 22
[+] 4tt3mpting t0 c0nn3ct t0 localhost:80

The open ports are: [('22', 'localhost')]


```

#### Usecase 3
We need to enter a lower and higher limit for the port number and a list of ip address  
Command to hit.
```bash
python3 script.py -r 10 25 localhost
```
Result
```console
___  ____ ____ ___    _  _ ____ ___  ___  ____ ____ 
|__] |  | |__/  |     |\/| |__| |__] |__] |___ |__/ 
|    |__| |  \  |     |  | |  | |    |    |___ |  \ 
                                                    


P0rt M4pp3r: 4 simpl3 p0rt sc4nn3r t00l...
F1nds 0p3n p0rts

[+] 4tt3mpting t0 c0nn3ct t0 localhost:10
[+] 4tt3mpting t0 c0nn3ct t0 localhost:11
[+] 4tt3mpting t0 c0nn3ct t0 localhost:12
[+] 4tt3mpting t0 c0nn3ct t0 localhost:13
[+] 4tt3mpting t0 c0nn3ct t0 localhost:14
[+] 4tt3mpting t0 c0nn3ct t0 localhost:15
[+] 4tt3mpting t0 c0nn3ct t0 localhost:16
[+] 4tt3mpting t0 c0nn3ct t0 localhost:17
[+] 4tt3mpting t0 c0nn3ct t0 localhost:18
[+] 4tt3mpting t0 c0nn3ct t0 localhost:19
[+] 4tt3mpting t0 c0nn3ct t0 localhost:20
[+] 4tt3mpting t0 c0nn3ct t0 localhost:21
[+] 4tt3mpting t0 c0nn3ct t0 localhost:22
    [.] Port open: 22
[+] 4tt3mpting t0 c0nn3ct t0 localhost:23
[+] 4tt3mpting t0 c0nn3ct t0 localhost:24
[+] 4tt3mpting t0 c0nn3ct t0 localhost:25

The open ports are: [(22, 'localhost')]
```





 
