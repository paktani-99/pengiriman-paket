print('\n','===Selamat datang di jasa pengiriman paket ANUGRAH===','\n')
iterasi = True
hitung = 0
paket_1JNE= 1500
paket_2JNE= 1000
paket_3JNE= 500
paket_1TIKI= 500
paket_2TIKI= 400
paket_3TIKI= 300
paket_1SC= 2000
paket_2SC= 1000

while iterasi == True:
    hitung += 1
    nama=input('Nama pengirim: ')
    nama_1=input('Nama penerima: ')
    alamat=input('Alamat penerima: ')
    berat_paket= int(input('Berapa berat paket(dlm kg): '))
    jarak= int(input('Berapa jarak pengiriman(dlm km): '))
    #durasi_kirim=int(input('Berapa lama paket sampai(dlm hari): '))
    print('Pilihan Agent Pengiriman:')
    print('A. Agent : JNE')
    print('B. Agent : TIKI')
    print('C. Agent : SiCepat')
    ja= input('pilih jenis agent paket:')
    if ja=='A':
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
            print('biaya ongkir dasar= Rp ',paket_1JNE,'per km' )
            biaya= paket_1JNE*jarak
            print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
        elif jp == '2':
            print('\n')
            print('Nama pengirim:',nama)
            print('Nama penerima:',nama_1)
            print('Alamat penerima:',alamat)
            print('biaya ongkir dasar= Rp ',paket_2JNE,'per km' )
            biaya= paket_2JNE*jarak
            print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
        elif jp == '3':
            print('\n')
            print('Nama pengirim:',nama)
            print('Nama penerima:',nama_1)
            print('Alamat penerima:',alamat)
            print('biaya ongkir dasar= Rp ',paket_3JNE,'per km' )
            biaya = paket_3JNE*jarak
            print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
    elif ja=='B':
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
            print('biaya ongkir dasar= Rp ',paket_1TIKI,'per km' )
            biaya= paket_1TIKI*jarak
            print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
        elif jp == '2':
            print('\n')
            print('Nama pengirim:',nama)
            print('Nama penerima:',nama_1)
            print('Alamat penerima:',alamat)
            print('biaya ongkir dasar= Rp ',paket_2TIKI,'per km' )
            biaya= paket_2TIKI*jarak
            print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
        elif jp == '3':
            print('\n')
            print('Nama pengirim:',nama)
            print('Nama penerima:',nama_1)
            print('Alamat penerima:',alamat)
            print('biaya ongkir dasar= Rp ',paket_3TIKI,'per km' )
            biaya = paket_3TIKI*jarak
            print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
    elif ja=='C':
        print('Pilihan Paket Pengiriman:')
        print('1. Yakin besok sampe: 1 hari pengiriman')
        print('2. Yakin lusa sampe: 2 hari pengiriman')
        jp= input('pilih jenis paket:')
        if jp=='1':
            print('\n')
            print('Nama pengirim:',nama)
            print('Nama penerima:',nama_1)
            print('Alamat penerima:',alamat)
            print('biaya ongkir dasar= Rp ',paket_1SC,'per km' )
            biaya= paket_1SC*jarak
            print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
        elif jp == '2':
            print('\n')
            print('Nama pengirim:',nama)
            print('Nama penerima:',nama_1)
            print('Alamat penerima:',alamat)
            print('biaya ongkir dasar= Rp ',paket_2SC,'per km' )
            biaya= paket_2SC*jarak
            print ('\n','Jumlah ongkos kirim: Rp',(biaya*1)+biaya*((berat_paket-1)*0.7))
    
    #print ('\n','Jumlah ongkos kirim: Rp',(biaya*1))
    #print ("Total transaksi hari ini: " + str(hitung),'\n')
    o_t= input('Ada traksaksi lain?(y/n) ')
    if o_t != 'y':
        iterasi == False
        break
print ("Total transaksi hari ini: " + str(hitung),'\n')
    
