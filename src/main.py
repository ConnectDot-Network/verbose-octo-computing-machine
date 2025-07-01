from Translator import Translator
translator = Translator(language='pl')  # 🇵🇱 zmień na 'en', 'de', 'nl', 'fr', 'es', itd.

import json

def load_products():
    try:
        with open('data/products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)
            print(translator.translate('loaded', count=len(products['products'])))
            for p in products['products']:
                print(f"- {p['name']} ({p['price_converted']['formatted']}) [{p['category']}]")
    except Exception as e:
        print(f"⚠️ Błąd: {e}")

def start():
    print("\n" + translator.translate('title') + "\n")
    load_products()
    print("\n" + translator.translate('ready'))

if __name__ == "__main__":
    start()
Zaktualizowano main.py – integracja tłumacza

