Aquatek Engineering – Rasa Telegram Chatbot

📌 Catatan Proyek

Project ini dikembangkan sebagai bagian dari penelitian skripsi terkait implementasi chatbot berbasis Artificial Intelligence dalam penyediaan informasi keselamatan bahan kimia industri. Fokus chatbot ini adalah memberikan informasi bahaya, komposisi, dan penanganan pertama (P3K) produk kimia HYTREAT pada perusahaan PT Aquatek Engineering.

Tujuan utama proyek:

1.memberikan akses informasi keselamatan bahan kimia secara cepat

2.mendukung prosedur kerja aman di lingkungan industri

3.meningkatkan awareness terhadap bahaya material kimia 

5.menyediakan solusi informasi instan dan otomatis tanpa harus membuka dokumen MSDS dan PTD /manual

Studi kasus yang digunakan mengacu pada:

1.Penggunaan bahan kimia HYTREAT (seri 1200, 2200, 5300, dan lainnya) , AQUA-SHIELD (Seri 620 , 630 dan lainya , dan Bahan kimia pendukung lain nya.

2.kebutuhan keselamatan saat penanganan bahan kimia

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

1.buat bot di Telegram (BotFather)

2.dapatkan token

3.buka file credentials.yml

4.ganti token Telegram

5.Jalankan connector Telegram :

rasa run --enable-api --connector telegram

6.Expose menggunakan ngrok

Terminal baru:

ngrok http 5005


7.Copy webhook URL → masukkan ke credentials.yml

Kemudian jalankan kembali:

rasa run
