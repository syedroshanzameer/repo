print("Hello World")

x = for x in range(10)

animals = ['Dog','Cat','Fox','Giraffe']
' '.join([animal.upper() + '!' for animal in animals])

names = 'raymond rachel matthew'.split()
colors = 'red blue yellow green'.split()
cities = 'austin dallas chicago austin houstom austin chocago dallas'.split()

for i,name in enumerate(names,start = 1):
    print(i, '--->', name)

new = map(colors,cities) 
print(new)
 

from functools import partial
def dist(p,q):
    return abs(p-q)
car = 48
gas_stations = [188,20,89,42,17,52,77,102,93,17,35,61]
list(map(partial(dist,car), gas_stations))


import pandas as pd


load_date = '2017-10-01'
end_date = '2020-01-01'

# choose some combination of below methods
while end_date < '2020-01-01':
for i in range(load_date,end_date) if i <= '2020-01-01':
    end_date = (pd.Timestamp(load_date) + pd.DateOffset(months=3)).strftime('%Y-%m-%d')
    print(end_date)

for i in range(2017,2020):
    end_date = (pd.Timestamp(load_date))
    end_date += pd.DateOffset(months=3)
    i = int(end_date[0:4])
    print(end_date)


end_date = pd.date_range(start='2017-07-01',end='2020-01-01', freq='2M')

for date in end_date:
    result = f"load_date > '2017-07-01' and load_date <{date.strftime('%Y-%m-%d')} and (TRANSACTION_EVENT_KEY < TRANSACTION_KEY - 11874725579980800) limit 10"
    print(result)

for date in end_date:
    print(date.strftime('%Y-%m-%d'))