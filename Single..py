#this class is violate Single principle
class ReportGenerator:
    def __init__(self, data):
        self.data = data
    
    def generate_pdf_report(self):
       
        print("Generating PDF report")
    
    def generate_csv_report(self):

        print("Generating CSV report")
    
    def send_report_by_email(self, email):

        print(f"Sending report to {email}")
        
        
#this class is not violate Single principle

class ReportGenerator:
    def __init__(self, data):
        self.data = data
    
    def generate_pdf_report(self):
        print("Generating PDF report")
    
    def generate_csv_report(self):
        print("Generating CSV report")

class ReportSender:
    def send_report_by_email(self, email):
        print(f"Sending report to {email}")
