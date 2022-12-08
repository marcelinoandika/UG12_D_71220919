print ("~~~~~ Table Matematika Nich ~~~~~")
print ("Pilihan Model Matematika ")
print ("1. Perkalian")
print ("2. Pembagian")
x = int(input("Masukkan model matematika yang diinginkan 1/2 :"))
y = int(input("Menampilkan table matematika dari angka: "))

if x == 1 :
    for i in range(1, 11):
        print(y, 'x', i, '=', y*i)
elif x == 2:
    for i in range(50, 66):
        print(i, ':', y, '=', i/y)
else:
    print("Pilihan tidak tersedia, jangan ngasal!")

    

