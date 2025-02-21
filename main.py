from src import Mahasiswa
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QHBoxLayout, QHeaderView

class MahasiswaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manajemen Data Mahasiswa")
        self.setGeometry(100, 100, 800, 600)

        # Data Mahasiswa (contoh awal)
        self.data_mahasiswa = [
            ["123456", "Budi Santoso", "Teknik Informatika", "2021", "Dr. Andi"],
            ["654321", "Siti Aminah", "Sistem Informasi", "2020", "Dr. Sari"],
        ]

        # Layout utama
        layout = QVBoxLayout()

        # Input pencarian
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Cari berdasarkan NIM atau Nama...")
        layout.addWidget(self.search_input)

        # Tombol cari
        search_button = QPushButton("Cari")
        search_button.clicked.connect(self.search_data)
        layout.addWidget(search_button)

        # Tabel untuk menampilkan data
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["NIM", "Nama", "Prodi", "Angkatan", "Dosen Pembimbing"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_data_to_table(self.data_mahasiswa)
        layout.addWidget(self.table)

        # Widget utama
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_data_to_table(self, data):
        """Memuat data mahasiswa ke tabel."""
        self.table.setRowCount(len(data))
        for row, mahasiswa in enumerate(data):
            for col, value in enumerate(mahasiswa):
                self.table.setItem(row, col, QTableWidgetItem(value))

    def search_data(self):
        """Mencari data mahasiswa berdasarkan input pencarian."""
        search_text = self.search_input.text().lower()
        filtered_data = [mhs for mhs in self.data_mahasiswa if search_text in mhs[0].lower() or search_text in mhs[1].lower()]
        self.load_data_to_table(filtered_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MahasiswaApp()
    window.show()
    sys.exit(app.exec_())
