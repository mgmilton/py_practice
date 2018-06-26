# print('Matt' + 2) results in type error
print('Matt' + str(2)) # convient method for converting object to string

sales_record = {
    'price': 3.24,
    'num_items': 4,
    'person': 'Chris'
}

sales_statement = '{} bought {} items(s) at a price of {} each for a totoal of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))
