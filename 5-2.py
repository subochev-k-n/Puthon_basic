my_f = open("my_file.txt", "w")
temp_line = " "
line_count = 0
words_count = []
while True:
    temp_line = input()
    if temp_line == "":
        break
    my_f.writelines(temp_line + '\n')
    line_count += 1
    temp_words = len(temp_line.split())
    words_count.append(temp_words)
my_f.close()
en_w = enumerate(words_count)
print(f"В созданном файле: {line_count} строк")
for w in en_w:
    print(f"Строка {w[0]}: {w[1]} слов")
