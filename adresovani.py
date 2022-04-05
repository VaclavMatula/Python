adresa = input ("enter IPv4 address: ")
oktet1 = adresa.partition('.')[0]
rest = adresa.partition('.')[2]
oktet2 = rest.partition('.')[0]
rest = rest.partition('.')[2]
oktet3 = rest.partition('.')[0]
rest = rest.partition('.')[2]
oktet4 = rest.partition('/')[0]
maska = rest.partition('/')[2]
print (oktet1)
print (oktet2)
print (oktet3)
print (oktet4)
print (maska)