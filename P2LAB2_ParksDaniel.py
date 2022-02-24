current_price = int(input())
last_months_price = int(input())

price_change = current_price - last_months_price
mortgage = f'{((current_price * 0.051) / 12):.2f}'

print( 'This house is $',current_price,'. The change is $',price_change , ' since last month.', sep='')
print( 'The estimated monthly mortgage is $', mortgage,"." ,sep='')

   