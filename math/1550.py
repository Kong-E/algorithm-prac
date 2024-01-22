hex_number = input()

# 16진수를 10진수로 변환하기
decimal_number = 0
length = len(hex_number)

for i in range(length):
    # 현재 자릿수의 문자를 가져옴
    digit = hex_number[i]

    # 16진수의 각 자릿수를 10진수로 변환
    if '0' <= digit <= '9':
        value = ord(digit) - ord('0')
    elif 'A' <= digit <= 'F':
        value = ord(digit) - ord('A') + 10
    elif 'a' <= digit <= 'f':
        value = ord(digit) - ord('a') + 10

    # 변환된 값을 적절한 자릿수의 16의 거듭제곱과 곱하여 더함
    decimal_number += value * (16 ** (length - 1 - i))

print(decimal_number)
