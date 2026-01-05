# ================== DATA GLOBAL ==================
biodata = {}
sks_list = []
nilai_list = []


# ================== KONVERSI NILAI ==================
def konversi_nilai_ke_bobot(nilai):
    if nilai >= 85:
        return 4
    elif nilai >= 80:
        return 3.75
    elif nilai >= 75:
        return 3.5
    elif nilai >= 70:
        return 3
    elif nilai >= 65:
        return 2.75
    elif nilai >= 60:
        return 2.5
    elif nilai >= 55:
        return 2
    elif nilai >= 45:
        return 1
    else:
        return 0

    
def konversi_huruf_ke_bobot(huruf):
    h = huruf.lower()
    if h == "a":
        return 4
    elif h == "a-":
        return 3.75
    elif h == "b+":
        return 3.5
    elif h == "b":
        return 3
    elif h == "b-":
        return 2.75
    elif h == "c+":
        return 2.5
    elif h == "c":
        return 2
    elif h == "d":
        return 1
    elif h == "e":
        return 0
    else:
        return None


def konversi_angka_ke_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 80:
        return "A-"
    elif nilai >= 75:
        return "B+"
    elif nilai >= 70:
        return "B"
    elif nilai >= 65:
        return "B-"
    elif nilai >= 60:
        return "C+"
    elif nilai >= 55:
        return "C"
    elif nilai >= 45:
        return "D"
    else:
        return "E"


# ================== BIODATA ==================
def input_biodata():
    global biodata
    nama = input("Nama : ")
    nim = input("NIM  : ")

    biodata["nama"] = nama
    biodata["nim"] = nim
    print("berhasil ditambahkan")


def lihat_biodata():
    if not biodata:
        print("data mahasiswa belum diinput")
    else:
        print("Nama :", biodata["nama"])
        print("NIM  :", biodata["nim"])


# ================== SKS ==================
def input_sks():
    global sks_list
    sks_list.clear()

    print("--------- Input SKS ---------")
    data = input("SKS: ")

    # contoh input: "2 2 3"
    sks_list = list(map(int, data.split()))

    print("berhasil ditambahkan")


# ================== INPUT NILAI  ==================
def input_nilai():
    global nilai_list
    nilai_list.clear()

    if not sks_list:
        print("SKS belum diinput")
        return

    print("--------- Input Nilai Mahasiswa ---------")
    print("Input dalam bentuk angka atau huruf? (1/2): ")
    pilihan = input()

    if pilihan == "1":
        data = input("Nilai: ")
        nilai_angka = list(map(float, data.split()))

        if len(nilai_angka) != len(sks_list):
            print("Jumlah nilai tidak sesuai jumlah SKS")
            return

        for n in nilai_angka:
            nilai_list.append(konversi_nilai_ke_bobot(n))

    elif pilihan == "2":
        data = input("Nilai: ")
        nilai_huruf = data.split()

        if len(nilai_huruf) != len(sks_list):
            print("Jumlah nilai tidak sesuai jumlah SKS")
            return

        for h in nilai_huruf:
            bobot = konversi_huruf_ke_bobot(h)
            if bobot is None:
                print("Input huruf tidak valid")
                return
            nilai_list.append(bobot)

    else:
        print("Pilihan tidak valid")
        return

    print("berhasil ditambahkan")


# ================== LIHAT NILAI  ==================
def lihat_nilai():
    if not biodata:
        print("Biodata belum diinput")
        return

    if not nilai_list:
        print("Nilai belum diinput")
        return

    print("--------- Nilai Mahasiswa ---------")
    print("Nama:", biodata["nama"])
    print("NIM :", biodata["nim"])

    nilai_huruf = []

    for bobot in nilai_list:
        # ubah bobot ke nilai angka kira-kira
        if bobot == 4:
            nilai_huruf.append("A")
        elif bobot == 3.75:
            nilai_huruf.append("A-")
        elif bobot == 3.5:
            nilai_huruf.append("B+")
        elif bobot == 3:
            nilai_huruf.append("B")
        elif bobot == 2.75:
            nilai_huruf.append("B-")
        elif bobot == 2.5:
            nilai_huruf.append("C+")
        elif bobot == 2:
            nilai_huruf.append("C")
        elif bobot == 1:
            nilai_huruf.append("D")
        else:
            nilai_huruf.append("E")

    print("Nilai:", nilai_huruf)



# ================== IP ==================
def hitung_ip():
    if not biodata:
        print("Biodata belum diinput")
        return

    if not sks_list or not nilai_list:
        print("Data SKS atau nilai belum lengkap")
        return

    total_sks = sum(sks_list)
    total_bobot = 0

    for i in range(len(sks_list)):
        total_bobot += sks_list[i] * nilai_list[i]

    ip = total_bobot / total_sks

    print("--------- Index Prestasi (IP) Mahasiswa ---------")
    print(f"Mahasiswa: {biodata['nim']} {biodata['nama']}")
    print(round(ip, 2))

