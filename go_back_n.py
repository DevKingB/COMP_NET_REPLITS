'''
Example Problem: 
A sender and a receiver that implement the Go-Back-N protocol communicate over a network with the RTT as 70 milliseconds. 
The first sequence number is 26, the sending window size is 4, the timeout value is 100 milliseconds. 
The sender sends 9 packets. The packet(s) of the ordinal number 2,9 from the sender are lost, and the packets of the ordinal number 1,2 from the receiver are lost. Assume zero transmission delay and assume that RTT includes all delay. 
When timer expiration and packet arrival occur at the exact same time, timeout is processed first. 
What are the sequence numbers sent by the sender and what are the acknowledgement numbers sent by the receiver? 
Separate the sender's sequence number by comma and separate the receiver's also by comma, and separate the two parts with a semicolon. 
For example, "3,4,5,3,4,5;3,3,3,4,5" without the quotes.


'''

class GoBackN:
  def __init__(self):
    self.rtt = int(input("rtt: "))

    self.beginning = int(input("first sequence number: "))
    self.sending_window = int(input("window sized: "))
    self.timeout = int(input("timeout value: "))
    self.packets_num = int(input("packets amount: "))
    self.sender_lost = input("sender lost: ").split(",")
    self.sender_lost = [int(i) for i in self.sender_lost]
    self.reciever_lost = input("reciever lost: ").split(",")
    self.reciever_lost = [int(i) for i in self.reciever_lost]

    self.curr = 0
    self.send_ind = 1
    self.r_ind = 1
    self.r_exp = self.beginning
    self.count = 0
    self.packets_to_send = [i for i in range(self.beginning, self.beginning+self.packets_num)]
    self.sent_by_sender = []
    self.sent_by_reciever = []
    self.myL = []
    self.i = 0
    self.j = 0

    self.send()
    return

  def send(self, isRepeat = True):
    if self.count >= self.packets_num:
      self.stop()
      return

    tempJ = self.j
    self.j = self.i + self.sending_window
    # print(tempJ, self.j)
    if isRepeat:
      self.packets_window = [i for i in self.packets_to_send[self.i:self.j]]
    else:
      # print("hi", self.packets_window)
      self.packets_window = [i for i in self.packets_to_send[tempJ:self.j]]
    to_send = []
    for i in self.packets_window:
      to_send.append((i, self.send_ind))
      self.send_ind+=1
      self.count+=1

    self.myL.append((self.curr + self.timeout, "timeout", [i[0] for i in to_send]))
    self.sent_by_sender.extend([i[0] for i in to_send])
    # print(self.myL)
    recieved = []
    for i in to_send:
      i_val = i[0]
      i_ind = i[1]
      if i_ind not in self.sender_lost:
        recieved.append(i_val)
    send_back = []
    for i in recieved:
      if i == self.r_exp:
        send_back.append(i)
        self.r_exp += 1
      else:
        send_back.append(self.r_exp-1)


    # print(send_back)
    self.sent_by_reciever.extend(send_back)
    # sending back packets
    coming_back = []
    for i in send_back:
      if self.r_ind not in self.reciever_lost:
        coming_back.append(i)  
      self.r_ind+=1

    stuff = (self.curr+self.rtt+1, "packets", coming_back)
    self.myL.append(stuff)    

    self.myL = sorted(self.myL, key=self.getKey)
    # print(self.myL)

    self.next()
    return


  def next(self):
    first = self.myL.pop(0)
    [self.curr, type1, packets] = first

    if type1 == "timeout":
      self.send()
    elif type1 == "packets":
      self.curr-=1
      changed = False
      for i in packets:
        exp = self.packets_to_send[self.i]
        # print(i, exp)
        if i >= exp:
          # discard Timeout
          self.discardTimeout(i)
          self.i+=i-exp+1
          changed = True
          # print("hia")
      # after something is acknowledged and you increment i and j, you have to add the i and j you incremented
      if changed:
        self.send(False)
      else:
        self.next()
      #remember to discard timeouts for recieved nums
    else:
      print("something went wrong here")
    return

  def discardTimeout(self, val):
    for i in self.myL:
      if i[1] == "timeout":
        if val in i[2]:
          i[2].remove(val)
          break
    return
  def getKey(self, item):
    return item[0]

  def stop(self):
    length = len(self.sent_by_sender)
    ans1 = self.sent_by_sender[:self.packets_num]
    diff = length - self.packets_num
    ans2 = self.sent_by_reciever[:-diff] if diff > 0 else self.sent_by_reciever

    ans1 = [str(i) for i in ans1]
    ans2 = [str(i) for i in ans2]
    ans1 = ",".join(ans1)
    ans2 = ",".join(ans2)
    print(f"\033[32m{ans1};{ans2}\033[0m")

if __name__ == "__main__":
    print("\nRunning Go-Back-N....Enter your values below: \n")
    GoBackN()