import json

my_list = []
my_keys = dict()
with open("text_7.txt") as file3:
    isok = 0
    av_profit = 0
    for line in file3:
        temp = line.split()
        profit = int(temp[2]) - int(temp[3])
        my_keys[temp[0]] = profit
        if profit >= 0:
            av_profit += float(profit)
            isok += 1
    my_list.append(my_keys)
    av_profit /= isok
    my_list.append({'average_profit': av_profit})

print(my_list)

with open("text_7.json", "w", encoding="utf-8") as w_json:
    json.dump(my_list, w_json, ensure_ascii=False, indent='\t')
