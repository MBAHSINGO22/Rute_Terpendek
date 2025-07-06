import numpy as np

# Nama kota/kabupaten di Jawa Tengah
kota_kabupaten = [
    "Banjarnegara", "Banyumas", "Batang", "Blora", "Boyolali",
    "Brebes", "Cilacap", "Demak", "Grobogan", "Jepara",
    "Karanganyar", "Kebumen", "Kendal", "Klaten", "Kudus",
    "Magelang", "Pati", "Pekalongan", "Pemalang", "Purbalingga",
    "Purworejo", "Rembang", "Semarang", "Sragen", "Sukoharjo",
    "Tegal", "Temanggung", "Wonogiri", "Wonosobo", "Kota Magelang",
    "Kota Pekalongan", "Kota Salatiga", "Kota Semarang", "Kota Surakarta",
    "Kota Tegal"
]

# Data jarak antar kota/kabupaten (dalam km, sebagai contoh)
# Matriks jarak harus berukuran 35x35 sesuai dengan jumlah kota/kabupaten
# Untuk kesederhanaan, berikut adalah contoh matriks jarak kecil, silakan sesuaikan dengan data sebenarnya
distances = np.random.randint(50, 500, size=(35, 35))
np.fill_diagonal(distances, 0)  # Jarak ke diri sendiri adalah 0

n = len(distances)
visited = [False] * n
route = [0]  # Mulai dari kota/kabupaten pertama (index 0)
visited[0] = True
total_distance = 0

for _ in range(n - 1):
    last = route[-1]
    next_distances = [(distances[last][j], j) for j in range(n) if not visited[j]]
    next_city = min(next_distances)[1]
    total_distance += distances[last][next_city]
    route.append(next_city)
    visited[next_city] = True

# Kembali ke titik awal
total_distance += distances[route[-1]][0]
route.append(0)

# Tampilkan hasil
print("Rute terpendek :")
for i in range(len(route) - 1):
    print(f"{kota_kabupaten[route[i]]} -> {kota_kabupaten[route[i + 1]]} ({distances[route[i]][route[i + 1]]} km)")
print(f"Total jarak: {total_distance} km")
