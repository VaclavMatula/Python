adresa = input ("enter IPv4 address: ")
oktet1 = adresa.partition('.')[0]
rest = adresa.partition('.')[2]
oktet2 = rest.partition('.')[0]
rest = rest.partition('.')[2]
oktet3 = rest.partition('.')[0]
rest = rest.partition('.')[2]
oktet4 = rest.partition('/')[0]
maska = rest.partition('/')[2]

#print (oktet1)
#print (oktet2)
#print (oktet3)
#print (oktet4)
#print (maska)

x = int(maska)
y = 32 - x

binmask = ""

while x > 0:
    binmask = binmask + "1"
    x = x - 1

while y > 0:
    binmask = binmask + "0"
    y = y -1

#print (binmask)

m1oct = binmask[0:8]
m2oct = binmask[8:16]
m3oct = binmask[16:24]
m4oct = binmask[24:32]

#print (m1oct)
#print (m2oct)
#print (m3oct)
#print (m4oct)

mask = m1oct + "." + m2oct + "." + m3oct + "." + m4oct
print (f"Maska (binárně) : {mask}")

z = 32-int(maska)
pocet_adres = 2**z
pocet_hostu = pocet_adres - 2
print (f"Počet adres: {pocet_adres}")
print (f"Počet hostů: {pocet_hostu}")