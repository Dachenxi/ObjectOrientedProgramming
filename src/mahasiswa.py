class Mahasiswa:
    def __init__(self, nim, nama, prodi, angkatan, dospem):
        if not nim.isdigit():
            raise ValueError("NIM harus berupa angka.")
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan
        self.dospem = dospem
    
    def __str__(self):
        return (f"NIM: {self.nim}\n"
                f"Nama: {self.nama}\n"
                f"Prodi: {self.prodi}\n"
                f"Angkatan: {self.angkatan}\n"
                f"Dosen Pembimbing: {self.dospem}")

    def update_prodi(self, new_prodi):
        self.prodi = new_prodi

    def ganti_dospem(self, new_dospem):
        self.dospem = new_dospem
