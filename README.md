Catatan Versi

Rasa Version: 3.6.21


Rasa SDK Version: 3.6.2


Python Version: 3.9.13


Operating System: Windows 10


Python Path: C:\Users\ari\Desktop\Skripsi\chatbot\venv\Scripts\python.exe


Menjalankan Chatbot Rasa Lokal


1️⃣ Clone Repository

git clone https://github.com/ismailadadas/aquatekengineering-rasa-telegram-chatbot.git


bash : cd aquatekengineering-rasa-telegram-chatbot


2️⃣ Buat Virtual Environment (venv)


bash : python -m venv venv


Virtual environment menjaga dependency Python terpisah dari sistem.

3️⃣ Aktifkan Virtual Environment


Windows (PowerShell):


bash : .\venv\Scripts\Activate.ps1



Windows (cmd):



.\venv\Scripts\activate.bat



Mac/Linux:

source venv/bin/activate

4️⃣ Install Dependency


pip install --upgrade pip


pip install rasa==3.6.21


pip install rasa-sdk==3.6.2


pip install -r requirements.txt


5️⃣ Training Model Rasa


bash : rasa train


6️⃣ Jalankan Action Server (Terminal 1, karena ada custom actions)


bash : rasa run actions


Biarkan terminal ini tetap berjalan karena bot memiliki custom actions.

7️⃣ Jalankan Chatbot (Terminal 2)


7a. Test Lokal dengan Rasa Shell


bash : rasa shell


Chat langsung dengan bot di terminal untuk testing cepat.


Contoh chat ke bot : 


Input : Hai



Bot : Halo! Saya adalah Chatbot Informasi Keselamatan Bahan Kimia Hytreat. Saya dapat memberikan data Komposisi, Bahaya, dan P3K untuk HYTREAT 1200, 2200, dan 5300.


input : bahaya 1200


Bot : Kata Sinyal: DANGER. Bahaya utama: Menyebabkan kerusakan mata yang tidak dapat diperbaiki dan luka bakar pada kulit. Mungkin fatal jika tertelan atau diserap melalui kulit.



7b. Jalankan Server untuk API / Channel Lain


bash : rasa run --enable-api --debug


Server akan berjalan di http://localhost:5005.
Gunakan terminal terpisah agar action server tetap berjalan.

8️⃣ Integrasi Telegram (Opsional)

Buat bot Telegram → dapatkan bot token

Ubah acces token yang di dapet tadi di dalam file credentials.yml

Jalankan Rasa dengan connector Telegram (Terminal 2):

bash : rasa run --enable-api --connector telegram


expose ke internet gunakan ngrok , buat terminal baru (terminal 3):

bash : ngrok http 5005

copy webhook_url ngrok edit(masukin) ke credentials.yml

biarkan server nya berjalan

lalu bash : rasa run (terminal 2)

