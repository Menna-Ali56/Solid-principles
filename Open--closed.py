#this code is violate open_closed
class PaymentProcessor:
    def __init__(self, payment_method, amount):
        self.payment_method = payment_method
        self.amount = amount
    
    def process_payment(self):
        if self.payment_method == "CreditCard":
            return f"Processing credit card payment of {self.amount}"
        elif self.payment_method == "PayPal":
            return f"Processing PayPal payment of {self.amount}"
        elif self.payment_method == "BankTransfer":
            return f"Processing bank transfer payment of {self.amount}"
        else:
            return "Invalid payment method"


#this code is not violate open_closed

class PaymentProcessor:
    def __init__(self, payment_method, amount):
        self.payment_method = payment_method
        self.amount = amount
    
    def process_payment(self):
        return self.payment_method.process_payment(self.amount)

class CreditCardPayment:
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount}"

class PayPalPayment:
    def process_payment(self, amount):
        return f"Processing PayPal payment of {amount}"

class BankTransferPayment:
    def process_payment(self, amount):
        return f"Processing bank transfer payment of {amount}"

