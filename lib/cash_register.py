#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount if self._valid_discount(discount) else 0
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def _valid_discount(self, discount):
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            return False
        return True

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discounted_total = self.total * (100 - self.discount) / 100
        self.total = int(discounted_total) if discounted_total.is_integer() else discounted_total
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        amount = last_transaction["price"] * last_transaction["quantity"]
        self.total -= amount
        if self.total == int(self.total):
            self.total = int(self.total)

        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])
