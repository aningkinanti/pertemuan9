# TUGAS PERTEMUAN 9 DAN PENJELASAN
## LIST, TUPLE, DAN DICTIONARY

**Nama	  : Aning Kinanti** <br>
**Nim	    : 312010364** <br>
**Kelas	  : TI.20.A2** <br>
**Matkul	: Bahasa Pemrograman** <br>

## TUGAS PRAKTIKUM 4

#### SOAL
![soal](ssPraktikum4/soal.PNG)

![soal2](ssPraktikum4/soal2.PNG)

#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas

```python
#author aning kinanti - 312010364

print(95*"=")
print("MASUKAN DATA SISWA")
print(95*"=")

dataNilai = []
while True :
    nama = input("Nama        : ")
    nim = input("NIM         : ")
    nTugas = int(input("Nilai Tugas : "))
    nUts = int(input("Nilai UTS   : "))
    nUas = int(input("Nilai UAS   : "))
    nAkhir = float(nTugas)*30/100+(nUts)*35/100+(nUas)*35/100
    dataNilai.append ([nama, nim, nTugas, nUts, nUas, nAkhir])
    add = input("TAMBAH DATA (ya/tidak)?")

    if add.lower() == "tidak":
        break


#directory data siswa
print(95*"=")
print("| {0:^2} | {1:^18} | {2:^10} | {3:^10} | {4:^10} | {5:^10} | {6:^7} |".format("NO", "NAMA", "NIM", "NILAI TUGAS", "NILAI UTS", "NILAI UAS", "NILAI AKHIR"))
print(95*"=")
no = 0
for x in dataNilai:
    no+=1
    print("| {0:>2} | {1:<18} | {2:>10} | {3:>11} | {4:>10} | {5:>10} | {6:>11.2f} |"\
        .format (no,x[0][:18],x[1][:10],x[2],x[3],x[4],x[5]))
print(95*"=")
```

#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![output](ssPraktikum4/output.PNG)

#### ANALISIS
•	Proses input data terjadi pada syntax dibawah ini :
``` pyhton
dataNilai = []
while True :
    nama = input("Nama        : ")
    nim = input("NIM         : ")
    nTugas = int(input("Nilai Tugas : "))
    nUts = int(input("Nilai UTS   : "))
    nUas = int(input("Nilai UAS   : "))
    nAkhir = float(nTugas)*30/100+(nUts)*35/100+(nUas)*35/100
    dataNilai.append ([nama, nim, nTugas, nUts, nUas, nAkhir])
    add = input("TAMBAH DATA (ya/tidak)?")
```

•	Pada statement `dataNilai=[]` berfungsi untuk menyimpan/merangkap data yang akan diinputkan oleh user <br>
•	Pada statement `while True :` berfungsi untuk melakukan proses looping/perulangan. <br>
•	Pada statement `nAkhir = float(nTugas)*30/100+(nUts)*35/100+(nUas)*35/100` diambil dari ketentuan soal untuk proses perhitungan nilai akhir. <br>
•	Pada statement `dataNilai.append ([nama, nim, nTugas, nUts, nUas, nAkhir])` berfungsi menambah element list. <br>
•	Pada statement
``` python
add = input("TAMBAH DATA (ya/tidak)?")

if add.lower() == "tidak":
        break
```
  untuk melakukan proses condition atau pemilihan 2 opsi <br>
  jika user memilih ya maka program akan menampilkan tambah data, sedangkan jika user memilih tidak maka program akan menampilkan directory data mahasiswa. <br>
  
•	Proses directory terjadi pada syntax dibawah ini :
``` pyhton
#directory data siswa
print(95*"=")
print("| {0:^2} | {1:^18} | {2:^10} | {3:^10} | {4:^10} | {5:^10} | {6:^7} |".format("NO", "NAMA", "NIM", "NILAI TUGAS", "NILAI UTS", "NILAI UAS", "NILAI AKHIR"))
print(95*"=")
no = 0
for x in dataNilai:
    no+=1
    print("| {0:>2} | {1:<18} | {2:>10} | {3:>11} | {4:>10} | {5:>10} | {6:>11.2f} |"\
        .format (no,x[0][:18],x[1][:10],x[2],x[3],x[4],x[5]))
print(95*"=")
```

•	Pada statement
``` pyhton
print("| {0:^2} | {1:^18} | {2:^10} | {3:^10} | {4:^10} | {5:^10} | {6:^7} |".format("NO", "NAMA", "NIM", "NILAI TUGAS", "NILAI UTS", "NILAI UAS", "NILAI AKHIR"))
```
berfungsi untuk membuah tabel directory agar terlihat rapih. <br>

•	Pada statement `no = 0` dan `no+=1`berfungsi untuk menambahkan nomor urut. <br>
•	Pada statement 
``` pyhton
 print("| {0:>2} | {1:<18} | {2:>10} | {3:>11} | {4:>10} | {5:>10} | {6:>11.2f} |"\
        .format (no,x[0][:18],x[1][:10],x[2],x[3],x[4],x[5]))
```
berfungsi untuk memanggil/menyimpan data yang sudah diinput ke dalam directory. <br>

## SEKIAN DAN TERIMAKASIH :)






