#This Class is violate the Single responsiblity principle
class OrderProcessor:
    def __init__(self, orders):
        self.orders = orders
    
    def process_order(self, order_id):
       
        order = self.orders.get(order_id)
        if order:
            self.update_inventory(order)
            self.generate_invoice(order)
            self.send_email_confirmation(order)
    
    def update_inventory(self, order):
        
              print(f"Updating inventory for {order['item']}")
    
    def generate_invoice(self, order):
        
               print(f"Generating invoice for {order['item']}")
    
    def send_email_confirmation(self, order):
        
        
        print(f"Sending confirmation email for order {order['id']}")


#This Class is not violate the Single responsiblity principle

class OrderProcessor:
    def __init__(self, orders, inventory, email):
        self.orders = orders
        self.inventory = inventory  
        self.email = email   
    
    def process_order(self, order_id):
       
        order = self.orders.get(order_id)
        if order:
          self.inventory.update_inventory(order)
          self.inventory.generate_invoice(order)
          self.email.send_email_confirmation(order)

class inventory:
    def update_inventory(self, order):
        
              print(f"Updating inventory for {order['item']}")
    
    def generate_invoice(self, order):
        
               print(f"Generating invoice for {order['item']}")

class email:
                
    def send_email_confirmation(self, order):
        
        
        print(f"Sending confirmation email for order {order['id']}")
        
        
        
        
        
        
        