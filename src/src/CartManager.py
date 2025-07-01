class CartManager:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)
        print(f"🟢 Dodano: {product['name']}")

    def remove_product(self, product_id):
        before = len(self.cart)
        self.cart = [p for p in self.cart if p['id'] != product_id]
        after = len(self.cart)
        print(f"🗑️ Usunięto {before - after} produkt(ów) z ID {product_id}")

    def show_cart(self):
        if not self.cart:
            print("🛒 Koszyk jest pusty.")
        else:
            print("📋 Zawartość koszyka:")
            for p in self.cart:
                print(f"- {p['name']} ({p['price_converted']['formatted']})")

    def total_value(self):
        total = sum(p['price_converted']['value'] for p in self.cart)
        print(f"💰 Suma: ${total:.2f}")
