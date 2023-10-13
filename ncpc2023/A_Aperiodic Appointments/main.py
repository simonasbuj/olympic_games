

def read_input(file_path):
    with open(file_path) as file:
        for line in file:
            return int(line.split()[0]), int(line.split()[1])


def calculate_how_many_times_to_pay(N, K):
    s = '0'
    for n in range(2, N+1):
        if n > K:
            split_at_character_number = int(len(s) / K)
            previous_patterns = [s[i:i+split_at_character_number] for i in range(0, len(s), split_at_character_number)]

            if len(previous_patterns) > K:
                s = s + '0'
            elif all(i == previous_patterns[0] for i in previous_patterns):
                print(previous_patterns)
                print(all(i == previous_patterns[0] for i in previous_patterns))
                print('-'*10)
                s = s + '1'
            else:
                s = s + '0'
        else:
            s = s + '0'
        print(s)
    print(f"final: {s}")

if __name__ == "__main__":
    print("hi")
    N, K = read_input("input/1.in")

    print(f"N is {N}, K is {K}")
    calculate_how_many_times_to_pay(N, K)

    my_string = '001'
    n = int(len(my_string) / 2)
    #print([my_string[i:i+n] for i in range(0, len(my_string), n)])