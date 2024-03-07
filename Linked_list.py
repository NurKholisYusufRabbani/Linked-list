import time

class Node:
    def __init__(self, menu, price, quantity=1):
        self.menu = menu  #Nama menu
        self.price = price  #Harga menu
        self.quantity = quantity  #Jumlah pesanan
        self.next = None  #Pointer ke node berikutnya

class LinkedList:
    def __init__(self):
        self.head = None  #Inisialisasi kepala linked list

    def add_menu(self, menu, price, quantity=1):
        new_node = Node(menu, price, quantity)  #Membuat node baru
        if not self.head:
            #Menjadikan node baru sebagai kepala jika linked list masih kosong
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  #Menambahkan node baru di belakang linked list
            

    def display_menu(self):
        current = self.head
        count = 1
        while current:
            #Menampilkan menu, jumlah, dan total harga
            print(f"{count}. {current.menu} ({current.quantity} pcs) - {current.price * current.quantity} rupiah")
            current = current.next
            count += 1

    def calculate_total_price(self):
        total_price = 0
        current = self.head
        while current:
            total_price += current.price * current.quantity  # Menjumlahkan total harga pesanan
            current = current.next
        return total_price

#Daftar menu beserta harga
menu_dict = {
    "miexue ice cream": 5000,
    "boba shake": 16000,
    "mi sundae": 14000,
    "mi ganas": 11000,
    "creamy mango boba": 22000
}

#Inisialisasi linked list untuk menyimpan pesanan
menu_list = LinkedList()

#Fungsi untuk memesan menu dan menambahkannya ke dalam keranjang
def pesan_menu(menu, quantity=1):
    menu_lower = menu.lower()
    if menu_lower in menu_dict:
        menu_list.add_menu(menu, menu_dict[menu_lower], quantity)  #Menambahkan menu ke dalam keranjang
        print(f"{quantity} {menu} telah ditambahkan ke keranjang")

    else:
        print("Maaf, menu tidak tersedia")

#fungsi untuk menampilkan pesanan yang sudah ditambahkan kedalam keranjang
def tampilkan_pesanan():
    print("daftar pesanan:")
    menu_list.display_menu()

#fungsi untuk menghitung total harga pesanan 
def bayar_pesanan():
    total_price =
menu_list.calculate_total_price()
    print("menghitung total...")
    time.sleep(1)
    print(f"total biaya yang harus dibayar adalah:{total_price} rupiah. terima kasih sudah memesan!")

#interaksi dengan pengguna 
    print("selamat datang di miexue! silahkan memesan menu:")
while true:
    print("\npilihan menu:")
    for menu, price in
menu_dict.items():
    print(f"{menu.capitalize()}-{price}rupiah")

    pesanan = input("\nMasukkan nama menu yang ingin dipesan atau 'selesai' untuk menyelesaikan pesanan: ").lower()
    if pesanan == 'selesai':
        break
        
    elif pesanan in menu_dict:
        try:
            jumlah = int(input(f"Masukkan jumlah {pesanan.capitalize()} yang ingin dipesan: "))
            pesan_menu(pesanan, jumlah)
        except ValueError:
            print("Mohon masukkan angka untuk jumlah pesanan.")

    else:
        print("Maaf, menu tidak tersedia.")

    #Menampilkan pesanan dan menghitung total harga
    print("\nRangkuman Pesanan :")
    tampilkan_pesanan()
    bayar_pesanan()
    
