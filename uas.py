print('\n','===Selamat datang di jasa pengiriman paket ANUGRAH===','\n')
iterasi = True
hitung = 0
paket_1= 500
paket_2= 400
paket_3= 300



while iterasi == True:
    hitung += 1
    nama=input('Nama pengirim: ')
    nama_1=input('Nama penerima: ')
    alamat=input('Alamat penerima: ')
    berat_paket= int(input('Berapa berat paket(dlm kg): '))
    jarak= int(input('Berapa jarak pengiriman: '))
    #durasi_kirim=int(input('Berapa lama paket sampai(dlm hari): '))
    print('Pilihan Paket Pengiriman:')
    print('1. Yakin besok sampe: 1 hari pengiriman')
    print('2. Yakin lusa sampe: 2 hari pengiriman')
    print('3. Yakin besok^3 sampe: 3 hari pengiriman')
    jp= input('pilih jenis paket:')
    if jp=='1':
        print('\n')
        print('Nama pengirim:',nama)
        print('Nama penerima:',nama_1)
        print('Alamat penerima:',alamat)
        print('biaya ongkir dasar= Rp ',paket_1,'per km' )
        biaya= paket_1*jarak
        print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
    elif jp == '2':
        print('\n')
        print('Nama pengirim:',nama)
        print('Nama penerima:',nama_1)
        print('Alamat penerima:',alamat)
        print('biaya ongkir dasar= Rp ',paket_2,'per km' )
        biaya= paket_2*jarak
        print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
    elif jp == '3':
        print('\n')
        print('Nama pengirim:',nama)
        print('Nama penerima:',nama_1)
        print('Alamat penerima:',alamat)
        print('biaya ongkir dasar= Rp ',paket_3,'per km' )
        biaya = paket_3*jarak
        print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
    #print ('\n','Jumlah ongkos kirim: Rp',(biaya*1))
    #print ("Total transaksi hari ini: " + str(hitung),'\n')
    o_t= input('Ada traksaksi lain?(y/n) ')
    if o_t != 'y':
        iterasi == False
        break
print ("Total transaksi hari ini: " + str(hitung),'\n')
    
