print ("~~~~~ Table Matematika Nich ~~~~~")
print ("Pilihan Model Matematika ")
m = print ("1. Perkalian")
p = print ("2. Pembagian")
x = int(input("Masukkan model matematika yang diinginkan 1/2 :"))
y = int(input("Menampilkan table matematika dari angka: "))
for i in range(1, 11):
    print(y, 'x', i, '=', y*i)

if x== 1 :
    jumlah = x*y
    print(y, 'x', i, '=', y*i)
