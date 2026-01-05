def konversi_nilai_ke_label(nilai_angka):
    if nilai_angka >= 85:
        return "A"
    elif nilai_angka >= 80:
        return "A-"
    elif nilai_angka >= 75:
        return "B+"
    elif nilai_angka >= 70:
        return "B"
    elif nilai_angka >= 65:
        return "B-"
    elif nilai_angka >= 60:
        return "C+"
    elif nilai_angka >= 55:
        return "C"
    elif nilai_angka >= 45:
        return "D"
    else:
        return "E"
        

def konversi_label_ke_bobot(label_huruf):
    label = label_huruf.lower()  # biar aman kalau input A / a

    if label == "a":
        return 4
    elif label == "a-":
        return 3.75
    elif label == "b+":
        return 3.5
    elif label == "b":
        return 3
    elif label == "b-":
        return 2.75
    elif label == "c+":
        return 2.5
    elif label == "c":
        return 2
    elif label == "d":
        return 1
    elif label == "e":
        return 0
    else:
        return None  


def hitung_total_sks():
    jumlah = int(input("Jumlah Data: "))
    total_sks = 0

    print("--------- input sks ---------")
    for i in range(1, jumlah + 1):
        sks = int(input(f"SKS {i}: "))
        total_sks += sks

    return total_sks


def hitung_total_nilai():
    jumlah = int(input("Jumlah Data: "))
    total_nilai = 0

    print("--------- input sks ---------")
    sks_list = []
    for i in range(1, jumlah + 1):
        sks = int(input(f"SKS {i}: "))
        sks_list.append(sks)

    print("--------- input nilai mahasiswa ---------")
    for i in range(1, jumlah + 1):
        nilai = float(input(f"Nilai {i}: "))
        label = konversi_nilai_ke_label(nilai)
        bobot = konversi_label_ke_bobot(label)
        total_nilai += bobot * sks_list[i - 1]

    return total_nilai


def hitung_ips():
    jumlah = int(input("Jumlah Data: "))
    total_sks = 0
    total_bobot = 0

    print("--------- input sks ---------")
    sks_list = []
    for i in range(1, jumlah + 1):
        sks = int(input(f"SKS {i}: "))
        sks_list.append(sks)
        total_sks += sks

    print("--------- input nilai mahasiswa ---------")
    for i in range(1, jumlah + 1):
        nilai = float(input(f"Nilai {i}: "))
        label = konversi_nilai_ke_label(nilai)
        bobot = konversi_label_ke_bobot(label)
        total_bobot += bobot * sks_list[i - 1]

    ips = total_bobot / total_sks
    return ips



