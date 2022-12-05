from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import sys
import os

def parsePDF(infile):
    print(f'[+][+][+] Analyzing File {infile} ...[+][+][+]')
    pdf = open(f'{infile}', 'rb')
    analyzer = PDFParser(pdf)
    file = PDFDocument(analyzer)

    metadata = file.info  # The "Info" metadata
    # print(metadata)
    for i in metadata:
        for k,v in i.items():
            print(k, ':', v.decode('utf-8'))
def main():
    cmnd = sys.argv
    #Check whether files exists and execute the various above commands
    if not os.path.exists(cmnd[1]):
        print(cmnd[1])
        print('PDF file not found')
    else:
        fileToRead = parsePDF(cmnd[1])

if __name__ == '__main__':
    main()
