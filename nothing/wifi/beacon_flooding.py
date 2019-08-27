from scapy.all import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a simpe packet sniffer using scapy')
    parser.add_argument('-i', type=str, required=True, metavar='NIC', help='NIC name')
    parser.add_argument('-s', type=str, required=True, metavar='SSID', help='SSID of Beacon Frame')
    parser.add_argument('-b', type=str, metavar='BSSID', help='BSSID of Beacon Frame')
    args = parser.parse_args()

    iface = args.i
    ssid = args.s

    dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2='22:22:22:22:22:22', addr3='33:33:33:33:33:33')
    beacon = Dot11Beacon(cap='ESS+privacy')
    essid = Dot11Elt(ID='SSID', info=ssid, len=len(ssid))
    rsn = Dot11Elt(ID='RSNinfo', info=(
        '\x01\x00'  # RSN Version 1
        '\x00\x0f\xac\x02'  # Group Cipher Suite : 00-0f-ac TKIP
        '\x02\x00'  # 2 Pairwise Cipher Suites (next two lines)
        '\x00\x0f\xac\x04'  # AES Cipher
        '\x00\x0f\xac\x02'  # TKIP Cipher
        '\x01\x00'  # 1 Authentication Key Managment Suite (line below)
        '\x00\x0f\xac\x02'  # Pre-Shared Key
        '\x00\x00'))  # RSN Capabilities (no extra capabilities)

    frame = RadioTap() / dot11 / beacon / essid / rsn
    frame.show()

    sendp(frame, iface=iface, inter=0.100, loop=1, verbose=0)
