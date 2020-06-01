print('\n','===Selamat Datang di Jasa Pengiriman Paket MAJU JAYA===','\n')

iterasi = True
hitung = 0
paket_1 = 500
paket_2 = 400
paket_3 = 300



while iterasi == True:
    hitung += 1
    nama_pengirim = input('Nama pengirim: ')
    nama_penerima = input('Nama penerima: ')
    alamat = input('Alamat penerima: ')
    berat_paket = int(input('Berapa berat paket(dalam kg): '))
    jarak = int(input('Berapa jarak pengiriman(dalam km): '))
    #durasi_kirim=int(input('Berapa lama paket sampai(dalam hari): '))
    print('Pilihan Paket Waktu Pengiriman:')
    print('1. Paket Kilat: 1-2 hari pengiriman')
    print('2. Paket Biasa: 3-4 hari pengiriman')
    print('3. Paket Santai: >=5 hari pengiriman')
    jp = input('pilih jenis paket:')
    if jp == '1':
        print('\n')
        print('Nama pengirim:', nama_pengirim)
        print('Nama penerima:', nama_penerima)
        print('Alamat penerima:', alamat)
        print('biaya ongkir dasar= Rp. ', paket_1,'per km' )
        biaya = paket_1*jarak
        print ('\n','Jumlah ongkos kirim: Rp. ',(biaya*1)+biaya*((berat_paket-1)*0.7))
    elif jp == '2':
        print('\n')
        print('Nama pengirim:', nama_pengirim)
        print('Nama penerima:', nama_penerima)
        print('Alamat penerima:', alamat)
        print('biaya ongkir dasar= Rp. ', paket_2, 'per km' )
        biaya = paket_2*jarak
        print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
    elif jp == '3':
        print('\n')
        print('Nama pengirim:', nama_pengirim)
        print('Nama penerima:', nama_penerima)
        print('Alamat penerima:', alamat)
        print('biaya ongkir dasar= Rp. ', paket_3, 'per km' )
        biaya = paket_3*jarak
        print ('\n','Jumlah ongkos kirim: Rp. ',(biaya*1)+biaya*((berat_paket-1)*0.7))
    #jenis_barang = input('Apakah barangnya elektronik/non elektronik : ')
    print('A. Elektronik Ringan: 1-2 kg')
    print('B. Elektronik Sedang: 3-4 kg')
    print('C. Elektronik Berat: >=5 kg')
    jb = input ('pilih jenis barang: ')
    if jb == 'A':
        print('A. Elektronik Ringan: 1-2 kg')
        total_biaya = biaya+30000
        print('\n', 'Jumlah biaya yang harus dibayar: Rp. ', total_biaya)
    elif jb == 'B':
        print('B. Elektronik Sedang: 3-4 kg')
        total_biaya = biaya+45000
        print('\n', 'Jumlah biaya yang harus dibayar: Rp. ', total_biaya)
    elif jb == 'B':
        print('C. Elektronik Berat: >=5 kg')
        total_biaya = biaya+60000
        print('\n', 'Jumlah biaya yang harus dibayar: Rp. ', total_biaya)
    #print ('\n','Jumlah biaya yang harus dibayar: Rp',total_biaya)
    #print ("Total transaksi hari ini: " + str(hitung),'\n')
    o_t = input('Ada traksaksi lain?(y/n) ')
    if o_t != 'y':
        iterasi == False
        break
print ('Total transaksi hari ini: ' + str(hitung),'\n')
print ('Terima kasih sudah menggunakan jasa pengiriman kami')
print ('==Jasa Pengiriman Paket MAJU JAYA==')
    
