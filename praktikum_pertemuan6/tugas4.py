daftar_nama_teman = []

print("Silakan masukkan 5 nama teman Anda:")
for i in range(5):
    nama = input(f"Nama teman ke-{i + 1}: ")
    daftar_nama_teman.append(nama)

print("\nDaftar 5 Nama Teman Anda")
for nama in daftar_nama_teman:
    print(f"- {nama}")