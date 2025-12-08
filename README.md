Aquatek Engineering – Rasa Telegram Chatbot

Chatbot lokal berbasis Rasa 3.6 dengan integrasi Telegram untuk memberikan informasi keselamatan bahan kimia HYTREAT (komposisi, bahaya, dan P3K).

⚙️ Catatan Versi
Komponen	Versi
Rasa	3.6.21
Rasa SDK	3.6.2
Python	3.9.13

Python Path digunakan (opsional):
C:\Users\ari\Desktop\Skripsi\chatbot\venv\Scripts\python.exe

🚀 Menjalankan Chatbot Secara Lokal


1️⃣ Clone Repository
git clone https://github.com/ismailadadas/aquatekengineering-rasa-telegram-chatbot.git
cd aquatekengineering-rasa-telegram-chatbot

2️⃣ Buat Virtual Environment
python -m venv venv

3️⃣ Aktifkan Virtual Environment

Windows PowerShell

.\venv\Scripts\Activate.ps1


Windows CMD

.\venv\Scripts\activate


Mac / Linux

source venv/bin/activate

4️⃣ Install Dependency
pip install --upgrade pip
pip install rasa==3.6.21
pip install rasa-sdk==3.6.2
pip install -r requirements.txt

5️⃣ Training Model
rasa train

6️⃣ Jalankan Action Server (Terminal 1)
rasa run actions


Biarkan terminal ini tetap berjalan (karena terdapat custom actions)

7️⃣ Jalankan Chatbot
Test lokal menggunakan terminal
rasa shell


Contoh percakapan:

Hai
> Halo! Saya adalah Chatbot Informasi Keselamatan Bahan Kimia...

bahaya 1200
> Kata Sinyal: DANGER...

Run dengan REST API / Channel lain
rasa run --enable-api --debug


Server default:
http://localhost:5005

🤖 Integrasi Telegram (Opsional)
Langkah-langkah

buat bot di Telegram (BotFather)

dapatkan token

buka file credentials.yml

ganti token Telegram

Jalankan connector Telegram
rasa run --enable-api --connector telegram

Expose menggunakan ngrok

Terminal baru:

ngrok http 5005


Copy webhook URL → masukkan ke credentials.yml

Kemudian jalankan kembali:

rasa run
