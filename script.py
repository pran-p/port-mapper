"""This is a simple version of a port scanner built using the concept of sockets in python"""
import socket
import sys
import argparse

"""This function is used to scan a given ip for a given open port"""
def portScanSingle(port,ip):
    s=socket.socket()
    a=[]
    try:
        print ("[+] 4tt3mpting t0 c0nn3ct t0 "+ str(ip)+":"+str(port))
        s.connect((ip,port))
        print ("    [-] Port"+str(i)+" open:")
        a.append((i,ip))
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
                a.append(i,ip)
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
    scriptName=sys.argv[0]
    lowerRange=int(sys.argv[1])
    higherRange=int(sys.argv[2])
    ip=sys.argv[3].split(",")
    print ("[+] Script name: "+str(scriptName))
    print("[+] Lower range is:"+str(lowerRange))
    print("[+] Higher Range is:"+str(higherRange))
    openPort=portScanner(lowerRange, higherRange, ip)
    des="+"*100
    print(des)
    print("Summary")
    print("Open ports are:", openPort)
    print(des)
if __name__ == '__main__':
    main()
