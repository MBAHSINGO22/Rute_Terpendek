import numpy as np

# Nama kecamatan
kecamatan = [
    "Danurejan", "Gedongtengen", "Gondokusuman", "Gondomanan", "Jetis",
    "Kotagede", "Kraton", "Mantrijeron", "Mergangsan", "Ngampilan",
    "Pakualaman", "Tegalrejo", "Umbulharjo", "Wirobrajan"
]

# Data jarak antar kecamatan (dalam km, sebagai contoh)
distances = np.array([
    #  D  Gg  Gk  Gn  J  Kd  Kr  Mj  Mg  N  P  Tg  Ub  W
    [ 0,  2,  4,  1,  5,  7,  8,  3,  2,  4,  6,  9, 10, 4], # D
    [ 2,  0,  3,  4,  6,  5,  7,  2,  3,  5,  7,  8, 11, 3], # Gg
    [ 4,  3,  0,  5,  7,  3,  8,  1,  2,  3,  5,  6,  9, 3], # Gk
    [ 1,  4,  5,  0,  6,  8,  9,  4,  3,  4,  6, 10, 11, 5], # Gn
    [ 5,  6,  7,  6,  0,  9, 10,  6,  5,  4,  8, 12, 13, 7], # J
    [ 7,  5,  3,  8,  9,  0, 12,  4,  3,  5,  6,  9, 11, 3], # Kd
    [ 8,  7,  8,  9, 10, 12,  0,  9,  6,  7,  8, 13, 15, 8], # Kr
    [ 3,  2,  1,  4,  6,  4,  9,  0,  2,  3,  5,  7,  8, 4], # Mj
    [ 2,  3,  2,  3,  5,  3,  6,  2,  0,  4,  6,  8, 10, 2], # Mg
    [ 4,  5,  3,  4,  4,  5,  7,  3,  4,  0,  3,  9, 11, 5], # N
    [ 6,  7,  5,  6,  8,  6,  8,  5,  6,  3,  0, 10, 12, 6], # P
    [ 9,  8,  6, 10, 12,  9, 13,  7,  8,  9, 10,  0,  4, 8], # Tg
    [10, 11,  9, 11, 13, 11, 15,  8, 10, 11, 12,  4,  0, 9], # Ub
    [ 4,  3,  3,  5,  7,  3,  8,  4,  2,  5,  6,  8,  9, 0]  # W
])

n = len(distances)
visited = [False] * n
route = [0]  # Mulai dari kecamatan pertama (index 0)
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
    print(f"{kecamatan[route[i]]} -> {kecamatan[route[i + 1]]} ({distances[route[i]][route[i + 1]]} km)")
print(f"Total jarak: {total_distance} km")
