#this class is violate single responsibility

class OrderProcessor:
    def __init__(self, order ,inventory,notifier):
        self.order=order
        self.inventory=inventory
        self.notifier=notifier
        
    def proceddor_order(self):
        #Validate order
        if not self.order.is_valid():
            raise Exception("order is not valid")
        
        #Update inventory
        for item in self.order.items:
            self.inventory.Update(item)
            
        self.notifier.send("order processed",self.order.custmor_email)
        
        print("order processed successfully")
            
        
#this class is not  violate single responsibility

class OrderProcessor:
    def __init__(self, order ,inventory,notifier):
        self.order=order
        self.inventory=inventory
        self.notifier=notifier
    
    def proceddor_order(self):
        #Validate order
        if not self.order.is_valid():
            raise Exception("order is not valid")
        
        #Update inventory
        self.inventory_manager.update_inventory(self.order.items)
            
        self.notifier.send_notification("order processed",self.order.custmor_email)
        
        print("order processed successfully")
        
        
        
class inventory_manager:
    def __init__(self,inventory):
        self.inventory=inventory
    
    def update_inventory(self,items):
        for item in items:
            self.inventory.update(item)
        
        
class Notifier:
    def __init__(self,notification_service):
        self.notification_service=notification_service      
        
    def send_notification(self,message,recipient_email):
         self.notification_service.send_email(message,recipient_email)
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        