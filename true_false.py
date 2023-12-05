def read_answers(file_path):
    # Initialize empty dictionaries for true and false answers
    true_false_dict = {}

    # Open the file for reading
    with open(file_path, 'r', encoding='utf-8') as file:
        current_answer = None
        which = True
        true_false_dict[which] = []

        # Read each line
        for i, line in enumerate(file, start=1):
            # Remove leading and trailing whitespaces (including newline character)
            line = line.strip()

            if line == "":
                which = False
                true_false_dict[which] = []

            true_false_dict[which].append(line)

    return true_false_dict


def check_answer(ans):
    all_answers = read_answers("truefalse.txt")

    for check in all_answers.keys():
        if ans in all_answers[check]:
            return check
    return None


# Example usage
answers = """
A. The IP (Internet Protocol) service model is a best-effort delivery service‚ and is a reliable service.
B. At the destination host‚ UDP segments with the same destination port number but different source IP addresses and/or source port numbers will be directed to the same process via the same socket.
C. In all version of TCP, the congestion window size is set to one MSS when a packet loss event occurs.
D. Multiplexing is done at the sending side‚ and demultiplex is done at the receiving side.
""".split('\n')[1:-1]

answers = [answer[3:] for answer in answers]

ans1, ans2, ans3, ans4 = answers

A = check_answer(ans1)
B = check_answer(ans2)
C = check_answer(ans3)
D = check_answer(ans4)

answer_list = [A, B, C, D]

for ind, boo in enumerate(answer_list):
    if ind == 0:
        if boo == True:
            print("A is True.")
        elif boo == False:
            print("A is False.")
        else:
            print("A is not in the True or False list.")
    elif ind == 1:
        if boo == True:
            print("B is True.")
        elif boo == False:
            print("B is False.")
        else:
            print("B is not in the True or False list.")
    elif ind == 2:
        if boo == True:
            print("C is True.")
        elif boo == False:
            print("C is False.")
        else:
            print("C is not in the True or False list.")
    else:
        if boo == True:
            print("D is True.")
        elif boo == False:
            print("D is False.")
        else:
            print("D is not in the True or False list.")
