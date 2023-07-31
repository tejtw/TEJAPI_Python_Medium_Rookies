import tejapi
import matplotlib.pyplot as plt
tejapi.ApiConfig.api_key = "your api key"
tejapi.ApiConfig.ignoretz = True

# Select 2739 recent stock prices
company = '2739'
price_data = tejapi.get('TWN/EWPRCD',
                        coid=company,
                        mdate={
                            # start date
                            'gte': '2023-06-12',
                            # end date
                            'lte': '2023-07-12'},
                        opts={'columns': ['coid', 'mdate', 'close_d']},
                        paginate=True
                        )
print(price_data)

date = []
for d in price_data['mdate']:
    date.append(str(d)[5:7]+'/'+str(d)[8:10])


plt.figure(figsize=(11, 6))
plt.plot(date, price_data['close_d'], label='stock price', color='blue')
plt.title('stock price')  # set figure title
plt.xlabel('Days')  # set X-axis label
plt.ylabel('price')  # Set Y-axis label
plt.show()

get_day1_price = price_data['close_d'][0]
print('purchase price:', get_day1_price)
no_strategy = 0
if_strategy = 0


for i in range(0, len(price_data['close_d'])):
    no_strategy = no_strategy + price_data['close_d'][i]-get_day1_price

    # If the price decrease more than 10 percent of original price , it will be sold.
    if price_data['close_d'][i] < get_day1_price*0.9:
        if_strategy += 0
    else:
        if_strategy = if_strategy + price_data['close_d'][i]-get_day1_price


print('No-loss-avoidance operation settlement surplus:', no_strategy)
print('circumvention operation to settle the surplus:', if_strategy)
