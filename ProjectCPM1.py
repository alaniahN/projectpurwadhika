recordData = [ #list penyimpanan data dengan sampel data
     {"NomorID": "01",
     "Nama": "Mia", 
     "Domisili": "Jakarta", 
     "JudulBuku": "Matematika Dasar", 
     "WaktuPeminjaman": "5 Hari"},

     {"NomorID": "02", 
     "Nama": "Maya", 
     "Domisili": "Bandung", 
     "JudulBuku": "Kumpulan Cerpen 2021", 
     "WaktuPeminjaman": "5 Hari"}
     ]

def recordBuku(): #menu read data: menampilkan data yang tersimpan dalam program
    print("=====RECORD DATA PEMINJAMAN BUKU=====")
    print('''
    1. Record Seluruh Data Peminjaman Buku
    2. Record Spesifik Data
    3. Kembali ke Menu Utama
    ''')
    inputUser = input("Masukkan pilihan yang anda inginkan: ")
    print("\n")
    if inputUser == "1":
        numData = 1
        for i in recordData:
            print(str(numData) + ". Nomor ID: {}, Nama: {}, Domisili: {}, Judul Buku: {}, Waktu Peminjaman: {}"
            .format(i['NomorID'], i['Nama'], i['Domisili'], i['JudulBuku'], i['WaktuPeminjaman']))
            numData += 1
        print("\n")
        recordBuku()
    elif inputUser == "2":
        askID = input("Masukkan ID data yang ingin anda lihat: ")
        print("\n")
        for i in recordData:
            if i['NomorID'] == askID:
                print("Nomor ID: {}, Nama: {}, Domisili: {}, Judul Buku: {}, Waktu Peminjaman: {}"
                .format(i['NomorID'], i['Nama'], i['Domisili'], i['JudulBuku'], i['WaktuPeminjaman']))
                break
        else: 
            print("---Data yang anda cari tidak ada.---")
        print("\n")
        recordBuku()
    elif inputUser == "3":
        print("\n")
        menuUtama()
    else:
        print("Pilihan yang anda inginkan tidak ada.")
        print("\n")
        recordBuku()
            
def tambahData(): #menu create data: menambahkan data ke dalam program
    print("=====PENAMBAHAN DATA PEMINJAMAN BUKU=====")
    print('''
    1. Tambah Data Peminjaman Buku
    2. Kembali ke Menu Utama
    ''')
    inputUser = input("Masukkan pilihan yang anda inginkan: ")
    print("\n")
    if inputUser == "1":
        addDict = dict()
        userInputID = input("Masukkan Nomor ID disini: ")
        userInputNama = input("Masukkan Nama Disini: ")
        userInputDom = input("Masukkan Domisili Disini: ")
        userInputJud = input("Masukkan Judul Buku Disini: ")
        userInputWaktu = input("Masukkan Waktu Peminjaman Disini: ")

        addDict['NomorID'] = userInputID
        addDict['Nama'] = userInputNama
        addDict['Domisili'] = userInputDom
        addDict['JudulBuku'] = userInputJud
        addDict['WaktuPeminjaman'] = userInputWaktu

        while True: 
            userConfirm = input("Apakah anda ingin menyimpan data? (Y/N): ")
            if userConfirm == "Y" or userConfirm == "y":
                recordData.append(addDict)
                print("Data tersimpan")
                tambahData()
                break
            elif userConfirm == "N" or userConfirm == "n":
                tambahData()
                break
    elif inputUser == "2":
        print("\n")
        menuUtama()
    else:
        print("Pilihan yang anda inginkan tidak ada.")
        print("\n")
        tambahData()

def updateData(): #menu update data: mengubah data yang ada dalam program
    print("=====UPDATE DATA PEMINJAMAN BUKU=====")
    print('''
    1. Update Data Peminjaman Buku
    2. Kembali ke Menu Utama
    ''')
    inputUser = input("Masukkan pilihan yang anda inginkan: ")
    if inputUser == "1":
        askID = input("Masukkan ID data yang ingin diubah: ")
        for i in recordData:
            if i["NomorID"] == askID:
                print("Nomor ID: {}, Nama: {}, Domisili: {}, Judul Buku: {}, Waktu Peminjaman: {}"
                .format(i['NomorID'], i['Nama'], i['Domisili'], i['JudulBuku'], i['WaktuPeminjaman']))
                while True: 
                    userConfirm = input("Tekan Y jika ingin lanjut mengupdate data atau N jika ingin cancel update: " )
                    if userConfirm == "Y":
                        changeCol = input("Masukkan kolom/keterangan yang ingin diedit: ")
                        if changeCol == "Nomor ID":
                            print("Nomor ID tidak bisa diganti.")
                            updateData()
                        elif changeCol == "Nama":
                            changeName = input("Masukkan nama baru: ")
                            while True: 
                                userReCon = input("Apakah anda ingin menyimpan data? (Y/N): ")
                                if userReCon == "Y" or userReCon == "y":
                                    i["Nama"] = changeName
                                    print("Data telah diubah.")
                                    print("\n")
                                    updateData()
                                    break
                                elif userReCon == "N" or userReCon == "n":
                                    print("Data tidak terupdate.")
                                    break
                        elif changeCol == "Domisili":
                            changeName = input("Masukkan domisili baru: ")
                            while True: 
                                userReCon = input("Apakah anda ingin menyimpan data? (Y/N): ")
                                if userReCon == "Y" or userReCon == "y":
                                    i["Domisili"] = changeName
                                    print("Data telah diubah.")
                                    print("\n")
                                    updateData()
                                    break
                                elif userReCon == "N" or userReCon == "n":
                                    print("Data tidak terupdate.")
                                    break
                        elif changeCol == "Judul Buku":
                            changeName = input("Masukkan judul buku baru: ")
                            while True: 
                                userReCon = input("Apakah anda ingin menyimpan data? (Y/N): ")
                                if userReCon == "Y" or userReCon == "y":
                                    i["JudulBuku"] = changeName
                                    print("Data telah diubah.")
                                    print("\n")
                                    updateData()
                                    break
                                elif userReCon == "N" or userReCon == "n":
                                    print("Data tidak terupdate.")
                                    break
                        elif changeCol == "Waktu Peminjaman":
                            changeName = input("Masukkan waktu peminjaman yang baru: ")
                            while True: 
                                userReCon = input("Apakah anda ingin menyimpan data? (Y/N): ")
                                if userReCon == "Y" or userReCon == "y":
                                    i["WaktuPeminjaman"] = changeName
                                    print("Data telah diubah.")
                                    print("\n")
                                    updateData()
                                    break
                                elif userReCon == "N" or userReCon == "n":
                                    print("Data tidak terupdate.")
                                    break
                        else:
                            print("Data yang anda cari tidak ada.")
                            print("\n")
                            updateData()
                        
                    elif userConfirm == "N":
                        print("Data tidak terubah.")
                        updateData()
                             
        else:
            print("Data yang anda cari tidak ada.")
            updateData()
    elif inputUser == "2":
        menuUtama()
    else: 
        print("Input yang anda cari tidak ada.")
        updateData()

def hapusData(): #menu delete data: menghapus data yang ada di dalam program
    print("=====PENGHAPUSAN DATA PEMINJAMAN BUKU=====")
    print('''
    1. Hapus Data Peminjaman Buku
    2. Kembali ke Menu Utama
    ''')
    inputUser = input("Masukkan pilihan yang anda inginkan: ")
    if inputUser == "1":
        askDelID = input("Masukkan ID data yang ingin di hapus: ")
        for data in recordData:
            if data["NomorID"] == askDelID:
                recordData.remove(data)
                print("Data telah terhapus.")
                print("\n")
                hapusData()
                break
        else:
            print("---Data yang anda cari tidak ada.---")
            print("\n")
            hapusData()
    elif inputUser == "2":
        print("\n")
        menuUtama()
    else: 
        print("Pilihan yang anda inginkan tidak ada.")
        print("\n")
        hapusData()

def menuUtama(): #menu utama untuk melihat pilihan dalam program
    print("==========PROGRAM DATA PEMINJAMAN BUKU==========") 
    print('''
    1. Record Data Peminjaman Buku
    2. Tambah Data Peminjaman Buku
    3. Update Data Peminjaman Buku
    4. Hapus Data Peminjaman Buku
    5. Exit
        ''')
    inputUserMenu = input("Masukkan pilihan yang anda inginkan: ")
    if inputUserMenu == "1":
        recordBuku()
    elif inputUserMenu == "2":
        tambahData()
    elif inputUserMenu == "3":
        updateData()
    elif inputUserMenu == "4":
        hapusData()
    elif inputUserMenu == "5":
        print("Terimakasih telah menggunakan program kami.")
    else: 
        print("Pilihan yang anda inginkan tidak ada.")
        menuUtama()
        
menuUtama()

