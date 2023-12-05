Ethernet_Bus = 100 * 10**6 #Enter in Mbps
Propogation_Delay = 180
Byte_Frame = 1450 * 8
t = 0

#Works for Ethernet Bus = 100 Mbps

#Part A
print(Propogation_Delay)

#Part B
Time = t #A and B start transmitting
Time += Propogation_Delay #Detect Collision
Time += 48 #A and B Jam Signal
Time2 = Time
Time += Propogation_Delay #B's last jam signal at A, A detects idle channel
Time += (96) #A starts retransmission, channels needs to be idle for 96 bit times before B can retransmit. Now, if B senses signal on or before Time2 + 512 + 96, it will not retransmit
print(Time)

#Part C
Time += Propogation_Delay #A's retransmission signals reaches B
if Time < Time2 + 512 + 96:
  Time += Byte_Frame #B detects idle channel after A retransmission signal arrives at B
  Time += 96 #B behind transmission
  print(Time)

else:
  print(Time) #B behind transmission