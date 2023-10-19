'''
Bandwidth = 0.9 * 10 ** 9
Propogation_Speed = 2 * 10 ** 8
Packet_Size = 1300 * 8
Window_Size = 400
Channel_Utilization = 50 * 0.01 #Percentage

Time_to_send_Packet = Packet_Size / Bandwidth

Min_RTT = ((Window_Size * Time_to_send_Packet) / Channel_Utilization) - Time_to_send_Packet

Min_Length = Min_RTT * Propogation_Speed / 2
Min_Length /= 1000 #To Km
print(Min_Length)

'''

def find_min_length(bandwith, speed, packet_size, window_size, channel_utilization):
    
    #handles the conversion for each variable below
    bandwith = bandwith * 10 ** 9
    speed = speed * 10 ** 8
    packet_size = packet_size * 8
    channel_utilization = channel_utilization * 0.01
    
    #perform the actual calculations for the problem
    time_to_send_packet = packet_size / bandwith
    min_rtt = ((window_size * time_to_send_packet) / channel_utilization) - time_to_send_packet
    min_length = min_rtt * speed / 2
    min_length /= 1000
    return min_length


if __name__ == "__main__":
    bandwith = float(input("Enter the bandwidth: "))
    propogation_speed = float(input("Enter the propogation speed in meters per second(not the 10 ** 8): "))
    packet_size = float(input("Enter the packet size in bits: "))
    window_size = float(input("Enter the window size in packets: "))
    channel_utilization = float(input("Enter the channel utilization: "))
    print("Your answer is below:")
    print(f"\033[32m{round(find_min_length(bandwith, propogation_speed, packet_size, window_size, channel_utilization),1)}\033[0m")