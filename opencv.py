print('welcome to our shop here are the remaining items and remember this is a one way shop if you add item in your bag it will not be removed because it was not involved in our question assignment ')
print('REMEMBER THAT BOUTIQUE EMPLOY ONLY WORKS FOR 9 HOURS A DAY AND TIME ABOVE THAT INCLUDES BONUS')
print('REMEMBER BAKE SHOP EMPLOY WORKS FOR 8 HOURS AND ABOVE THAT INCLUDES BONUS')
number_of_available_rolls=0
number_of_available_samosay= 0
number_of_available_jalebi=0
samosa_unit_price=10
roll_unit_price=15
samosas_sold=0
rolls_sold=0
total_samosa_sales=0
total_roll_sales=0
add_samosas_instock=0
add_rolls_instock=0
emp_A_wagerate=80
emp_B_wagerate=60
bonus_A=0
bonus_B=0
emp_A_hours=0
emp_B_hours=0
total_cal_sales=0
total_number_of_available_samosay=int(number_of_available_samosay)
total_number_of_available_rolls=int(number_of_available_rolls)
total_stock=(int(total_number_of_available_rolls)+int(total_number_of_available_samosay))
number_of_cottonsuits=0
number_of_lawnsuits=0
emp_boutique_wagerate=50
emp_boutique_bonus=0
emp_boutique_hours=0
cottonsuit_price=200
lawnsuit_price=150
lawnsuit_sold=0
cottonsuit_sold=0
total_lawn_suitsales=0
total_cotton_suitsales=0
total_boutique_sales=0


def employ_payment():
    emp_hours_A = int(input('enter no.hours worked 1 to 8:'))
    emp_hours_B = int(input('enter no.hours worked 1 to 8:'))
    print('no.of hours worked by A:',emp_hours_A)
    print('no.of  hours worked by B:',emp_hours_B)
    employ_payment_A=emp_hours_A*80
    employ_payment_B=emp_hours_B*60
    print('employ A payment is:',employ_payment_A)
    print('employ B payment is:',employ_payment_B)

    if emp_hours_A>8:
        bonus_A=employ_payment_A * 0.3
        print('the salary bonus of employ A is:', bonus_A)
    elif emp_hours_B>8:
        bonus_B= employ_payment_B * 0.3
        print('the salary bonus of employ B is:',bonus_B)
    return ''



def add_stock():
    print()
    global number_of_available_samosay, add_samosas_instock, total_samosa_sales, samosas_sold
    global number_of_available_rolls, add_rolls_instock, total_roll_sales, rolls_sold
    global total_cal_sales, quantity
    number_of_available_samosay=number_of_available_samosay+int(input('enter no.of samosay you wan to add in stock:  '))
    number_of_available_rolls=number_of_available_rolls+int(input('enter no.of rolls you wan to add in stock:  '))
    return " "


def print_stock():
    global number_of_available_rolls,number_of_available_samosay
    print('remaining samosa stock is:',number_of_available_samosay)
    print('remaining rolls stock is:', number_of_available_rolls)
print(print_stock())

def item_remain():
    global number_of_available_rolls,number_of_available_samosay
    print('remaining samosa stock is:',number_of_available_samosay)
    print('remaining rolls stock is:',number_of_available_rolls)
    return ' '

def take_order():
    print()
    global number_of_available_samosay, add_samosas_instock, total_samosa_sales, samosas_sold
    global number_of_available_rolls, add_rolls_instock, total_roll_sales, rolls_sold
    global total_cal_sales, quantity
    total_sale = (int(total_roll_sales)) + (int(total_samosa_sales))

    print('samosas in stock:', number_of_available_samosay,'rolls in stock:', number_of_available_rolls)
    print('''samosasunit price=10\nrolls unit price=15\n''')
    print('press 1 if you want to buy roll')
    print('press 2 if you want to buy samosay')
    print('press any other number to end:')
    g = int(input('enter your choice 1 or 2:'))
    print()

    while True:

        if (g == 1) or (g == 2):
            if g == 1:
                if number_of_available_rolls >= 1:
                    quantity = int(input('enter no of rolls:'))
                    print()
                    if number_of_available_rolls >= quantity:
                        print('Here is your order :', quantity, 'rolls and your bill is:', roll_unit_price * quantity,
                                  'rupees')
                        rolls_sold = roll_unit_price * quantity
                        total_roll_sales = total_roll_sales + rolls_sold
                        print()
                        print()
                        number_of_available_rolls = number_of_available_rolls - quantity

                        if number_of_available_rolls < 1:
                            return 'rolls out of stock'
                        print()
                    else:
                        print('we have remaining rolls:', number_of_available_rolls)

                else:
                    print('rolls out of stock')
                    break
            if g == 2:
                if number_of_available_samosay >= 1:
                    quantity = int(input('enter no of samosay:'))
                    if number_of_available_samosay >= quantity:
                        print('Here is your order :', quantity, 'samosay and your bill is:',samosa_unit_price* quantity, 'rupees')

                        samosas_sold = samosa_unit_price * quantity
                        total_samosa_sales = total_samosa_sales + samosas_sold
                        print()
                        print()
                        number_of_available_samosay = number_of_available_samosay - quantity
                        if number_of_available_samosay < 0:
                            return 'samosay are out of stock'
                        print()

                    else:
                        print('we have remaining samosay', number_of_available_samosay, 'stock run out')

                else:
                    print('samosay out of stock')
                    break
        else:
            print()
            print('enter given choice 1 or 2')
            x = int(input('enter your choice again:'))
            print()
            continue
    return ' '
def total_amounted_calculations():
    global total_samosa_sales,total_roll_sales,total_cal_sales
    total_cal_sales=total_roll_sales+total_samosa_sales
    print('total samosa sales are:',total_samosa_sales)
    print('total roll sales are :',total_roll_sales)
    print('your total bakery shop sales are:', total_cal_sales)
    return ''

def boutique_emp():
    emp_boutique_hours = int(input('enter no.of hours boutique employe worked:'))
    print('no.of hours worked by boutique employ:', emp_boutique_hours)
    employ_boutique_payment=emp_boutique_hours*150
    print()
    print('boutiques employ salary is',employ_boutique_payment)
    if emp_boutique_hours>9:
        emp_boutique_bonus=employ_boutique_payment*0.3
        print('the bonus of boutique employ is:',emp_boutique_bonus)
        print()
        return ''



def add_boutique_stock():
    global number_of_cottonsuits,cottonsuit_price,cottonsuit_sold,total_cotton_suitsales
    global lawnsuit_price,lawnsuit_sold,number_of_lawnsuits,total_lawn_suitsales
    global total_boutique_sales
    number_of_cottonsuits=number_of_cottonsuits+int(input('enter no.of cotton suits you want to add:'))
    number_of_lawnsuits=number_of_lawnsuits+int(input('enter no.of lawn suits you want to add:'))
    return ' '


def print_boutique_stock():
    global number_of_cottonsuits, cottonsuit_price, cottonsuit_sold, total_cotton_suitsales
    global lawnsuit_price, lawnsuit_sold, number_of_lawnsuits, total_lawn_suitsales
    global total_boutique_sales
    print('no.of available cotton suits are: ',number_of_cottonsuits)
    print('no.of available lawn suits are:',number_of_lawnsuits)
    return " "

def remaining_boutique_items():
    global total_lawn_suitsales,total_cotton_suitsales,total_boutique_sales
    print('total lawnsuit sales are:',total_lawn_suitsales)
    print('total cotton suits sales are:',total_cotton_suitsales)
    print('total boutique sales are:',total_boutique_sales)
    return ' '

def boutique_order():

    print()
    global number_of_cottonsuits, cottonsuit_price, cottonsuit_sold, total_cotton_suitsales
    global lawnsuit_price, lawnsuit_sold, number_of_lawnsuits, total_lawn_suitsales
    global total_boutique_sales,amount
    total_boutique_sales=(int(total_cotton_suitsales)+int(total_lawn_suitsales))
    print('lawn suit in stock:',number_of_lawnsuits,'cotton suit in stock:',number_of_cottonsuits)
    print('cotton suit price=200,lawn suit price=150')
    print('press 1 if you want to buy cotton suit:')
    print()
    print('press 2 if you want to buy lawn suit:')
    print()
    o = int(input('enter your choice 1 or 2:'))

    while True:

        if (o == 1) or (o == 2):
            if o == 1:
                if number_of_cottonsuits >= 1:
                    quantity2 = int(input('enter no. of cotton suits:'))
                    print()
                    if number_of_cottonsuits >= quantity2:
                        print('Here is your order :', quantity2, 'cotton suits and your bill is:', cottonsuit_price * quantity2,
                              'rupees')
                        cottonsuit_sold = cottonsuit_price * quantity2
                        total_cotton_suitsales = total_cotton_suitsales + cottonsuit_sold
                        print()
                        print()
                        number_of_cottonsuits = number_of_cottonsuits - quantity2
                        if number_of_cottonsuits <= 0:
                            return 'cotton suit out of stock'
                        print()
                    else:
                        print('we have remaining cotton suits:', number_of_cottonsuits, 'stock run out')
                else:
                    print('cotton suit stock run out')
                    break
            if o == 2:
                if number_of_lawnsuits >= 1:
                    quantity2 = int(input('enter no of lawn suits:'))
                    print()
                    if number_of_lawnsuits >= quantity2:
                        print('Here is your order :', quantity2, 'cotton suits and your bill is:',
                              lawnsuit_price * quantity2, 'rupees')

                        lawnsuit_sold = lawnsuit_price * quantity2
                        total_lawn_suitsales = total_lawn_suitsales + lawnsuit_sold
                        print()
                        print()
                        number_of_lawnsuits = number_of_lawnsuits - quantity2
                        if number_of_lawnsuits <= 0:
                            return 'lawn suits are out of stock'
                        print()

                    else:
                        print('we have remaining lawn suits', number_of_lawnsuits, 'stock run out')

                else:
                    print('lawn suits run out of stock')
                    break
        else:
            print()
            print('enter given choice 1 or 2')
            x = int(input('enter your choice again:'))
            print()
            continue
    return ''
def total_amounted_calculations():
    global total_cotton_suitsales,total_lawn_suitsales,total_boutique_sales
    total_boutique_sales=total_cotton_suitsales+total_lawn_suitsales
    print('total cotton suit sales are:',total_cotton_suitsales)
    print('total lawn sales are :',total_lawn_suitsales)
    print('your total bakery shop sales are:', total_boutique_sales)
    return ''

while True:

        print('press 1 if you want to add employ hours and check employ wage rate')
        print('press 2 if you want to add stock')
        print('press 3 if you want to check stock')
        print('press 4 if you want to take order and calculate bill')
        print('press 5 if you want to check total bake shop sales')
        print('press 6 if you want to check bakery items')

        print('press 7if you want to take add boutique employ wage hours and calculate order')
        print('press 8  if you want to take order of boutique and calculate bill')
        print('press 9 if you want add boutique item')
        print('press 10 if you want to check boutique stock')
        print('press 11 if you want to check total boutique sales')
        print('press 12 to exit')
        c= int(input('enter your choice from 1 to 11: '))
        if c == 1:
            print(employ_payment())
        elif c == 2:
            print(add_stock())

        elif c == 3:
            print(print_stock())
        elif c == 4:
            print(take_order())
        elif c == 5:
            print(total_amounted_calculations())

        elif c == 6:
            print(item_remain())
        elif c == 7:
            print(emp_boutique_hours)
        elif c==8:
            print(boutique_order())
        elif c==9:
            print(remaining_boutique_items())
        elif c==10:
            print(print_boutique_stock())
        elif c==11:
            print(total_boutique_sales)
        elif c==12:
            print('exit')

print()