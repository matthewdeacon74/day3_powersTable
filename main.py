print('Learn your squares and cubes!')

#set condition for ending the script - continue by default
is_done=False

while is_done == False:
    user_int = int(input('Enter an integer: '))
    print('Number  ', 'Squared  ', 'Cubed  ')
    print('======  ', '=======  ', '=====  ')
    for number in range(1, user_int+1, 1):
        print(number, '      ', number**2, '       ', number**3)

    # multiplication table
    print('')
    current_xnum = ''
    current_spacer = ''
    for x_number in range(1, user_int+1, 1):
        current_xnum += ('    ' + str(x_number))
        current_spacer += ('    ' + '=')

    print(current_xnum)
    print(current_spacer)
    for y_number in range(1, user_int + 1, 1):
        x_string = str(y_number) + " | "
        for x_number in range(1, user_int+1, 1):
            product_number = y_number * x_number
            x_string += str(product_number) + '    '
        print(x_string)

    # ask if user wants to go again
    do_continue = input('Continue? (y/n): ')
    if do_continue == 'n':
        is_done = True