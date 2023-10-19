##########Chapter 1  - Part 2 ##########
"""In a packet-switched network (end to end)"""
"""Change these values for your question"""
packet_size = 1800
propagation_speed = 1.8 * 10**8
link_1_transmission_rate = 160
link_2_transmission_rate = 120
router_processing = 3
link_1_length = 1100
link_2_length = 1700 

# packet_size = 500
# propagation_speed = 1.8 * 10**8
# link_1_transmission_rate = 170
# link_2_transmission_rate = 120
# router_processing = 5
# link_1_length = 1100
# link_2_length = 1800 

# 6137.1,16170.5,16180.3,16190.1,17141.1

# Transmission delay for 1st link
link_1_transmission_delay = (packet_size * 8) / (link_1_transmission_rate * 10**6) # in microseconds

# Propagation delay for 1st link
link_1_propagation_delay = (link_1_length * 1000) / (propagation_speed) # in microseconds

# Transmission delay for 2nd link
link_2_transmission_delay = (packet_size * 8) / (link_2_transmission_rate * 10**6)

# Propagation delay for 2nd link
link_2_propagation_delay = (link_2_length * 10**3) / (propagation_speed)

# Router processing delay
router_processing_delay = (packet_size / 1000) * (router_processing * 10**-6)

# Total delay from source to router of 1st packet
total_delay_src_to_rout = link_1_transmission_delay + router_processing_delay + link_1_propagation_delay

# Total delay from source to destination of 1st packet
total_delay_src_to_dest = link_1_transmission_delay + link_1_propagation_delay + router_processing_delay + link_2_transmission_delay + link_2_propagation_delay

# Packet delay
packet_delay = link_2_transmission_delay - link_1_transmission_delay

# Formula for packet delay
n = 0
packet_n_delay = total_delay_src_to_dest + ((n - 1) * packet_delay)

# End-to-end delay of 1st packet
packet_1_delay = total_delay_src_to_dest + ((1 - 1) * packet_delay)

# End-to-end delay of 2nd packet
packet_2_delay = total_delay_src_to_dest + ((2 - 1) * packet_delay)

# End-to-end delay of 3rd packet
packet_3_delay = total_delay_src_to_dest + ((3 - 1) * packet_delay)

# End-to-end delay of 100th packet
packet_100_delay = total_delay_src_to_dest + ((100 - 1) * packet_delay)

# Print solutions
print(f"Total delay from source to router of 1st packet {round(total_delay_src_to_rout * 10**6, 1)} microseconds\n")
print(f"End-to-end delay of 1st packet: {round(packet_1_delay * 10**6, 1)} microseconds\n")
print(f"End-to-end delay of 2nd packet: {round(packet_2_delay * 10**6, 1)} microseconds\n")
print(f"End-to-end delay of 3rd packet: {round(packet_3_delay * 10**6, 1)} microseconds\n")
print(f"End-to-end delay of 100th packet: {round(packet_100_delay * 10**6, 1)} microseconds\n")