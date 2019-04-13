# UAS Bahasa Pemrograman 1


1. Buka link ini https://github.com/abuazzam/uaspy , lalu fork <br/>
![alt text](https://raw.githubusercontent.com/arkyana/uaspy/master/ss/1.png)

2. lalu otomatis akan link ke akun yg saya punya, (harus sudah login), lalu pilih clone or download, lalu copy link ini<br/>
![alt text](https://raw.githubusercontent.com/arkyana/uaspy/master/ss/2.png)

3.setelah itu git bash di folder lokal, lalu ketik "git clone" dan pastekan link yg tadi<br/>
![alt text](https://raw.githubusercontent.com/arkyana/uaspy/master/ss/3.png)


4. open project menggunakan pycharm, lalu setting environment location seperti gambar berikut </br>
![alt text](https://raw.githubusercontent.com/arkyana/uaspy/master/ss/5.png)

5. install packages pygame, berikut cara-caranya </br>
![alt text](https://raw.githubusercontent.com/arkyana/uaspy/master/ss/6.png)

6. cek apakah packages sudah terinstall apa belum dengan menegtikan "pip list" di terminal </br>
![alt text](https://raw.githubusercontent.com/arkyana/uaspy/master/ss/7.png)

7. Buat class utama dengan menurunkan dari class BaseApp dengan nama App (di main.py), kurang lebih begini kodingnya </br>
   
from core.baseapp import BaseApp

class App(BaseApp):
    def __init__(self) :
        BaseApp.__init__(self)

    def on_playing(self):
        self.check_collision(self.player, self.enemies)

<br/>

![alt text](https://raw.githubusercontent.com/arkyana/uaspy/master/ss/langkah.png)

8. run program, dan beginilah hasil screenshotnya </br>
![alt text](https://raw.githubusercontent.com/arkyana/uaspy/master/ss/hasil.png)
