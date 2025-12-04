from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet 

# Database (Data Hytreat Aqua-Shield dan Sulfuric Acid yang di gunakan sebagai respons dari chatbot)
PRODUCT_DATA = {
    # HYTREAT 1200
    "1200": {
        "komposisi": "Komposisi HYTREAT 1200 (Microbiocide): 5-chloro-2-Methyl-4-Isothiazolin (2.0-2.8%) dan 2-Methyl-4-Isothiazolin (2.0-2.8%).",
        "bahaya": "Kata Sinyal: Danger!. Menyebabkan kerusakan mata permanen dan luka bakar kulit. Berbahaya jika tertelan, terserap kulit, atau terhirup. Dapat menyebabkan sensitisasi kulit.",
        "p3k": "Jika terhirup, pindahkan korban ke udara segar, berikan napas buatan jika tidak bernapas, segera cari bantuan medis. Jika tertelan, jangan memicu muntah dan segera dapatkan pertolongan medis. Jika terkena kulit, lepaskan pakaian atau sepatu yang terkontaminasi lalu cuci area yang terkena dengan sabun dan air. Jika terkena mata, bilas dengan air selama minimal 15 menit dan segera cari perhatian medis.",
        "fungsi": "Microbiocide untuk cooling tower.",
        "informasi_penggunaan": "Hindari tumpahan, kontak dengan kulit, dan mata. Simpan di tempat yang sejuk, kering, berventilasi baik, dalam wadah tertutup, serta menghindari suhu yang ekstrem."
    },
    # HYTREAT 2200
    "2200": {
        "komposisi": "Komposisi HYTREAT 2200 (Bio-dispersant): Glutaraldehyde (10-12%) dan n-Alkyl dimethyl benzyl ammonium chloride (1-2%).",
        "bahaya": "Kata Sinyal: Danger!. Toxic jika tertelan dan terhirup (H301+H331). Menyebabkan luka bakar kulit dan kerusakan mata yang parah (H314). Sangat beracun bagi kehidupan akuatik (H400).",
        "p3k": "P3K Mata: Bilas mata minimal 15 menit, segera dapatkan perhatian medis. P3K Tertelan: Jika Mual-mual, jangan berikan apapun untuk diminum, segera dapatkan perhatian medis.",
        "fungsi": "Bio-dispersant dan surfactant untuk cooling tower.",
        "informasi_penggunaan": "Hindari tumpahan, kontak dengan kulit, dan mata. Gunakan sarung tangan, pakaian, serta pelindung mata dan wajah."
    },
    # HYTREAT 5300
    "5300": {
        "komposisi": "Komposisi HYTREAT 5300: 2-phosphonobutane-1,2,4-tricarboxylic acid (<3%), Sodium tolyltriazole (<2%), Terpolymer (<5%), Polyacrylic acid (<5%), Zinc Chloride (<2%), dan Hydrochloride acid (<5%).",
        "bahaya": "Kata Sinyal: Danger!. Bisa Menyebabkan luka bakar pada kulit dan kerusakan mata. Bisa menyebabkan cacat genetik. Beracun untuk Kehidupan air. Produk ini juga sangat asam (pH 1.0-1.20).",
        "p3k": "P3K Mata: Bilas mata dengan air minimal 15 menit, segera cari perhatian medis. P3K Tertelan: Bilas mulut, Jika Mual-mual, cari pertolongan medis.",
        "fungsi": "Inhibitor kerak dan korosi untuk cooling tower.",
        "informasi_penggunaan": "Hindari tumpahan, kontak dengan kulit dan mata. Gunakan sarung tangan, pakaian, serta pelindung mata dan wajah. Simpan di tempat sejuk, kering, dan berventilasi baik."
    },
    # HYTREAT 5700
    "5700": {
        "komposisi": "Komposisi HYTREAT 5700: Sodium Molybdate (10-20%) dan Tolyl Triazole (2-4%).",
        "bahaya": "Kata Sinyal: Warning!. Menyebabkan iritasi serius pada mata dan iritasi kulit.",
        "p3k": "Jika terkena mata/kulit, bilas dengan air minimal 15 menit dan cari perhatian medis. Jika tertelan, berikan air untuk diminum dan cari perhatian medis.",
        "fungsi": "Inhibitor kerak dan korosi untuk chiller.",
        "informasi_penggunaan": "Hindari tumpahan, kontak dengan kulit dan mata. Cuci tangan secara menyeluruh."
    },
    # AQUA-SHIELD 221
    "221": {
        "komposisi": "Komposisi AQUA-SHIELD 221: Blend of Sulphite based compound dan performance enhancement catalyst compounds.",
        "bahaya": "Tidak ada simbol bahaya yang diperlukan, tetapi bisa menyebabkan iritasi mata/kulit. Menelan/menghirup debu bisa berbahaya.",
        "p3k": "Jika terkena mata, segera bilas dengan air minimal 15 menit dan cari bantuan medis. Jika tertelan, segera cari pertolongan medis.",
        "fungsi": "Penghambat korosi ketel uap pada boiler.",
        "informasi_penggunaan": "Kontainer material ini dapat berbahaya ketika dikosongkan. Semua tindakan pencegahan bahaya harus diperhatikan. Simpan di tempat kering dan dalam wadah tertutup rapat."
    },
    # AQUA-SHIELD 320
    "320": {
        "komposisi": "Komposisi AQUA-SHIELD 320: Pure alkali solution. Mengandung Sodium Hydroxide (<50%).",
        "bahaya": "Kata Sinyal: Danger!. Bersifat korosif terhadap mata, dapat menyebabkan luka bakar pada kulit, dan iritasi internal yang parah jika tertelan.",
        "p3k": "Mata: Bilas terus menerus dengan air mengalir minimal 15 menit, cari perhatian medis. Tertelan: Jangan rangsang muntah, beri air untuk diminum, cari perhatian medis.",
        "fungsi": "Penghambat korosi dan pengendalian kerak, untuk menaikkan pH air umpan dan menjaga alkalinitas air ketel pada boiler.",
        "informasi_penggunaan": "Jangan menghirup gas/fume/uap. Jangan pernah menambahkan air ke produk ini. Gunakan sarung tangan, pakaian, pelindung mata dan wajah. Simpan di tempat sejuk."
    },
    # AQUA-SHIELD 620
    "620": {
        "komposisi": "Komposisi AQUA-SHIELD 620: High performance blend of scale inhibitors, termasuk thermally stable polymer dispersants, metals sequesterants, organic sludge conditioners, dan antifoam.",
        "bahaya": "Kata Sinyal: Danger! dan Toxic!.Bisa Menyebabkan kerusakan mata dan kulit, Berbahaya jika tertelan dan terhirup.",
        "p3k": "Mata/Kulit: Bilas segera dengan air minimal 15 menit, cari perhatian medis segera. Tertelan: JANGAN RANGSANG MUNTAH, bilas mulut, beri susu/air minum, cari perhatian medis segera.",
        "fungsi": "Pengendalian kerak ketel uap, mencegah endapan padat pada boiler.",
        "informasi_penggunaan": "Simpan dalam wadah tertutup di area yang kering dan berventilasi baik."
    },
    # AQUA-SHIELD 630
    "630": {
        "komposisi": "Komposisi AQUA-SHIELD 630: High performance blend of scale inhibitors, termasuk thermally stable polymer dispersants, metals sequesterants, organic sludge conditioners, antifoam, dan polyphosphates.",
        "bahaya": "Tidak ada simbol bahaya yang diperlukan.Tetapi bisa menyebabkan Iritasi mata/kulit. Menelan/menghirup debu bisa berbahaya.",
        "p3k": "Mata/Kulit: Bilas dengan air/sabun, cari perhatian medis. Tertelan/Terhirup: Pindah ke udara segar, cari perhatian medis segera.",
        "fungsi": "Pengendalian kerak ketel uap, efektif di mana kekerasan ada dalam air umpan untuk boiler.",
        "informasi_penggunaan": "Gunakan sarung tangan pelindung, pakaian pelindung, pelindung pernapasan, serta pelindung mata dan wajah. Jauhkan dari pembekuan."
    },
    # SULFURIC ACID
    "SULFURIC ACID": {
        "komposisi": "Komposisi SULFURIC ACID: Sulphuric Acid (98.2%).",
        "bahaya": "Jenis bahaya: Danger!. Bisa menyebabkan luka bakar kulit yang parah dan kerusakan mata serius. Dapat bersifat korosif terhadap logam.",
        "p3k": "Jika terhirup: pindahkan ke udara segar dan hubungi dokter. Jika terkena kulit: seka dengan kain kering lalu bilas dengan banyak air, segera lepaskan pakaian yang terkontaminasi, dan hubungi dokter segera. Jika terkena mata: bilas dengan banyak air dan segera hubungi dokter spesialis mata. Jika tertelan: berikan air untuk diminum, jangan dipicu untuk muntah, dan segera hubungi dokter.",
        "fungsi": "Untuk Menurunkan PH air.",
        "informasi_penggunaan": "Kenakan sarung tangan pelindung, pelindung mata, dan pelindung wajah. Gunakan pakaian pelindung yang tahan asam dan segera ganti pakaian yang terkontaminasi. Cuci tangan."
    },
}

# --- Action Classes Lainnya 
# --- Fungsi Mengambil data komposisi bahan kimia dari produk (misal HYTREAT 1200, 5300, 221, dll) kemudian mengirimkannya sebagai response ke user.

#   --- ACTION: Minta Komposisi ---
class ActionProvideKomposisi(Action):
# ... (kode ActionProvideKomposisi) ...
    def name(self) -> Text:
        return "action_provide_komposisi"
    # ... (implementasi) ...
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produk_entity = next(tracker.get_latest_entity_values("produk"), None)
        
        if not produk_entity:
            produk_entity = tracker.get_slot("produk") 

        # Normalisasi key produk
        produk_entity = produk_entity.upper() if produk_entity else None
        if produk_entity and produk_entity in PRODUCT_DATA:
            response = PRODUCT_DATA[produk_entity]["komposisi"]
            dispatcher.utter_message(text=response)
            
            return [SlotSet("produk", None)] 
        else:
            dispatcher.utter_message(response="utter_minta_komposisi")
            return []
        
#   --- ACTION: Minta Bahaya ---
class ActionProvideBahaya(Action):
# ... (kode ActionProvideBahaya) ...
    def name(self) -> Text:
        return "action_provide_bahaya"
    # ... (implementasi) ...
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produk_entity = next(tracker.get_latest_entity_values("produk"), None)
        
        if not produk_entity:
            produk_entity = tracker.get_slot("produk") 
            
        # Normalisasi key produk
        produk_entity = produk_entity.upper() if produk_entity else None
        if produk_entity and produk_entity in PRODUCT_DATA:
            response = PRODUCT_DATA[produk_entity]["bahaya"]
            dispatcher.utter_message(text=response)
            
            return [SlotSet("produk", None)]
        else:
            dispatcher.utter_message(response="utter_minta_bahaya")
            return []

#   --- ACTION: Minta P3K ---
class ActionProvideP3K(Action):
# ... (kode ActionProvideP3K) ...
    def name(self) -> Text:
        return "action_provide_p3k"
    # ... (implementasi) ...
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produk_entity = next(tracker.get_latest_entity_values("produk"), None)
        
        if not produk_entity:
            produk_entity = tracker.get_slot("produk") 
            
        # Normalisasi key produk
        produk_entity = produk_entity.upper() if produk_entity else None
        if produk_entity and produk_entity in PRODUCT_DATA:
            response = PRODUCT_DATA[produk_entity]["p3k"]
            dispatcher.utter_message(text=response)
            
            return [SlotSet("produk", None)]
        else:
            dispatcher.utter_message(response="utter_minta_p3k")
            return []

# --- ACTION: Minta Fungsi (Tujuan/Kegunaan) ---
class ActionProvideFungsi(Action):
    def name(self) -> Text:
        return "action_provide_fungsi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produk_entity = next(tracker.get_latest_entity_values("produk"), None)
        
        if not produk_entity:
            produk_entity = tracker.get_slot("produk") 

        # Normalisasi key produk
        produk_entity = produk_entity.upper() if produk_entity else None
        if produk_entity and produk_entity in PRODUCT_DATA:
            response = PRODUCT_DATA[produk_entity]["fungsi"]
            dispatcher.utter_message(text=response)
            
            # MERESET SLOT
            return [SlotSet("produk", None)] 
        else:
            dispatcher.utter_message(response="utter_minta_fungsi")
            return []

# --- ACTION : Minta Informasi Penggunaan ---
class ActionProvideInformasiPenggunaan(Action):
    def name(self) -> Text:
        return "action_provide_informasi_penggunaan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produk_entity = next(tracker.get_latest_entity_values("produk"), None)
        
        if not produk_entity:
            produk_entity = tracker.get_slot("produk") 

        # Normalisasi key produk
        produk_entity = produk_entity.upper() if produk_entity else None
        if produk_entity and produk_entity in PRODUCT_DATA:
            response = PRODUCT_DATA[produk_entity]["informasi_penggunaan"]
            dispatcher.utter_message(text=response)
            
            # MERESET SLOT
            return [SlotSet("produk", None)] 
        else:
            dispatcher.utter_message(response="utter_minta_penggunaan")
            return []