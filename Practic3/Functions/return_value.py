# 1
def area(length, width):
    return length*width

length = float(input('Enter length: '))
width = float(input('Enter width: '))
result = area(length, width)
print('area:',result)


# 2
def even_num(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

num = int(input('Enter number: '))
result = even_num(num)
print(result)

# 3
def week_day(day):
    match day:
        case 1|2|3|4|5:
            return 'Week day!'
        case 6|7:
            return 'WEEKEND HOOORA!'

day = int(input('Enter the day: '))
result = week_day(day)
print(result)

# 4 work length
def wor_len(word):
    if len(word) >= 10 and len(word) <= 15:
        return 'Medum word'
    elif len(word) < 10:
        return 'short word'
    else:
        return 'Long word'

word = str(input('Enter your word: '))
result = wor_len(word)
print(result)
