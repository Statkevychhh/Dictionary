def say_hello(name=''):
    print(f'Hello {name}')

def print_age(age=20):
    print(f'Age  {age}')


def main():
    name = input('Enter your name please: ')
    say_hello(name=name)
    print_age(age=30)
    print(f"Ця програма працює як независима програма з іменем  {__name__}")

if __name__ == '__main__':
    main()
else:
 
   print(f"Ця програма працює як імпортований модуль з іменем  {__name__}")

   