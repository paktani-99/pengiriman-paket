print('\n','===Selamat datang di jasa pengiriman paket ANUGRAH===','\n')
print('...............................................................')
iterasi = True
hitung = 0
paket_jne = [1500, 1000, 500]
paket_tiki = [500,400,300]
paket_sc = [2000,1000,500]
dict_paket = {'A':paket_jne, 'B':paket_tiki, 'C': paket_sc}
total_biaya = 0
print('Masukkan Data Pengiriman Anda')

while iterasi:
    hitung += 1
    print()
    print('===========================================================')
    print('BIODATA')
    print('===========================================================')
    nama_pengirim=input('Nama pengirim: ')
    nama_penerima=input('Nama penerima: ')
    alamat=input('Alamat penerima: ')
    no_penerima=input('No Telp penerima: ')
    jarak= float(input('Berapa jarak pengiriman (dlm km): '))
    print()
    print('===========================================================')
    print('DETAIL BARANG')
    print('===========================================================')
    berat_paket= float(input('Berapa berat paket(dlm kg): '))
    panjang_paket= float(input('Berapa panjang paket(dlm cm): '))
    lebar_paket= float(input('Berapa lebar paket(dlm cm): '))
    tinggi_paket= float(input('Berapa tinggi paket(dlm cm): '))
    #durasi_kirim=int(input('Berapa lama paket sampai(dlm hari): '))
    
    berat_konversi= float(((panjang_paket/100)*(lebar_paket/100)*(tinggi_paket/100))/(6000))
    if berat_paket >= berat_konversi:
        berat= berat_paket
    elif berat_paket < berat_konversi:
        berat= berat_konversi
    
    print()
    print('===========================================================')
    print('DETAIL PENGIRIMAN')
    print('===========================================================')
    print()
    print('Pilihan Jenis Agent Pengiriman:')
    print('A. Agent : JNE')
    print('B. Agent : TIKI')
    print('C. Agent : SiCepat')
    ja= input('pilih agent paket (A/B/C): ').upper()
    while True:
        print('Pilihan Paket Waktu Pengiriman:')
        print('1. Paket Kilat: 1-2 hari pengiriman')
        print('2. Paket Biasa: 3-4 hari pengiriman')
        print('3. Paket Santai: >=5 hari pengiriman')
        jp= input('pilih jenis paket(1/2/3): ')
        if jp == '1':
            biaya = dict_paket[ja][0] * jarak
            break
        elif jp == '2':
            biaya = dict_paket[ja][1] * jarak
            break
        elif jp == '3':
            biaya = dict_paket[ja][2] * jarak
            break
            
    print()
    print('===========================================================')
    print('ASURANSI')
    print('===========================================================')   
    kemas= input('Paket mudah pecah/makanan? (Y/N): ').upper()
    if kemas== 'Y':
        biaya_1 = biaya+500
        jumlah_ongkir = ((biaya_1*1)+biaya_1*((berat-1)*0.7))
    elif kemas =='N':
        biaya_1 =biaya
        jumlah_ongkir = round(((biaya_1*1)+biaya_1*((berat-1)*0.7)),1)
    
    print('\n')   
    print('Pilih jenis barang:')
    print('1. Elektronik Ringan: 1-2 kg')
    print('2. Elektronik Sedang: 3-4 kg')
    print('3. Elektronik Berat: >=5 kg')
    print('4. Non Elektronik')
    jb= input('Pilih jenis barang (1/2/3/4): ')
    if jb== '1':
        total_ongkir = jumlah_ongkir+30000
    elif jb== '2':
        total_ongkir = jumlah_ongkir+45000
    elif jb== '3':
        total_ongkir = jumlah_ongkir+60000
    elif jb== '4':
        total_ongkir = jumlah_ongkir

    print()
    print('===========================================================')
    print ('BERIKUT DATA PEMESANAN ANDA')
    print('===========================================================')
    print()
    print ('Nama pengirim:', nama_pengirim)
    print ('Nama penerima:', nama_penerima)
    print ('Alamat penerima:', alamat)
    print('No Telp penerima:', no_penerima)
    print ('Jumlah ongkos kirim: Rp',total_ongkir)
    print('...........................................................')
    print ("Total transaksi hari ini: " + str(hitung),'\n')
    o_t= input('Ada traksaksi lain?(Y/N) ').upper()
    if o_t == 'Y':
        total_biaya += total_ongkir
        print()
        pass
    elif o_t == 'N':
        total_biaya += total_ongkir
        iterasi = False

print()
print('...........................................................')
print()
print ('Jumlah transaksi hari ini: ' + str(hitung),'\n')
print ("Total transaksi hari ini: " + str(total_biaya),'\n')
print ('==========================================================')
print ('   Terima kasih sudah menggunakan jasa pengiriman kami    ')
print ('            Jasa Pengiriman Paket ANUGRAH                 ')
print ('==========================================================')
