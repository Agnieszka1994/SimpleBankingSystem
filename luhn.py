def calculate_reminder(string: str) -> str:
    list_int = [int(x) for x in list(string)]
    running_sum = 0
    for i in range(len(list_int)):
        list_int[i] = list_int[i] * 2 if i % 2 == 0 else list_int[i]
        list_int[i] = list_int[i] - 9 if list_int[i] > 9 else list_int[i]
        running_sum += list_int[i]
    reminder = str(10 - (running_sum % 10))
    return reminder if reminder != '10' else '0'


def check_number(string: str) -> bool:
    list_int = [int(x) for x in list(string)]
    running_sum = 0
    for i in range(len(list_int) - 1):
        list_int[i] = list_int[i] * 2 if i % 2 == 0 else list_int[i]
        list_int[i] = list_int[i] - 9 if list_int[i] > 9 else list_int[i]
        running_sum += list_int[i]
    running_sum += list_int[-1]
    return running_sum % 10 == 0
