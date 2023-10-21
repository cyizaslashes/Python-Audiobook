import pyttsx3
import PyPDF2

# Open the PDF file
book = open('bm.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)  # Use PdfReader instead of PdfFileReader
pages = len(pdfReader.pages)  # Use len(pdfReader.pages) to get the total number of pages

# Print the total number of pages
print(pages)

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Iterate through each page and read the text
for num in range(pages):
    page = pdfReader.pages[num]  # Access each page using pdfReader.pages
    text = page.extract_text()  # Use extract_text() to extract text
    speaker.say(text)

# Run the text-to-speech engine
speaker.runAndWait()
