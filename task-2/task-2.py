import pytesseract
from PIL import Image
def solve_captcha(image_path):
    # Open the image file
    image = Image.open(image_path)
    # Run tesseract OCR on the image
    text = pytesseract.image_to_string(image)
    try:
        # Evaluate the expression
        result = eval(text)
    except:
        # Handle any errors that may occur during evaluation
        result = "Invalid expression"
    # Print the result
    return result
captcha_result = solve_captcha("captcha.jpg")
print(captcha_result)

"""This reframed version of the code encapsulates the OCR and evaluation process in a function called solve_captcha(). 
This function takes the path of the image file as an input and returns the result of the OCR and evaluation process. 
The function also includes a try-except block to handle any errors that may occur during the evaluation process, 
such as when the OCR text is not a valid Python expression, and return an informative message."""