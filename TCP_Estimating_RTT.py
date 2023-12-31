Current_RTT = 48
Current_DEV = 2
TRANS_1 = 9
TRANS_2 = 25
TRANS_3 = 38
TRANS_4 = 53
TRANS_5 = 66
ACK_1 = 60
ACK_2 = 82
ACK_3 = 105
ACK_4 = 108 #Repeat

RTT_1 = ACK_1 - TRANS_1 #1 seg
RTT_2 = ACK_2 - TRANS_3 #3 seg
RTT_3 = ACK_3 - TRANS_4 #4 seg
#2nd segment can't be used because retransmission

ERT_0 = Current_RTT
ERT_1 = (1-0.125)*ERT_0 + 0.125 * RTT_1
ERT_2 = (1-0.125)*ERT_1 + 0.125 * RTT_2
ERT_3 = (1-0.125)*ERT_2 + 0.125 * RTT_3

DEV_0 = Current_DEV
DEV_1 = (1-0.25)*DEV_0 + 0.25 * abs(RTT_1 - ERT_1)
DEV_2 = (1-0.25)*DEV_1 + 0.25 * abs(RTT_2 - ERT_2)
DEV_3 = (1-0.25)*DEV_2 + 0.25 * abs(RTT_3 - ERT_3)

print(ERT_1 + 4 * DEV_1)
print(ERT_2 + 4 * DEV_2)
print("This is answer 5: ", (ERT_3 + 4 * DEV_3))#5

print("THIS IS EVERYTHING INDIVDUAL(DEV -> ERT)")
print("This is answer 2: ", DEV_1)#2
print(DEV_2)
print("This is answer 4: ", DEV_3)#4
print("This is answer1:", ERT_1)#maybe #1
print(ERT_2)
print("This is answer 3: ", ERT_3)#3


print("All ERTs:", (ERT_1 + ERT_2 + ERT_3))
print("All DEVs: ", (DEV_1 + DEV_2 + DEV_3))
print("All RTTs: ", (RTT_1 + RTT_2 + RTT_3))