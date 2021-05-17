my_f = open("my_file.txt", "w")
temp_line = " "
while temp_line != "":
    temp_line = input()
#    print(temp_line)
    my_f.writelines(temp_line + '\n')
my_f.close()
