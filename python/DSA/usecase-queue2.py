# Printing the Document in a Printer in a Sequential order
class PrintDocument:
    def __init__(self):
        self.printer = []
        
    def scan_doc(self, doc):
        self.printer.append(doc)
        print(f"Scanning the {doc} document")  
         
    def print_doc(self):
        # check if any document found in the queue
        if self.printer:
            # print it (remove the scanned document)
            doc = self.printer.pop(0)
            print(f"Printing the {doc} document")
        else:
            print(f"Printed all documents, No Document found")
        
printDoc = PrintDocument()

printDoc.scan_doc("Aadhar Card")
printDoc.scan_doc("Voter ID")
printDoc.scan_doc("Hall Ticket")
printDoc.scan_doc("Marks Card")
printDoc.print_doc()
printDoc.print_doc()
printDoc.print_doc()
printDoc.print_doc()
printDoc.print_doc()