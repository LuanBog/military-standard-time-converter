#!/usr/bin/env python

def standard_to_military(standard_time):
    splitted_by_space = standard_time.split()
    hour = splitted_by_space[0].split(':')[0]
    minute = splitted_by_space[0].split(':')[1]
    am_or_pm = splitted_by_space[1].lower()

    if am_or_pm == 'am':
        hour = hour.replace('0', '') # if the user put 06:23, if this line is not here, it will return as 006:23 am
        hour = '0' + hour
    else:
        hour = int(hour) + 12

    return f'{hour}{minute}'

def military_to_standard(military_time):
    hour = int(military_time[0]) if len(military_time) == 3 else int(military_time[:2])
    minute = military_time[1:] if len(military_time) == 3 else military_time[2:]
    am_or_pm = 'am'

    if hour >= 12:
        hour = hour - 12
        am_or_pm = 'pm'

        if hour == 0:
            hour = 12
    
    return f'{hour}:{minute} {am_or_pm}'

if __name__ == '__main__':
    choice = input('\nChoose: \n[A] Standard to Military \n[B] Military to Standard \n> ').lower()

    if choice == 'a':
        print('\nExample:')
        print('12:00 pm')
        print('4:52 pm')
        print('6:03 am')
        print('')
        print('How to convert: \nIf it is pm, get the hour and add it by 12 and combine it with the minute. If it is am, just get the hour and attach it to the minute')
        standard_time = input('\nStandard time: ')

        print('Military time: {}'.format(standard_to_military(standard_time.strip())))
    elif choice == 'b':
        print('\nExample:')
        print('1200')
        print('1652')
        print('603 / 0603')
        print('')
        print('How to convert: \nFor a military time that is larger than 12:00, just subtract 12 hours to get the 24 hour(standard time), then add “pm”')
        military_time = input('\nMilitary time: ')

        print('Standard time: {}'.format(military_to_standard(military_time.strip())))
