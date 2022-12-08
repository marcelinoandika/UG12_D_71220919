susu = 20000
permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

uangAwal = int(input('Masukkan jumlah uang: RP'))
start = input('ketik START untuk memulai: ')
if start.lower() == 'start':
    while True:
        beli = input('Apa barang yang akan Anda beli? ')
        if beli.lower() =='susu':
            if uangAwal >= susu:
                uangAwal -= susu
                print('Sisa uang Anda',uangAwal)
            else:
                print('Uang tidak cukup')
        elif beli.lower() =='permen':
            if uangAwal >= permen:
                uangAwal -= permen
                print('Sisa uang Anda',uangAwal)
            else:
                print('Uang anda tidak cukup')
        elif beli.lower() =='roti':
            if uangAwal >= roti:
                uangAwal -= roti
                print('Sisa uang Anda',uangAwal)
            else:
                print('Uang anda tidak cukup')
        elif beli.lower() =='indomie':
            if uangAwal >= indomie:
                uangAwal -= indomie
                print('Sisa uang Anda',uangAwal)
            else:
                print('Uang anda tidak cukup')
        elif beli.lower() =='vitamin':
            if uangAwal >= vitamin:
                uangAwal -= vitamin
                print('Sisa uang Anda',uangAwal)
            else:
                print('Uang anda tidak cukup')
        elif beli.lower() == 'sudah':
            break
        else :
            print('Barang tidak tersedia')
