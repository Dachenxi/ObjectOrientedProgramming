from rich import print
from rich.panel import Panel
from rich.columns import Columns
from src import Mahasiswa

mhs1 = Mahasiswa("M0001", "Budi", "Teknik Informatika", 2020, "Pak Joko")
mhs2 = Mahasiswa("M0002", "Susi", "Sistem Informasi", 2020, "Bu Rina")
mhs3 = Mahasiswa("M0003", "Rudi", "Teknik Informatika", 2020, "Pak Joko")
mhs4 = Mahasiswa("M0004", "Siti", "Sistem Informasi", 2020, "Bu Rina")

list_mhs = [mhs1, mhs2, mhs3, mhs4]

panel = [Panel(str(mhs), title=f"Mahasiswa {mhs.nim}", expand=False) for mhs in list_mhs]
print(Columns(panel, equal=True))