import tkinter as tk


class TampilanAntarmuka:
    def _init_(self) -> None:
        self.root = tk.Tk()

        self.title_program = tk.Label(
            self.root, text="Sistem Deteksi Hoax", font=("Arial", 28)
        )
        self.title_program.pack()

        self.input_label = tk.Label(
            self.root, text="silahkan masukan judul berita anda"
        )
        self.input_label.pack()
        self.input_judul = tk.Entry(self.root)
        self.input_judul.pack()

        self.label_hasil = tk.Label(self.root, text="berita anda adalah")
        self.label_hasil.pack()

        self.cek_button = tk.Button(self.root, text="Cek")
        self.cek_button.pack()
        self.reset_button = tk.Button(self.root, text="Reset")
        self.reset_button.pack()

        self.root.mainloop()

    def cek_judul(self):
        print(self.input_judul.get())


def main():
    TampilanAntarmuka()


if __name__ == "__main__":
    main()