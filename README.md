Menjalankan Chatbot Rasa Lokal
1. Clone repository
git clone https://github.com/ismailadadas/aquatekengineering-rasa-telegram-chatbot.git
cd aquatekengineering-rasa-telegram-chatbot

2. Buat virtual environment (venv)
python -m venv venv

3. Aktifkan virtual environment

Windows (PowerShell):

.\venv\Scripts\Activate.ps1


Windows (cmd):

.\venv\Scripts\activate.bat


Mac/Linux:

source venv/bin/activate

4. Install dependency
pip install --upgrade pip
pip install rasa==3.6.21
pip install rasa-sdk==3.6.2
pip install -r requirements.txt


Jika requirements.txt belum ada, buat dari environmentmu:

pip freeze > requirements.txt

5. Training model Rasa
rasa train

6. Jalankan action server (Terminal 1, jika ada custom actions)

Terminal 1:

rasa run actions


Biarkan terminal ini tetap berjalan.
Ini penting kalau bot punya custom actions.

7. Jalankan Rasa server atau testing lokal (Terminal 2)
7a. Test chatbot lokal dengan shell

Terminal 2:

rasa shell


Bisa langsung chat dengan bot untuk testing.

7b. Jalankan server untuk API atau channel lain

Terminal 2:

rasa run --enable-api --debug


Server Rasa akan berjalan di http://localhost:5005

8. Integrasi Telegram (opsional)

Buat bot Telegram → dapatkan bot token

Jalankan Rasa dengan connector Telegram (Terminal 2):

rasa run --enable-api --connector telegram


Jika mau expose ke internet pakai ngrok:

ngrok http 5005

9. Pastikan venv tidak ikut ke GitHub

Buat .gitignore di root project:

venv/
.env
__pycache__/
*.pyc


Jika venv sudah terlanjur ke-tracking:

git rm -r --cached venv
git add .
git commit -m "Remove venv from tracking"
git push --set-upstream origin main


Sekarang push aman, file besar di venv tidak ikut ke GitHub.

10. Catatan versi

Rasa Version: 3.6.21

Rasa SDK Version: 3.6.2

Python Version: 3.9.13

Operating System: Windows 10

Python Path: C:\Users\ari\Desktop\Skripsi\chatbot\venv\Scripts\python.exe
