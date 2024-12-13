# Interface Segregation Principle (ISP)
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, doc):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class ModernPrinter(Printer, Scanner):
    def print_document(self, doc):
        print(f"Printing: {doc}")

    def scan_document(self):
        print("Scanning document")


class SimplePrinter(Printer):
    def print_document(self, doc):
        print(f"Printing: {doc}")
