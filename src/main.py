import json

def load_products():
    try:
        with open('data/products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)
            print(f"✅ Załadowano {len(products['products'])} produktów.")
            for p in products['products']:
                print(f"- {p['name']} ({p['price_converted']['formatted']}) [{p['category']}]")
    except Exception as e:
        print(f"⚠️ Błąd: {e}")

def start():
    print("🚀 ConnectDot – AI Transformation Hub\n")
    load_products()
    print("\n🟢 System gotowy. Czekam na dalsze komendy...")

if __name__ == "__main__":
    start()
