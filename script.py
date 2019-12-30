"""This is a simple version of a port scanner built using the concept of sockets in python"""
import socket
import sys
import argparse

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

def main():
    parser=argparse.ArgumentParser(description="P0rt M4pp3r: A simple port scanner tool...")
    parser.add_argument('--options',dest='options',help='1-single port ip, 2-multiple port on single ip, 3-range of ports on multiple ip ',type=int, metavar='opt', required=True )
    parser.add_argument('-p','--port',dest='port',help='port number(comma separated in case of multiple). use in case of option 1,2', metavar='port')
    parser.add_argument('-ip','--ip-address',dest='ip',help='ip address(comma separeted in case of multiple). use in case of option 1,2,3', metavar='ip')
    parser.add_argument('-lp','--lower-range',dest='ll',help='lower port limit. use in case of option 3', metavar='port', type=int)
    parser.add_argument('-hp','--higher-range',dest='hl',help='higher port limit. use in case of option 3', metavar='port', type=int)
    args=parser.parse_args()
    if args.options==1:
        ans=portScanSingle(args.port,args.ip)
        if ans==0:
            print("Th3 p0rt is cl0s3d...")
    elif args.options==2:
        p=args.port.split(',')
        ans=portScanSingleIp(p,args.ip)
        print("The open ports are:",ans)
    elif args.options==3:
        address=args.ip.split(',')
        if args.hl>65535:
            print("Out of limit")
        else:
            ans=portScanner(args.ll,args.hl, address)
        print("The open ports are:",ans)
    else:
        print("Invalid option")











    # scriptName=sys.argv[0]
    # lowerRange=int(sys.argv[1])
    # higherRange=int(sys.argv[2])
    # ip=sys.argv[3].split(",")
    # print ("[+] Script name: "+str(scriptName))
    # print("[+] Lower range is:"+str(lowerRange))
    # print("[+] Higher Range is:"+str(higherRange))
    # openPort=portScanner(lowerRange, higherRange, ip)
    # des="+"*100
    # print(des)
    # print("Summary")
    # print("Open ports are:", openPort)
    # print(des)
if __name__ == '__main__':
    main()
