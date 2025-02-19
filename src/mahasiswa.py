class Mahasiswa:
    def __init__(self, nim, nama, prodi, angkatan, dospem):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan
        self.dospem = dospem
    
    def __str__(self):
        return f"""Nim : {self.nim}\nNama : {self.nama}\nProdi : {self.prodi}\nAngkatan : {self.angkatan}\nDosen Pembimbing : {self.dospem}"""