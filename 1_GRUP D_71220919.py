susu = 20000
permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

duitpertama = int(input('Masukkan jumlah uang: RP'))
start = input('ketik START untuk memulai: ')
if start.lower() == 'start':
    while True:
        tumbas = input('Apa barang yang akan Anda tumbas? ')
        if tumbas.lower() =='susu':
            if duitpertama >= susu:
                duitpertama -= susu
                print('Sisa uang Anda',duitpertama)
            else:
                print('Uang tidak cukup')
        elif tumbas.lower() =='permen':
            if duitpertama >= permen:
                duitpertama -= permen
                print('Sisa uang Anda',duitpertama)
            else:
                print('Uang anda tidak cukup')
        elif tumbas.lower() =='roti':
            if duitpertama >= roti:
                duitpertama -= roti
                print('Sisa uang Anda',duitpertama)
            else:
                print('Uang anda tidak cukup')
        elif tumbas.lower() =='indomie':
            if duitpertama >= indomie:
                duitpertama -= indomie
                print('Sisa uang Anda',duitpertama)
            else:
                print('Uang anda tidak cukup')
        elif tumbas.lower() =='vitamin':
            if duitpertama >= vitamin:
                duitpertama -= vitamin
                print('Sisa uang Anda',duitpertama)
            else:
                print('Uang anda tidak cukup')
        elif tumbas.lower() == 'sudah':
            break
        else :
            print('Barang tidak tersedia')
