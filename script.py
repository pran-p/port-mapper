"""This is a simple version of a port scanner built using the concept of sockets in python"""
import socket
import sys
import argparse
import pyfiglet
import os

"""This function is used to scan a given ip for a given open port"""
def portScanSingle(port,ip):
    s=socket.socket()
    try:
        print ("[+] 4tt3mpting t0 c0nn3ct t0 "+ str(ip)+":"+str(port))
        s.connect((ip,int(port)))
        print ("    [.] Port open: "+str(port))
        s.close()
        return 1
    except:
        s.close()
    return 0


"""This function is used to scan for all the given ports of a specific ip"""
def portScanSingleIp(port,ip):
    a=[]
    for i in port:
        try:
            test=portScanSingle(i,ip)
            if test==1:
                a.append((i,ip))
        except:
            pass
    return a

"""This function is used to scan for all the ports from a lower ip range to higher range of all the hosts(a python list)"""
def portScanner(lowerRange, higherRange,hosts):
    a=[]
    for ip in hosts:
        for i in range(lowerRange,higherRange+1):
            try:
                # pass
                test=portScanSingle(i,ip)
                if test==1:
                    a.append((i,ip))
            except :
                pass
    return a

"""This function is used to scan specific port of a list of IPs"""
def portScanPortIp(port,ip):
    b=[]
    for i in ip:
        try:
            a=portScanSingleIp(i,ip)
            if len(a):
                b.append(a)
        except:
            pass
    return b

"""This is the driver code"""
def main():
    os.system('tput clear')
    f=pyfiglet.Figlet(font='cybermedium')
    print(f.renderText('Port Mapper'))
    print ('\033[1m')
    print("P0rt M4pp3r: 4 simpl3 p0rt sc4nn3r t00l...")
    print ('\033[0m')
    parser=argparse.ArgumentParser(description="P0rt M4pp3r: 4 simpl3 p0rt sc4nn3r t00l...")
    parser.add_argument('-s','--simple', nargs=2, metavar=('port','ip'), help="enter the port number followed by the ip of the system for port scan")
    parser.add_argument('-m','--multiple', nargs=2, metavar=('port1,port2,...','ip'),help='enter the list of port number separated by comma and the ip of the system for port scan')
    parser.add_argument('-r','--range', nargs=3, metavar=('start-port', 'end-port', 'ip1,ip2,...'), help='enter the start port and the end port range and the ip of the system for port scan')
    args=parser.parse_args()
    if args.simple:
        ans=portScanSingle(args.simple[0],args.simple[1])
        if ans==0:
            print("Th3 p0rt is cl0s3d...")
    elif args.multiple:
        p=args.multiple[0].split(',')
        ans=portScanSingleIp(p,args.multiple[1])
        print ('\033[1m')
        print("The open ports are:",ans)
        print ('\033[0m')
    elif args.range:
        address=args.range[2].split(',')
        if int(args.range[1])>65535:
            print("Port out of range")
        else:
            ans=portScanner(int(args.range[0]),int(args.range[1]), address)
        print ('\033[1m')
        print("The open ports are:",ans)
        print ('\033[0m')
    else:
        print("set -h flag to see options")


if __name__ == '__main__':
    main()
