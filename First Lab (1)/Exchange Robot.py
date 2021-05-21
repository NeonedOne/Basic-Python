# Алексей Головлев, группа БСБО-07-19
buyprice = 0
sellprice = 0
price = int(input())
backprice = price

while price != 0:
    if backprice < price and buyprice == 0:
        buyprice = price
        print(buyprice)
    elif backprice > price and buyprice != 0 and sellprice == 0:
        sellprice = price
        print(sellprice)
    backprice = price
    price = int(input())

print(sellprice - buyprice)
