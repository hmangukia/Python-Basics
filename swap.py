obj = "qwerty"


def my_print(my_text=''):
    print('ASCII     DEC     HEX     BIN')
    for i in my_text:
        print('{0}         {1}     0x{1:02X}    0b{1:08b}'.format(i, ord(i)))


my_swap_text = reversed(obj)
my_print(my_swap_text)