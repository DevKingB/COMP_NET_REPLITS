Number_Nodes = 40
Transmission_Rate = 100 * 10**6 #Enter in Mbps
Token_Size = 1000 * 8 #Enter in bytes
Transmit_Most = 10000 * 8 #Enter in bytes
Effective_Throughput_Rate = 940 * 10**6 #Enter in Mbps

#Part A
Time_Transmit_Token_Node = Token_Size / Transmission_Rate
Time_Data_Transmission_Round = Transmit_Most / Transmission_Rate
Time_Token_Passing = Number_Nodes * Time_Transmit_Token_Node
Throughput_Rate = Transmit_Most / (Time_Data_Transmission_Round + Time_Token_Passing)
print(Throughput_Rate/10**6)

#Part B
Time_Data_Transmission_Round = Transmit_Most * Number_Nodes / Transmission_Rate
Time_Token_Passing = Number_Nodes * Time_Transmit_Token_Node
Throughput_Rate = (Transmit_Most * Number_Nodes) / (Time_Data_Transmission_Round + Time_Token_Passing)
print(Throughput_Rate/10**6)

#Part C
Min_Number_Bytes = (Token_Size/8 * Effective_Throughput_Rate) / (Transmission_Rate - Effective_Throughput_Rate)
print(Min_Number_Bytes)