<h1 align="center">🗺️ Rute_Terpendek</h1>
<p align="center">
  <b>Optimasi Rute Perjalanan Menggunakan Python</b><br>
  <sub>Studi Kasus: Provinsi Jawa Tengah dan Kota Yogyakarta</sub>
</p>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Made%20by-MBAHSINGO22-blue)](https://github.com/MBAHSINGO22)

</div>

---

## 🧾 Ringkasan

**Rute_Terpendek** adalah repositori Python yang mengimplementasikan algoritma sederhana (greedy) untuk menentukan **rute terpendek** dalam mengunjungi sejumlah kota atau kecamatan secara melingkar (Traveling Salesman Problem versi dasar).

Dataset terdiri dari:
- 🏙️ 35 kota/kabupaten di **Jawa Tengah**
- 🏘️ 14 kecamatan di **Yogyakarta**

---

## 📂 Struktur Folder

```
Rute_Terpendek/
├── JawaTengah.py      # Rute terpendek antar kota di Jawa Tengah
├── Yogyakarta.py      # Rute terpendek antar kecamatan di Yogyakarta
└── README.md          # Dokumentasi proyek
```

---

## ⚙️ Algoritma

Program menggunakan pendekatan **greedy algorithm**:
- Mulai dari titik pertama
- Pilih kota terdekat berikutnya yang belum dikunjungi
- Ulangi hingga semua kota/kecamatan dikunjungi
- Kembali ke titik awal

---

## 🏙️ JawaTengah.py

🔹 Menentukan rute terpendek dari 35 kota/kabupaten di Jawa Tengah.  
🔹 Jarak antar kota dibangkitkan secara acak menggunakan `numpy`.  
🔹 Output berupa urutan rute dan total jarak tempuh.

---

## 🏘️ Yogyakarta.py

🔹 Menentukan rute terpendek dari 14 kecamatan di Yogyakarta.  
🔹 Menggunakan matriks jarak tetap berdasarkan nilai manual.  
🔹 Output berupa detail lintasan dan total jarak.

---

## ✅ Requirements

```bash
pip install numpy
```

---

## ✍️ Author

**MBAHSINGO22**  
🔗 [GitHub](https://github.com/MBAHSINGO22)

