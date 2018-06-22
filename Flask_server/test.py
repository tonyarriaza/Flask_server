import pytesseract
import Image
import os
from parse_OCR import parse_OCR
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def parse_files():
    RESULT=''
    PATH = '/home/ec2-user/environment/photos'
    for file in os.listdir(PATH):
        filename = file
        file_path=os.path.join(PATH, filename)
        RESULT=pytesseract.image_to_string(Image.open(file_path))
        parser=parse_OCR()
        listofItems=parser.parse(RESULT)
        print listofItems
        
    return RESULT
def Image_Results():
   
    RESULT=''
  
    try:
       RESULT=parse_files()
       RESULT="program ran without a hitch"
       return RESULT
    except Exception as e: 
        print(e)
      
    
        

   
x= Image_Results()
print x

    
#if __name__ == "__main__":
 #   app.run(debug=True, host='0.0.0.0', port=Config.RUN_PORT)    
