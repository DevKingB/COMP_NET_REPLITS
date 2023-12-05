from itertools import permutations

'''
Example Problem:
The node at the center is a router. The two black boxes around the center node are switches. A datagram is sent from Interface A to Interface F, and then a datagram is sent from Interface F to Interface E. Assume all ARP and switching tables are empty initially. For each of the frames received by Interface E (including those not destined for E), show the source and destination IP address of the datagram carried by the frame as well as the source and destination MAC address of the frame. If the datagram is not an IP datagram, write 0 in place of IP address. For example, "1.2.3.4,2.3.4.5,AA-BB-CC-DD-EE-FF, 
'''

center = "router"
sides = "switches"
msg1_src = "A"
msg1_dst = "F"
msg2_src = "F"
msg2_dst = "E"
observer = "E"

address_table = '''
A	23.115.227.89	08-06-09-47-A0-C1
B	23.115.227.140	1B-3B-4E-A4-20-42
E	167.26.145.70	56-45-1E-26-A2-98
F	167.26.145.240	D1-91-51-4B-D8-96
C	23.115.227.17	76-E0-DC-97-0B-F9
D	167.26.145.15	50-DD-F2-24-3D-A5
'''
network_devices = ('switch', 'router', 'hub')
if not {center, sides}.issubset(network_devices):
  print('center and sides must each be one of:', network_devices)
  quit()

address_table = [line.split('\t') for line in address_table.strip().split('\n')]
MAC = {interface:mac for interface, ip, mac in address_table}
IP = {interface:ip for interface, ip, mac in address_table}
router_interface = {'A':'C','B':'C','E':'D','F':'D'}

seen = set() # one-way interface pairs: knows->known

# Everyone in broadcast domain should know you now, but you don't know them yet.
def arp_query(src, target):  
  res = "0,0,%s,FF-FF-FF-FF-FF-FF" % MAC[src] \
    if (src, target) not in seen and src != observer else None
  seen.update(filter((lambda pair:pair[1]==src), broadcast_domain))
  return res

def arp_resp(src, dst, target):
  # src is the responder.
  # target is the guy that dst originally asked about.
  # dst now knows both src and target.
  res = "0,0,%s,%s" % (MAC[src], MAC[dst]) \
    if (dst, target) not in seen and src != observer else None
  seen.update([(dst, src), (dst, target)])
  return res

ip_data = lambda src, dst, intf1, intf2: \
  "%s,%s,%s,%s" % (IP[src],IP[dst],MAC[intf1],MAC[intf2]) \
  if intf1 != observer else None

# Set of pairs in same domain:
collision_domain = \
  set(permutations('ABEF',2)) if (center, sides) == ('hub', 'hub') else \
  set(permutations('ABC',2)).union(permutations('DEF',2)) if sides == 'hub' else \
  set()
broadcast_domain = \
  set() if (center, sides) == ('router', 'router') else \
  set(permutations('ABC',2)).union(permutations('DEF',2)) if center == 'router' else \
  set(permutations('ABEF',2))

observed = []

for src, dst in [(msg1_src, msg1_dst), (msg2_src, msg2_dst)]:
  if (src, observer) in broadcast_domain:
    observed.append(arp_query(src, target=dst))
  if (src, dst) in broadcast_domain:
    if {(observer, src), (observer, dst)}.intersection(collision_domain):
      observed.append(arp_resp(dst, src, target=dst))
      observed.append(ip_data(src, dst, src, dst))
  else:
    if (observer, src) in collision_domain:
      observed.append(arp_resp(router_interface[src], src, target=dst))
      observed.append(ip_data(src, dst, src, router_interface[src]))
    if (observer, dst) in broadcast_domain:
      observed.append(arp_query(router_interface[dst], target=dst))
    if (observer, dst) in collision_domain:
      observed.append(arp_resp(dst, router_interface[dst], target=dst))
      observed.append(ip_data(src, dst, router_interface[dst], dst))

print('\n'*10,','.join(msg for msg in observed if msg))
