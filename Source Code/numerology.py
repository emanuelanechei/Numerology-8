import ssl, urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

print('***NUMEROLOGY***')
print('')

#Number assigned for each alphabet
alphabet_number = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6,'G':7,'H':8,'I':9,
                  'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'O':6,'P':7,'Q':8,'R':9,
                  'S':1, 'T':2, 'U':3, 'V':4, 'W':5, 'X':6,'Y':7,'Z':8}


web_pages = {1: 'NUMBER ONE', 2: 'NUMBER TWO', 3: 'NUMBER THREE',
            4: 'NUMBER FOUR', 5: 'NUMBER FIVE', 6:'NUMBER SIX',
            7:'NUMBER SEVEN', 8: 'NUMBER EIGHT', 9:'NUMBER NINE', None:'YOUR MATURITY NUMBER'}

while True:

    user_input = input('Enter your name (A-Z), or quit: ')
    if user_input == 'quit':
        break
    name = user_input.upper().split()
    name_element = list()
    for alphabet in name:
        if alphabet.isalpha():
            name_element.append(alphabet)
        else:
            print('Please enter only unaccented alphabet, a-z')
            print(' ')
            continue
    number = list()
    for alphabet in name_element:
        letter = list(alphabet)
        for each_alphabet in letter:
            number.append(alphabet_number.get(each_alphabet))
    integer_1 = list()
    integer_2 = list()
    destiny_number = None
    if sum(number)>=10:
        for i in str(sum(number)):
            integer_1.append(int(i))
            if sum(integer_1)>=10:
                for ii in str(sum(integer_1)):
                    integer_2.append(int(ii))
                destiny_number = sum(integer_2)
            else:
                destiny_number = sum(integer_1)
    elif sum(number) < 10:
        destiny_number = sum(number)

    birthday_input = input('Enter your birthday (DDMMYYYY): ')
    if len(birthday_input.strip()) == 8:
        try:
            birthday_number = int(birthday_input)
        except:
            print('Please enter a value with numeric characters only')
            print(' ')
            continue
    else:
        print('Please enter a value with numeric characters only in DDMMYYYY format')
        print(' ')
        continue

    str_birthday_number = str(birthday_number)
    date = str_birthday_number.zfill(8)[0:2]
    month = str_birthday_number.zfill(8)[2:4]
    if  int(date) > 31:
        print('Date cannot be greater than 31')
        print(' ')
        continue
    elif int(date) < 1:
        print('Please enter a valid date')
        print(' ')
        continue
    elif int(month) > 12:
        print('Month cannot be greater than 12')
        print(' ')
        continue
    elif int(month) < 1:
        print('Please enter a valid month')
        print(' ')
        continue
    life_number = None
    birthday_number_list_0 = list()
    birthday_number_list_1 = list()
    birthday_number_list_2 = list()
    for u in str(birthday_number):
        birthday_number_list_0.append(int(u))

    if sum(birthday_number_list_0)>=10:
        for y in str(sum(birthday_number_list_0)):
            birthday_number_list_1.append(int(y))
        if sum(birthday_number_list_1)>=10:
            for yy in str(sum(birthday_number_list_1)):
                birthday_number_list_2.append(int(yy))
            life_number = sum(birthday_number_list_2)
        else:
            life_number = sum(birthday_number_list_1)
    elif sum(birthday_number_list_0)<10:
        life_number = sum(birthday_number_list_0)

    #ignore ssl certificate
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        connection = urllib.request.urlopen('https://goo.gl/h8Xiym', context=ctx).read()
    except:
        print(' ')
        print('Please check your internet connection')
        print(' ')
        continue

    soup = BeautifulSoup(connection, 'html.parser')
    tags = soup.get_text()

    if int(life_number) < 9 :
        target_1 = web_pages.get(int(life_number))
        target_2 = web_pages.get(int(life_number)+1)
    else:
        target_1 = web_pages.get(int(life_number))
        target_2 = web_pages.get(None)

    if int(destiny_number) < 9 :
        target_1_des = web_pages.get(int(destiny_number))
        target_2_des = web_pages.get(int(destiny_number)+1)
    else:
        target_1_des = web_pages.get(int(destiny_number))
        target_2_des = web_pages.get(None)

    find_1 = tags.find(str(target_1))
    find_2 = tags.find(str(target_2))
    find_1_des = tags.find(str(target_1_des))
    find_2_des = tags.find(str(target_2_des))

    print(' ')
    print('Life Number:', life_number)
    print(tags[find_1+len(target_1):find_2].strip())
    print(' ')
    print('Destiny Number:', destiny_number)
    print(tags[find_1_des+len(target_1_des):find_2_des].strip())
    print(' ')
    print('Source: http://www.dailymail.co.uk')
    print('Code created by Fernandi Terahadi - 17 October 2017')
    print(' ')
