from flask import Flask, render_template, request, redirect
from utils import *

app = Flask(__name__)

# ================= MENU UTAMA =================
@app.route("/", methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        p = request.form["pilihan"]

        # CEK BIODATA UNTUK MENU 2-5
        if p in ["2", "3", "4", "5"] and not biodata_lengkap():
            return redirect("/peringatan")
        
        if p == "1":
            return redirect("/biodata")
        elif p == "2":
            return redirect("/sks")
        elif p == "3":
            return redirect("/nilai")
        elif p == "4":
            return redirect("/lihat-nilai")
        elif p == "5":
            return redirect("/ip")

    return render_template("menu.html")


# ================= BIODATA (SUBMENU) =================
@app.route("/biodata", methods=["GET", "POST"])
def biodata_menu():
    if request.method == "POST":
        p = request.form["pilihan"]

        if p == "1":
            return redirect("/biodata/lihat")
        elif p == "2":
            return redirect("/biodata/input")

    return render_template("biodata_menu.html")


@app.route("/biodata/lihat")
def biodata_lihat():
    return render_template(
        "biodata_lihat.html",
        biodata=get_biodata()
    )


@app.route("/biodata/input", methods=["GET", "POST"])
def biodata_input():
    if request.method == "POST":
        set_biodata(
            request.form["nama"],
            request.form["nim"]
        )
        return redirect("/")
    return render_template("biodata_input.html")


# ================= SKS =================
@app.route("/sks", methods=["GET", "POST"])
def sks():
    if request.method == "POST":
        data = list(map(int, request.form["sks"].split()))
        set_sks(data)
        return redirect("/")
    return render_template("sks.html")


# ================= NILAI =================
@app.route("/nilai", methods=["GET", "POST"])
def nilai():
    if request.method == "POST":
        jenis = request.form["jenis"]
        nilai = request.form["nilai"].split()

        if jenis == "angka":
            set_nilai_dari_angka(list(map(float, nilai)))
        else:
            set_nilai_dari_huruf(nilai)

        return redirect("/")

    return render_template("nilai.html")


# ================= LIHAT NILAI =================
@app.route("/lihat-nilai")
def lihat_nilai():
    return render_template(
        "lihat_nilai.html",
        biodata=get_biodata(),
        nilai=get_nilai_huruf()
    )


# ================= IP =================
@app.route("/ip")
def ip():
    return render_template(
        "ip.html",
        biodata=get_biodata(),
        ip=round(hitung_ip(), 2)
    )

@app.route("/peringatan")
def peringatan():
    return render_template("peringatan.html")



if __name__ == "__main__":
    app.run(debug=True)
