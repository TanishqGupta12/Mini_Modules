from PyPDF2 import PdfFileWriter , PdfFileMerger , PdfFileReader
import os
import getpass

choosie = int(input(print (" choosie \n 1. Password Protect \n 2. Merge Multiple PDF")))
optin = ["Password Protect" , "Merge Multiple PDF" ]
if choosie == 1 :
    print("*****************************"+optin[0]+"*********************************")
    FileWriter = PdfFileWriter()
    # original file path
    pdf=PdfFileReader("")
    for item_num in range(pdf.numPages):
        PdfFileReader.addPage(pdf.getPage(item_num))
    passw=getpass.getpass(prompt="Password :")
    FileWriter.encrypt(passw)
    with open('ho.pdf' ,'wb') as f:
        PdfFileWriter.write(f)

elif choosie == 2:
    print("*****************************"+optin[1]+"*********************************")
    merge=PdfFileMerger()
    for item in os.listdir():
        if item.endswith('.pdf'):
            merge.append(item)
        merge.write('Final_pdf.pdf')
    merges=PdfFileMerger
    # original file path
    with open ("", 'rb') as fin:
        merges.append(PdfFileReader(fin))
os.remove("")
merges.close()