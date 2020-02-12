#!/usr/bin/env python3

def add(*numbers):
    result = None
    for number in numbers:
        if result is None:
            result = number
        else:
            result += number
    return result
def say_hello(first_name, last_name):
    return f'Hello {first_name}, {last_name}'
def contact_card(name, age, *titles,
    phone, mail, format = 'simple', **kwargs):
    """
    """
    
    if format == 'simple':
        print(f"{name} is {age}, You may contact him/her at phone: {phone}, mail: {mail}")
    else:
        print(f'Name: {name}')
        print(f'Age: {age}')
        print(f'Phone: {phone}')
        print(f'Mail: {mail}')
        for key, value in kwargs.items():
            print(f'{key}: {value}')

contact_card('ali', 30, 'title1', 'title2',
    phone='09123456789',
    mail='ali@python.org',
    format='simple',
    position='CO',
    title='Scrum Master')