#this code is violate open_closed
class TaxCalculator:
    def __init__(self, country, amount):
        self.country = country
        self.amount = amount
    
    def calculate_tax(self):
        if self.country == "USA":
            return self.amount * 0.1  # 10% tax in USA
        elif self.country == "India":
            return self.amount * 0.2  # 20% tax in India
        elif self.country == "UK":
            return self.amount * 0.15  # 15% tax in UK
        else:
            return 
        
        
        
#this code isnot violate open_closed
class TaxCalculator:
    def __init__(self, amount, tax_strategy):
        self.amount = amount
        self.tax_strategy = tax_strategy
    
    def calculate_tax(self):
        return self.tax_strategy.calculate_tax(self.amount)

class USATaxStrategy:
    def calculate_tax(self, amount):
        return amount * 0.1

class IndiaTaxStrategy:
    def calculate_tax(self, amount):
        return amount * 0.2

class UKTaxStrategy:
    def calculate_tax(self, amount):
        return amount * 0.15
