import sys
import random
import csv

a= 'Paket ini diasuransikan'
b= 'Paket ini diasuransikan'
c= 'Paket ini diasuransikan'
d= 'Paket ini tidak diasuransikan'
iya= 'dan diberi kemasan pelindung'
tidak= 'dan tidak diberi lapisan pelindung'


print('\n','===Selamat Datang di Jasa Pengiriman Paket ANUGRAH===','\n')
print('...........................................................')
iterasi = True
hitung = 0
paket_jne = [1500, 1000, 500]
paket_tiki = [500,400,300]
paket_sc = [2000,1000,500]
dict_paket = {'A':paket_jne, 'B':paket_tiki, 'C': paket_sc}
total_biaya = 0
dict_ket1 = {'Y':iya, 'N':tidak}
dict_ket2 = {'1':a, '2':b, '3':c, '4':d}
from datetime import datetime
current = datetime.now()

tahun = current.year
bulan = current.month
hari = current.day
print('Masukkan Data Pengiriman Anda')

while iterasi:
    hitung += 1
    print()
    print('===========================================================')
    print('BIODATA')
    print('===========================================================')


    try:
        nama_pengirim=str(input('Nama pengirim: '))
        if nama_pengirim == '':
            raise ValueError
        elif nama_pengirim == ' ':
            raise ValueError
        elif not str.isalpha():
            raise ValueError
    except Exception:
        print("\nError: Input tidak sesuai")
        nama_pengirim=str(input('Nama pengirim: '))
        
    try:
        nama_penerima=str(input('Nama penerima: '))
        if nama_penerima == '':
            raise ValueError
        elif nama_penerima == ' ':
            raise ValueError
        elif not str.isalpha():
            raise ValueError
    except Exception:
        print("\nError: Input tidak sesuai")
        nama_penerima=str(input('Nama penerima: '))

    print()
    print('DETAIL ALAMAT PENERIMA')
    print('----------------------')
    try:
        rt_rw=input('RT/RW: ')
        if rt_rw =='':
            raise ValueError
    except Exception:
        print("\nError: Wajib diisi ")
        rt_rw=input('RT/RW: ')
    try:
        desa_jln=input('Desa/Jalan: ')
        if desa_jln=='':
            raise ValueError
    except Exception:
        print("\nError: Wajib diisi ")
        desa_jln=input('Desa/Jalan: ')

    try:
        kecamatan=input('Kecamatan: ')
        if kecamatan=='':
            raise ValueError
    except Exception:
        print("\nError: Wajib diisi ")
        kecamatan=input('Kecamatan: ')
    try:
        kabupaten=input('Kabupaten: ')
        if kabupaten == '':
            raise ValueError
    except Exception:
        print("\nError: Wajib diisi ")
        kabupaten=input('Kabupaten: ')
    try:
        provinsi=input('Provinsi: ')
        if provinsi == '':
            raise ValueError
    except Exception:
        print("\nError: Wajib diisi ")
        provinsi=input('Provinsi: ')
    try:
        kode_pos=input('Kode Pos: ')
        if kode_pos == '':
            raise ValueError
    except Exception:
        print("\nError: Wajib diisi ")
        kode_pos=input('Kode Pos: ')
    try:
        no_penerima=input('No Telp penerima: ')
        if no_penerima=='':
            raise ValueError
    except Exception:
        print("\nError: Wajib diisi ")
        no_penerima=input('No Telp penerima: ')
    
    print("")
    with open ('daftardaerah.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row [1] == kabupaten:
                print("Jarak(km) : ",row[2])
                jarak= int(row[2])

        
    jenis= input('Paket Surat (Y)/ Non Surat (N): ')
    if jenis== 'Y' or 'y':
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
            print()
            print('Pilihan Paket Waktu Pengiriman:')
            print('1. Paket Kilat: 1-2 hari pengiriman')
            print('2. Paket Biasa: 3-4 hari pengiriman')
            print('3. Paket Santai: >=5 hari pengiriman')
            jp= input('pilih jenis paket(1/2/3): ')
            if jp == '1':
                total_ongkir = dict_paket[ja][0] * jarak
                break
            elif jp == '2':
                total_ongkir = dict_paket[ja][1] * jarak
                break
            elif jp == '3':
                total_ongkir = dict_paket[ja][2] * jarak
                break
        no_resi=random.randint(1000, 2000)
        print()
        print('===========================================================')
        print ('BERIKUT DATA PEMESANAN ANDA')
        print('===========================================================')
        print()
        print ('Nama pengirim:', nama_pengirim)
        print ('Nama penerima:', nama_penerima)
        print ('Alamat penerima:', desa_jln, kecamatan, kabupaten, provinsi, 'RT/RW:', rt_rw, 'Kode Pos: ', kode_pos)
        print('No Telp penerima:', no_penerima)
        print('Waktu Pengiriman: ',':',hari,':',bulan,':',tahun)
        print('No Resi: ',no_resi)
        print ('Jumlah ongkos kirim: Rp',total_ongkir)
        print('...........................................................')
        print ("Total transaksi hari ini: " + str(hitung),'\n')
        o_t= input('Ada traksaksi lain?(Y/N) ').upper()
        if o_t == 'Y'or 'y':
            total_biaya += total_ongkir
            print()
            pass
        elif o_t == 'N'or 'n':
            total_biaya += total_ongkir
            iterasi = False
            
    if jenis== 'N'or'n':
        print()
        print('===========================================================')
        print('DETAIL BARANG')
        print('===========================================================')
        berat_paket= float(input('Berapa berat paket(dlm kg): '))
        panjang_paket= float(input('Berapa panjang paket(dlm cm): '))
        lebar_paket= float(input('Berapa lebar paket(dlm cm): '))
        tinggi_paket= float(input('Berapa tinggi paket(dlm cm): '))
        #durasi_kirim=int(input('Berapa lama paket sampai(dlm hari): '))
    
        berat_konversi= float(((panjang_paket)*(lebar_paket)*(tinggi_paket))/(6000))
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
            print()
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
            ket1 = dict_ket1[kemas]
        elif kemas =='N':
            biaya_1 =biaya
            jumlah_ongkir = round(((biaya_1*1)+biaya_1*((berat-1)*0.7)),1)
            ket1 = dict_ket1[kemas]
    
        print('\n')   
        print('Pilih jenis barang:')
        print('1. Elektronik Ringan: 1-2 kg')
        print('2. Elektronik Sedang: 3-4 kg')
        print('3. Elektronik Berat: >=5 kg')
        print('4. Non Elektronik')
        
        jb= input('Pilih jenis barang (1/2/3/4): ')      
        if jb== '1':
            total_ongkir = jumlah_ongkir+30000
            ket2 = dict_ket2[jb]
        elif jb== '2':
            total_ongkir = jumlah_ongkir+45000
            ket2 = dict_ket2[jb]
        elif jb== '3':
            total_ongkir = jumlah_ongkir+60000
            ket2 = dict_ket2[jb]
        elif jb== '4':
            total_ongkir = jumlah_ongkir
            ket2 = dict_ket2[jb]
        
        if berat >= 200:
            total_ongkir_1 = total_ongkir+(total_ongkir)
        elif berat >= 150:
            total_ongkir_1 = total_ongkir+(total_ongkir*0.5)
        elif berat >= 100:
            total_ongkir_1 = total_ongkir+(total_ongkir*0.35)
        elif berat >= 75:
            total_ongkir_1 = total_ongkir+(total_ongkir*0.25)
        else:
            total_ongkir_1 = total_ongkir
        
        no_resi=random.randint(1000, 2000)
        
        print()
        print('===========================================================')
        print ('BERIKUT DATA PEMESANAN ANDA')
        print('===========================================================')
        print()
        print ('Nama pengirim:', nama_pengirim)
        print ('Nama penerima:', nama_penerima)
        print ('Alamat penerima:', desa_jln, kecamatan, kabupaten, provinsi, 'RT/RW:', rt_rw, 'Kode Pos: ', kode_pos)
        print('No Telp penerima:', no_penerima)
        print('Waktu Pengiriman: ',hari,':',bulan,':',tahun)
        print('No Resi: ', no_resi)
        print ('Jumlah ongkos kirim: Rp',total_ongkir_1)
        print()
        print ('*Keterangan: ', ket2, ket1)
        print('...........................................................')
        print ("Total transaksi hari ini: " + str(hitung),'\n')
        o_t= input('Ada traksaksi lain?(Y/N) ').upper()
        if o_t == 'Y'or'y':
            total_biaya += total_ongkir_1
            print()
            pass
        elif o_t == 'N'or'n':
            total_biaya += total_ongkir_1
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
