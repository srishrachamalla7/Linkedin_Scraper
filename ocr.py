# import pytesseract
from PIL import Image
import os
import easyocr

class OCR:
    reader = easyocr.Reader(['en'])
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def extract_text_from_image(self,image_path):
        """Extracts text from an image using Tesseract OCR"""
        try:
            # Open the image using PIL
            # img = Image.open(image_path)
            
            # # Use Tesseract to do OCR on the image
            # # text = pytesseract.image_to_string(img)
            # text = self.reader.readtext(image_path)
            # print(text)
            results = self.reader.readtext(image_path)
        
        # Extract only the text from each detection result and join them
            text = " ".join([item[1] for item in results])
            return text
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return None

    def folder_reader(self,folder_path):
        # folder_path = 'C:\prop\wd_spearsoft\MeetAgent\screenshots'
        files = os.listdir(folder_path)
        print(files)
        extracted_text = 'The Linkedin Profile Information :'
        files = [f for f in files if f.endswith('.png')]
        for i in range(len(files)):
            image_path = os.path.join(folder_path, files[i])
            extracted_text = extracted_text +'\n' +self.extract_text_from_image(image_path)

        text_file = os.path.join(folder_path, 'output.txt')
        with open(text_file, 'w') as f:
            f.write(extracted_text)

        return extracted_text

if __name__ == '__main__':
    ocr = OCR()
    # ocr.folder_reader('C:\prop\wd_spearsoft\MeetAgent\screenshots')

#pip install easyocr torch torchvision
