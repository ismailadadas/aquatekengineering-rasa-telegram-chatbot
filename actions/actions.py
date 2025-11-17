from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet 

# Database (Data Hytreat)
PRODUCT_DATA = {
    # HYTREAT 1200
    "1200": {
        "komposisi": "Komposisi HYTREAT 1200 (Microbiocide): 5-chloro-2-Methyl-4-Isothiazolin (2.0-2.8%) dan 2-Methyl-4-Isothiazolin (2.0-2.8%).",
        "bahaya": "Kata Sinyal: DANGER. Bahaya utama: Menyebabkan kerusakan mata yang tidak dapat diperbaiki dan luka bakar pada kulit. Mungkin fatal jika tertelan atau diserap melalui kulit.",
        "p3k": "P3K Mata: Segera bilas mata dengan air minimal 15 menit dan segera dapatkan perhatian medis. P3K Tertelan: Jika Mual-mual, segera dapatkan perhatian medis."
    },
    # HYTREAT 2200
    "2200": {
        "komposisi": "Komposisi HYTREAT 2200 (Bio-dispersant): Glutaraldehyde (10-12%) dan n-Alkyl dimethyl benzyl ammonium chloride (1-2%).",
        "bahaya": "Kata Sinyal: Danger. Bahaya utama: Toxic jika tertelan dan terhirup (H301+H331). Menyebabkan luka bakar kulit dan kerusakan mata yang parah (H314). Sangat beracun bagi kehidupan akuatik (H400).",
        "p3k": "P3K Mata: Bilas mata minimal 15 menit, segera dapatkan perhatian medis. P3K Tertelan: Jika Mual-mual, jangan berikan apapun untuk diminum, segera dapatkan perhatian medis."
    },
    # HYTREAT 5300
    "5300": {
        "komposisi": "Komposisi HYTREAT 5300 (Scale and Corrosion Inhibitor): 2-phosphonobutane-1,2,4-tricarboxylic acid (<3%), Sodium tolyltriazole (<2%), dan Hydrochloride acid (<5%).",
        "bahaya": "Kata Sinyal: DANGER. Bahaya utama: Bisa Menyebabkan luka bakar pada kulit dan kerusakan mata . Lalu bisa menyebabkan cacat genetik. Beracun untuk Kehidupan air . Produk ini juga sangat asam (pH 1.0-1.20).",
        "p3k": "P3K Mata: Bilas mata dengan air minimal 15 menit, segera cari perhatian medis. P3K Tertelan: Bilas mulut, Jika Mual-mual, cari pertolongan medis."
    },
}

# --- Action Classes ---

class ActionProvideKomposisi(Action):
    def name(self) -> Text:
        return "action_provide_komposisi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produk_entity = next(tracker.get_latest_entity_values("produk"), None)
        
        if not produk_entity:
            produk_entity = tracker.get_slot("produk") 

        if produk_entity and produk_entity in PRODUCT_DATA:
            response = PRODUCT_DATA[produk_entity]["komposisi"]
            dispatcher.utter_message(text=response)
            
            # MERESET SLOT
            return [SlotSet("produk", None)] 
        else:
            # FIX: Menggunakan utter_message(response=...) untuk fallback
            dispatcher.utter_message(response="utter_minta_komposisi")
            return []

class ActionProvideBahaya(Action):
    def name(self) -> Text:
        return "action_provide_bahaya"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produk_entity = next(tracker.get_latest_entity_values("produk"), None)
        
        if not produk_entity:
            produk_entity = tracker.get_slot("produk") 
            
        if produk_entity and produk_entity in PRODUCT_DATA:
            response = PRODUCT_DATA[produk_entity]["bahaya"]
            dispatcher.utter_message(text=response)
            
            # MERESET SLOT
            return [SlotSet("produk", None)]
        else:
            # FIX: Menggunakan utter_message(response=...) untuk fallback
            dispatcher.utter_message(response="utter_minta_bahaya")
            return []

class ActionProvideP3K(Action):
    def name(self) -> Text:
        return "action_provide_p3k"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produk_entity = next(tracker.get_latest_entity_values("produk"), None)
        
        if not produk_entity:
            produk_entity = tracker.get_slot("produk") 
            
        if produk_entity and produk_entity in PRODUCT_DATA:
            response = PRODUCT_DATA[produk_entity]["p3k"]
            dispatcher.utter_message(text=response)
            
            # MERESET SLOT
            return [SlotSet("produk", None)]
        else:
            # FIX: Menggunakan utter_message(response=...) untuk fallback
            dispatcher.utter_message(response="utter_minta_p3k")
            return []