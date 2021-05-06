def sum_by_string(numbers):
    #    numbers=string_of_numbers.split()
    answer = 0.0
    for n in numbers:

        if n.isnumeric():
            answer += float(n)
    return answer


sum = 0
subsum = 0
f = False
print("Введите строку чисел разделенных пробелами или Q для выхода: ")
while f == False:
    numstr = input().split()
    subsum = sum_by_string(numstr)
    sum += subsum
    print(f"{subsum} ({sum})")

    for n in numstr:
        if n == "Q":
            f = True
