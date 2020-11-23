
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
    #.format(no, nama, nim, nTugas, nUts, nUas, nAkhir))
        .format (no,x[0][:18],x[1][:10],x[2],x[3],x[4],x[5]))
print(95*"=")