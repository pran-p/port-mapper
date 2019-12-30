"""This is a simple version of a port scanner built using the concept of sockets in python"""
import socket
import sys
def portScanner(lowerRange, higherRange,ip):
    a=[]
    for i in range(lowerRange,higherRange+1):
        try:
            # pass
            print ("[+] 4tt3mpting t0 c0nn3ct t0 "+ str(ip)+":"+str(i))
            s=socket.socket()
            # print(ip,i)
            s.connect((ip,i))
            banner=s.recv(1024)
            if banner:
                print ("    [-] Port"+str(i)+" open:"+str(banner.decode()))
                a.append((banner,i))
            s.close()

        except :
            pass
    return a
def main():
    scriptName=sys.argv[0]
    lowerRange=int(sys.argv[1])
    higherRange=int(sys.argv[2])
    ip=sys.argv[3]
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
