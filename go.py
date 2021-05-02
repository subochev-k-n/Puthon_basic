firm = str(input("Введите название организации: "))
revenue = float(input("Введите значение выручки за 2020 год: "))
costs = float(input("Введите значение издержек за 2020 год: "))

profit = revenue - costs

if profit > 0:
    print("Поздравляем. Ваша организация прибыльна!")
    profitability = float(profit / revenue)
    employee = int(input("Введите среднесписочную численность сотрудников за 2020 год: "))
    profit_per_employ = float(profit / employee)
    print("Результаты %s за 2020 год: рентабельность выручки %.2f' , прибыль на сотрудника %.02f рублей" % (firm,
                                                                                                            profitability,
                                                                                                            profit_per_employ))
else:
    print("Увы. Ваша организация убыточна. Удачи в следующем году.")
