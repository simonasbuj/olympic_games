

def read_input(file_path):
    with open(file_path) as file:
        for line in file:
            return int(line.split()[0]), int(line.split()[1])


def are_all_values_in_list_the_same(list):
    return all(i == list[0] for i in list)


def split_string_at_character_numbers(string, how_many_parts):
    split_at_character_number = int(len(string) / how_many_parts)
    patterns = [string[i:i+split_at_character_number] for i in range(0, len(string), split_at_character_number)]
    return patterns


def find_matching_patterns(string, K):

    s_reversed = string[::-1]

    found_matching_pattern = False

    for char_num in range(K, len(s_reversed) + 1, K):
        patterns = split_string_at_character_numbers(s_reversed[:char_num], K)
        are_values_the_same = are_all_values_in_list_the_same(patterns)
        if (are_values_the_same):
            found_matching_pattern = True
            break

    return '1' if found_matching_pattern else '0'


def calculate_how_many_times_to_pay(N, K):

    s = '0'

    for n in range(2, N+1):
        s = s + find_matching_patterns(s, K)

    return s.count('1')


if __name__ == "__main__":
    print("hi")
    N, K = read_input("input/3.in")

    print(f"N is {N}, K is {K}")

    answer = calculate_how_many_times_to_pay(N, K)

    print(f"answer is {answer}")
    

