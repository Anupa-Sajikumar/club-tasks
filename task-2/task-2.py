import pytesseract
from PIL import Image
def calculate_captcha(image_file):
    # Open the image file
    image = Image.open(image_file)
    # Use pytesseract to extract the text from the image
    text = pytesseract.image_to_string(image)
    # Use the eval function to calculate the result of the expression
    result = eval(text)
    return result
# Test the function
image_file = 'task-2/add_nos_capcha.jpg'
result = calculate_captcha(image_file)
print(result)