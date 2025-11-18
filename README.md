Menjalankan Chatbot Rasa Lokal
1️⃣ Clone Repository
git clone https://github.com/ismailadadas/aquatekengineering-rasa-telegram-chatbot.git
cd aquatekengineering-rasa-telegram-chatbot

2️⃣ Buat Virtual Environment (venv)
python -m venv venv


Virtual environment menjaga dependency Python terpisah dari sistem.

3️⃣ Aktifkan Virtual Environment

Windows (PowerShell):

.\venv\Scripts\Activate.ps1


Windows (cmd):

.\venv\Scripts\activate.bat


Mac/Linux:

source venv/bin/activate

4️⃣ Install Dependency
pip install --upgrade pip
pip install rasa==3.6.21
pip install rasa-sdk==3.6.2
pip install -r requirements.txt


Jika requirements.txt belum ada, buat dari environmentmu:

pip freeze > requirements.txt

5️⃣ Training Model Rasa
rasa train


Folder models/ akan berisi model terbaru.

6️⃣ Jalankan Action Server (Terminal 1, jika ada custom actions)
rasa run actions


Biarkan terminal ini tetap berjalan jika bot memiliki custom actions.

7️⃣ Jalankan Chatbot (Terminal 2)
7a. Test Lokal dengan Rasa Shell
rasa shell


Chat langsung dengan bot di terminal untuk testing cepat.

7b. Jalankan Server untuk API / Channel Lain
rasa run --enable-api --debug


Server akan berjalan di http://localhost:5005.
Gunakan terminal terpisah agar action server tetap berjalan.

8️⃣ Integrasi Telegram (Opsional)

Buat bot Telegram → dapatkan bot token

Jalankan Rasa dengan connector Telegram (Terminal 2):

rasa run --enable-api --connector telegram


Jika mau expose ke internet gunakan ngrok:

ngrok http 5005


Terminal 1 → rasa run actions
Terminal 2 → rasa run --enable-api --connector telegram

9️⃣ Pastikan venv Tidak Ikut ke GitHub

Buat file .gitignore di root project:

venv/
.env
__pycache__/
*.pyc


Jika venv sudah terlanjur di-track:

git rm -r --cached venv
git add .
git commit -m "Remove venv from tracking"
git push --set-upstream origin main


Ini mencegah push file besar di venv yang dapat menyebabkan error.

🔟 Catatan Versi

Rasa Version: 3.6.21

Rasa SDK Version: 3.6.2

Python Version: 3.9.13

Operating System: Windows 10

Python Path: C:\Users\ari\Desktop\Skripsi\chatbot\venv\Scripts\python.exe
