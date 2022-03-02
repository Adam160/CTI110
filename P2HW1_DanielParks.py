# Totals from purchased items
# 01 Mar 2022
# CTI-110 P2HW1 - Total Purchases
# Daneil Parks
#

item_1 = float(input('Enter the price of item #1:\n'))
item_2 = float(input('Enter the price of item #2:\n'))
item_3 = float(input('Enter the price of item #3:\n'))
item_4 = float(input('Enter the price of item #4:\n'))
item_5 = float(input('Enter the price of item #5:\n'))

subtotal_int = (item_1 + item_2 + item_3 + item_4 + item_5)
sales_tax = (subtotal_int *.07)
total = (subtotal_int + sales_tax)

print('-------Results-------')
print('Subtotal: ',  f'{(subtotal_int):.2f}' )
print('Sales Tax: ',  f'{(sales_tax):.2f}')
print('Total: ', f'{(total):.2f}')