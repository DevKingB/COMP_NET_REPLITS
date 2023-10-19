'''
Consider an Internet path over which data can be transmitted at a rate of 5 megabits/sec in both directions. The path include 3 links and 2 routers. 
Each link is 3000 kilometers long. Signal propagates over the links at a speed of 2 × 108 meters per second. 
A HTTP client at one end of the path downloads a web page and the web objects referenced within the page from a HTTP server at the other end of the path. 
Suppose the web page size is 29 kilobytes, 18 images are embedded in the web page and each of them is 190 kilobytes. 
Consider transmission delay and propagation delay only. The web page and images are stored on the same web server. 
Assume TCP connection requests/responses and HTTP requests are small enough for their transmission delay to be ignored. 
The maximum packet size is 1 kilobytes. Ignore header size.

How long is the RTT?
For non-persistant HTTP,
    - How much time elapses from the beginning to when the first packet arrives at the router connected to the HTTP server?
    - How much time elapses from the beginning to when the first packet arrives at the router two hops away from the server?
    - How much time elapses from the beginning to when the HTTP client receives the first packet?
    - How much time elapses from the beginning to when the HTTP client receives the whole web page?
For non-persistant HTTP using a single TCP connection at any time, how much time elapses from the beginning to when the HTTP client receives the first image?
For non-persistant HTTP using a single TCP connection at any time, how much time elapses from the beginning to when the web page can be displayed (i.e. when the HTTP client receives the web page and all the images)?
For non-persistant HTTP using multiple TCP connections simultaneously, how much time elapses from the beginning to when the web page can be displayed?
For persistant HTTP, how much time elapses from the beginning to when the web page can be displayed?
The answers must be in seconds and rounded to the nearest thousandth. Separate them with commas.


'''

def find_http(transmission_rate, number_of_links, number_of_routers, length_of_link, signal_propagation_speed, webpage_size, number_of_images, image_size, max_pkt_size):
    # How long is the RTT?
    total_length_of_links = number_of_links * length_of_link
    propagation_delay = total_length_of_links / signal_propagation_speed
    RTT = propagation_delay * 2
    print("RTT ", round(RTT, 3))

    # For non-persistent HTTP:
    # How much time elapses from the beginning to when the first packet arrives at the router connected to the HTTP server?
    time_for_tcp_connection = RTT
    time_for_request = time_for_tcp_connection / 2
    first_transmission_delay = max_pkt_size / transmission_rate
    first_propagation_delay_till_router = length_of_link / signal_propagation_speed
    travel_time = time_for_tcp_connection + time_for_request + first_transmission_delay + first_propagation_delay_till_router
    print("time for first packet to arrive ", round(travel_time, 3))

    # How much time elapses from the beginning to when the first packet arrives at the router two hops away from the server?
    time_till_one_hop_away = travel_time
    second_transmission_delay = max_pkt_size / transmission_rate
    second_propagation_delay_till_router = length_of_link / signal_propagation_speed
    extra_time = second_propagation_delay_till_router + second_transmission_delay
    total_time_two_hops = extra_time + time_till_one_hop_away
    print("time two hops ", round(total_time_two_hops, 3))

    # How much time elapses from the beginning to when the HTTP client receives the first packet?
    time_for_tcp_connection = RTT
    time_for_request = time_for_tcp_connection / 2
    propagation_delay = number_of_links * (length_of_link / signal_propagation_speed)
    transmission_delay_for_first_packet = (number_of_routers + 1) * (max_pkt_size / transmission_rate)
    total_time_first_pkt = time_for_tcp_connection + time_for_request + propagation_delay + transmission_delay_for_first_packet
    print("total time first pkt ", round(total_time_first_pkt, 3))

    # How much time elapses from the beginning to when the HTTP client receives the whole web page?
    time_for_tcp_connection = RTT
    time_for_request = time_for_tcp_connection / 2
    propagation_delay = number_of_links * (length_of_link /
    signal_propagation_speed)
    num_packets_of_max_size = webpage_size // max_pkt_size
    transmission_delay_for_packets_of_max_size = (num_packets_of_max_size + number_of_routers) * (max_pkt_size /
    transmission_rate)

    num_packets_of_rem_bytes = webpage_size % max_pkt_size
    transmission_delay_for_rem_bytes = num_packets_of_rem_bytes / transmission_rate

    total_time_webpage = time_for_tcp_connection + time_for_request + propagation_delay + transmission_delay_for_packets_of_max_size + transmission_delay_for_rem_bytes
    print("time to receive whole webpage", round(total_time_webpage, 3))

    # For non-persistant HTTP using a single TCP connection at any time, how much time elapses from the beginning to when the HTTP client receives the first image?
    time_to_get_webpage = total_time_webpage
    time_for_tcp_connection = RTT
    time_for_request = time_for_tcp_connection / 2
    propagation_delay = number_of_links * (length_of_link /
    signal_propagation_speed)

    num_packets_for_images_of_max_size = image_size // max_pkt_size
    transmission_delay = (num_packets_for_images_of_max_size + number_of_routers) * (max_pkt_size / transmission_rate)
    num_packets_of_rem_bytes = image_size % max_pkt_size
    transmission_delay_for_rem_bytes = num_packets_of_rem_bytes / transmission_rate
    time_to_receive_first_image = time_for_tcp_connection + time_for_request + propagation_delay + transmission_delay + transmission_delay_for_rem_bytes
    total_time_for_first_image = time_to_receive_first_image + time_to_get_webpage
    print("total time for first image ", round(total_time_for_first_image, 3))

    # For non-persistant HTTP using a single TCP connection at any time, how much time elapses from the beginning to when the web page can be displayed (i.e. when the HTTP client receives the web page and all the images)?
    time_to_get_webpage = total_time_webpage
    time_for_tcp_connection = RTT
    time_for_request = time_for_tcp_connection / 2
    propagation_delay = number_of_links * (length_of_link / signal_propagation_speed)
    number_of_pkts = image_size // max_pkt_size
    transmission_delay = (number_of_pkts + number_of_routers) * (
    max_pkt_size / transmission_rate)
    num_packets_of_rem_bytes = image_size % max_pkt_size
    transmission_delay_for_rem_bytes = num_packets_of_rem_bytes / transmission_rate
    time_to_get_all_images = (time_for_tcp_connection + time_for_request + propagation_delay +
    transmission_delay +
    transmission_delay_for_rem_bytes) * number_of_images
    time_client_receives_webpage = time_to_get_webpage + time_to_get_all_images
    print("time elapsed for client to receive webpage/images ", round(time_client_receives_webpage, 3))

    # For non-persistant HTTP using multiple TCP connections simultaneously, how much time elapses from the beginning to when the web page can be displayed?
    time_to_get_webpage = total_time_webpage
    time_for_tcp_connection = RTT
    time_for_request = time_for_tcp_connection / 2
    propagation_delay = number_of_links * (length_of_link / signal_propagation_speed)
    total_packets_formed_from_all_images_of_max_size = (image_size * number_of_images) // max_pkt_size
    total_transmission_delay = (total_packets_formed_from_all_images_of_max_size + number_of_routers) * (max_pkt_size / transmission_rate)
    packets_formed_of_less_than_max_size = (image_size * number_of_images) % max_pkt_size
    transmission_delay_for_packets_formed_of_less_than_max_size = packets_formed_of_less_than_max_size / transmission_rate
    time_to_receive_all_images_simultaneously = time_for_tcp_connection + time_for_request + propagation_delay + total_transmission_delay + transmission_delay_for_packets_formed_of_less_than_max_size
    time_elapsed_to_display_webpage = time_to_get_webpage + time_to_receive_all_images_simultaneously
    print("time elapsed for webpage display ", round(time_elapsed_to_display_webpage, 3))

    # For persistant HTTP, how much time elapses from the beginning to when the web page can be displayed?
    time_to_get_webpage = total_time_webpage
    time_for_tcp_connection = RTT
    time_for_request = time_for_tcp_connection / 2
    propagation_delay = number_of_links * (length_of_link / signal_propagation_speed)
    total_packets_formed_from_all_images_of_max_size = (
    image_size * number_of_images) // max_pkt_size
    total_transmission_delay = (total_packets_formed_from_all_images_of_max_size + number_of_routers) * (max_pkt_size / transmission_rate)
    packets_formed_of_less_than_max_size = (image_size * number_of_images) % max_pkt_size
    transmission_delay_for_packets_formed_of_less_than_max_size = packets_formed_of_less_than_max_size / transmission_rate
    time_to_receive_all_images_simultaneously = time_for_request + propagation_delay + total_transmission_delay + transmission_delay_for_packets_formed_of_less_than_max_size
    time_to_display_webpage = time_to_get_webpage + time_to_receive_all_images_simultaneously
    print("webpage display time ", round(time_to_display_webpage, 3))
    print("\n If the numbers does not match up to the rounded place, it is because of the rounding error. Just add a 0 to the number.")
    print(f"Here is you final answer: \033[32m{round(RTT, 3)},{round(travel_time, 3)},{round(total_time_two_hops, 3)},{round(total_time_first_pkt, 3)},{round(total_time_webpage, 3)},{round(total_time_for_first_image, 3)},{round(time_client_receives_webpage, 3)},{round(time_elapsed_to_display_webpage, 3)},{round(time_to_display_webpage, 3)}\033[0m")



if __name__ == "__main__":
    transmission_rate = float(input("Enter the transmission rate in megabits per second: ")) * 10**6
    number_of_links = int(input("Enter the number of links: "))
    number_of_routers = int(input("Enter the number of routers: "))
    length_of_link = float(input("Enter the length of link in kilometers: ")) * 10**3
    signal_propagation_speed = float(input("Enter the signal propagation speed in meters per second: ")) * 10**8
    webpage_size = float(input("Enter the webpage size in kilobytes: ")) * 8 * 10**3
    number_of_images = int(input("Enter the number of images: "))
    image_size = float(input("Enter the image size in kilobytes: ")) * 8 * 10**3
    max_pkt_size = float(input("Enter the maximum packet size in kilobytes: ")) * 8 * 10**3

    find_http(transmission_rate, number_of_links, number_of_routers, length_of_link, signal_propagation_speed, webpage_size, number_of_images, image_size, max_pkt_size)
