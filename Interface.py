from abc import ABC, abstractmethod

from typing import Protocol


class Printable(Protocol):
    @abstractmethod
    def print(self) -> None:
       pass

class Scannable(Protocol):
    @abstractmethod
    def scan(self) -> None:
        pass

class Faxable(Protocol):
    @abstractmethod
    def fax(self) -> None:
        pass

class Document(Printable):
    def __init__(self, content: str):
        self.content = content

    def print(self) -> None:
        print(self.content)

class Image(Scannable, Faxable):
    def __init__(self, data: bytes):
        self.data = data
    
    def scan(self) -> None:
        print("Scanning the image")
  
    def fax(self) -> None:
        print("Faxing the image")

class Printer:
    def print(self, printable: Printable) -> None:
       
        printable.print()


class ScannerFaxer:
    def scan_and_fax(self, scannable: Scannable,faxable: Faxable) -> None:

         scannable.scan()

         faxable.fax()

document = Document("Hello, world!")

image = Image(b"\x89PNG\r\n\x1a\n\x00\x00")

printer = Printer()
 
printer.print(document)

scanner_faxer = ScannerFaxer()

scanner_faxer.scan_and_fax(image, image)
