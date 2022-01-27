# importing required modules
import PyPDF2



def PDFrotate(origFileName, newFileName, rotation):

	# creating a pdf File object of original pdf
	pdfFileObj = open("example.pdf", 'rb')
	
	# creating a pdf Reader object
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	# creating a pdf writer object for new pdf
	pdfWriter = PyPDF2.PdfFileWriter()
	
	# rotating each page
	for page in range(pdfReader.numPages):

		# creating rotated page object
		pageObj = pdfReader.getPage(page)
		pageObj.rotateClockwise(rotation)

		# adding rotated page object to pdf writer
		pdfWriter.addPage(pageObj)

	# new pdf file object
	newFile = open("rotatedexample.pdf", 'wb')
	
	# writing rotated pages to new file
	pdfWriter.write(newFile)

	# closing the original pdf file object
	pdfFileObj.close()
	
	# closing the new pdf file object
	newFile.close()
	

def main():

	# original pdf file name
	origFileName = 'example.pdf'
	
	# new pdf file name
	newFileName = 'rotated_example.pdf'
	
	# rotation angle
	rotation = int(input("Degrees to be rotated: "))
	
	# calling the PDFrotate function
	PDFrotate(origFileName, newFileName, rotation)
	
if __name__ == "__main__":
	# calling the main function
	main()


#merging pdf:
 
def PDFmerge(pdfs, output):
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()
 
    # appending pdfs one by one
    for pdf in pdfs:
        pdfMerger.append(pdf)
 
    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)

def add_watermark(wmFile, pageObj):
    # opening watermark pdf file
    wmFileObj = open("watermark.pdf", 'rb')
    
    # creating pdf reader object of watermark pdf file
    pdfReader = PyPDF2.PdfFileReader(wmFileObj)
     
    # merging watermark pdf's first page with passed page object.
    pageObj.mergePage(pdfReader.getPage(0))
     
    # closing the watermark pdf file object
    wmFileObj.close()
     
    # returning watermarked page object
    return pageObj
 
 
def main():
    # pdf files to merge
    pdfs = ['example.pdf', 'rotatedexample.pdf']
 
    # output pdf file name
    output = 'combined_example.pdf'
 
    # calling pdf merge function
    PDFmerge(pdfs=pdfs, output=output)
 
 

mywatermark = 'watermark.pdf'
    
    # original pdf file name
origFileName = 'example.pdf'
     
    # new pdf file name
newFileName = 'watermarked_example.pdf'
     
    # creating pdf File object of original pdf
pdfFileObj = open(origFileName, 'rb')
     
    # creating a pdf Reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
    # creating a pdf writer object for new pdf
pdfWriter = PyPDF2.PdfFileWriter()
     
    # adding watermark to each page
for page in range(pdfReader.numPages):
        # creating watermarked page object
        wmpageObj = add_watermark(mywatermark, pdfReader.getPage(page))
         
        # adding watermarked page object to pdf writer
        pdfWriter.addPage(wmpageObj)
 
 # new pdf file object
newFile = open(newFileName, 'wb')
     
    # writing watermarked pages to new file
pdfWriter.write(newFile)
 
    # closing the original pdf file object
pdfFileObj.close()
    # closing the new pdf file object
newFile.close()
if __name__ == "__main__":
    # calling the main function
    main()   