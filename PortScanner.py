from socket import *

if __name__ == '__main__':
    print("PORT SCANNER V 1.0 (simple port scanner)")
    target = input('Enter host to scan: ')
    targetIP = gethostbyname(target)
    print ('Starting scan on host ', targetIP)

    #scan reserved ports
    portstoscann = [21, 22, 53, 25, 443, 110, 143, 80, 546, 547, 1080, 156]
    for i in portstoscann:
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print ('Port %d: OPEN' % (i,))
        else:
            print('Port %d: CLOSED' % (i,))
        s.close()