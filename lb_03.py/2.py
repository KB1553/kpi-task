from itertools import permutations

def is_des(num_str):
    return all(num_str[i] > num_str[i + 1] for i in range(len(num_str) - 1))

def is_div_by_3(num_str):
    return int(num_str) % 3 == 0

def find_passwords():
    passwords = []
    for digits in permutations('9876543210', 7):
        num_str = ''.join(digits)
        if is_des(num_str) and is_div_by_3(num_str):
            passwords.append(num_str)
    return passwords

print("Усі можливі паролі:")
print(find_passwords())