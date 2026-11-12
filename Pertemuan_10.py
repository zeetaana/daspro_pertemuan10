# Pratikum Pertemuan 10 

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

list = [1, 2, 3, 4, 5]
print(list)
print(type(list))

arr2 = np.array([[1, 2, 3,4,5]])
print(arr[1])
print(arr[2:5])
print(arr[0]+arr[4])

# dimensi 2
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# dimensi 3
arr = np.array([ [[1,2]], [4, 5,]], [[7, 8]])
print(arr)

b = np.array([1, 2, 3, 4, 5])
c= arr = np.array([[1, 2, 3], [4, 5, 6]])
d= arr = np.array([ [[1,2]], [4, 5,]], [[7, 8]])

print(b.ndim)
print(c.ndim)
print(d.ndim)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

arr = np.array([1, 2, 3, 4, 5], dtype='S')
print(arr)
print(arr.dtype)

# soal 1 dan 2

# Nama : Mutia Risnawati 
# Kelas : 1C
# Nim : 2603069

# Seorang ilmuan memiliki sebuah array 1D yang isinya adalah suhu di Singapura selama 10 hari
# terakhir. Suhu tersebut ingin dikonversi dari Celcius menjadi Farenheit. Buatlah programnya
# dengan menggunakan library Numpy! (Catatan: silahkan buat data dummy untuk suhu 10 hari
# tersebut)

import numpy as np
b = np.array([35.3, 34.1, 34.3, 40.1, 34.1, 33.2, 34.5, 36.2, 30.1, 36.2])
konversi = (b * 9/5) + 32
print(konversi)

# Seorang guru Matematika memiliki data nilai ujian sebanyak 30 orang. Guru tersebut ingin
# menyimpan seluruh nilai ujian tadi ke dalam sebuah array untuk kemudian diurutkan nilainya
# dari yang terbesar hingga terkecil, kemudian ditampilkan. Selain itu, guru tersebut ingin melihat 5
# nilai terbesarnya saja. Buatlah programnya dengan menggunakan library Numpy! (Catatan:
# silahkan buat data dummy untuk nilai ujian 30 siswa tersebut).

import numpy as np
nilai = np.array([75, 88, 92, 67, 80, 95, 78, 85, 90, 82, 76, 89, 91, 84, 77, 93, 81, 86, 79, 94, 83, 87, 96, 70, 72, 74, 73, 71, 69, 68])
nilai_urut = np.sort(nilai)[::-1]
print("Nilai ujian dari yang terbesar hingga terkecil:",nilai_urut)
print("5 nilai terbesarnya:", nilai_urut[:5])