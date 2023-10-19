import struct

'''

Example Problem:
Network byte order (equivalent to big endianess) is used for multi-byte data in UDP headers. 
Suppose the first 4 bytes of a UDP segment is B01E5467, and the bytes after the first 8 bytes are 1911E9EB2483. 
What is the source port number (in decimal), destination port number (in decimal) and the 5th to 8th byte (in hexadecimal, use capital letters, no leading "0x") of this segment? 
Assume the checksum calculation is only based on the UDP segment (which is not the case in reality). 
Provide the answers in the given order and separate them with comma.


'''

def get_checksum_and_length(src_port:int, dst_port:int , payload:str) -> tuple:
  
  # Data or payload (hexadecimal representation)
  data = bytes.fromhex(payload)
  
  # Calculate the UDP length (header + data length)
  udp_length = len(data) + 8  # UDP header is 8 bytes
  
  # Create the UDP header (in network byte order)
  udp_header = struct.pack('!HHHH', src_port, dst_port, udp_length, 0) # Initialize checksum field to 0
  
  # Combine UDP header and data
  packet = udp_header + data
  
  # Calculate the checksum
  checksum = 0
  
  # Calculate the checksum for the entire packet (header + data)
  for i in range(0, len(packet), 2):
      checksum += (packet[i] << 8) + packet[i + 1]
  
  while checksum > 0xFFFF:
      checksum = (checksum & 0xFFFF) + (checksum >> 16)
  
  checksum = ~checksum & 0xFFFF  # Take one's complement
  
  # Store the checksum in the UDP header
  udp_header_with_checksum = struct.pack('!HHHH', src_port, dst_port, udp_length, checksum)
  
  # Print the calculated checksum in hexadecimal form 
  print(f"UDP Checksum: 0x{checksum:04X} | UDP length: {udp_length}")
  return hex(checksum), hex(udp_length)

   
def main() -> None:
   first_bytes = input("Enter your first 4 bytes UDP Segment: ")
   bytes_after_first = input("Enter your bytes after the first 8 bytes: ") #payload

   #parsing the bytes code that was entered
   source_port_num = int(first_bytes[0:4], 16)
   destination_port_num = int(first_bytes[4:], 16)


   #getting the checksum and length by calling the function
   checksum, udp_length = get_checksum_and_length(source_port_num, destination_port_num, bytes_after_first)
   fifth_to_eigth_byte = f"{udp_length[2:]}{checksum[2:]}"

   if len(fifth_to_eigth_byte) < 8:
      fifth_to_eigth_byte = f"{('0' * (8 - len(fifth_to_eigth_byte)))}{fifth_to_eigth_byte}"
    
   #print the results, in the order of source port number, destination port number, 5th to 8th byte and make the color green
   print("The answers will be printed in the order of source port number, destination port number, 5th to 8th byte")

   print(f"\033[32m{source_port_num},{destination_port_num},{fifth_to_eigth_byte}\033[0m")

if __name__ == "__main__":
   main()
