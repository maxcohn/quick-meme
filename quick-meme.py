from PIL import Image, ImageDraw, ImageFont
from typing import Tuple
import sys

def get_font(img_width, font_name: str, text: str):
    """Get the ImageFont instance of the wanted font in the correct size for the
    length of the text

    :param img_width: Width of the base image
    
    :param font_name: File name of the font being used

    :param text: Text that is going to be rendered in the given font
    """
    # current font size, starting at 1
    cur_size = 1
    cur_font = ImageFont.truetype(font_name, size=cur_size)
    
    # check if the text is multilined
    is_multiline = '\n' in text

    # loop while font stays within a 5% margin on left and right
    new_width = 0
    while new_width < img_width * .9:
        cur_font = ImageFont.truetype(font_name, size=cur_size)

        new_width = cur_font.getsize_multiline(text)[0] if is_multiline else cur_font.getsize(text)[0]

        cur_size += 1
    
    # get the final font and the final size of the rendered text
    final_font = ImageFont.truetype(font_name, size=cur_size - 1)
    final_size = final_font.getsize_multiline(text) if is_multiline else final_font.getsize(text)

    return (final_font, final_size)
    

file_name = sys.argv[1]
out_file = sys.argv[2]
font_name = sys.argv[3]
meme_text = sys.argv[4]

with open(file_name, mode='rb') as f:
    # open the original image
    original_image = Image.open(f)

    # get the font and the size of the rendered text in that font
    font, font_size = get_font(original_image.size[0], font_name, meme_text)

    #TODO possibly do something a little more elaborate with the margins
    # create the dimensions of the new image
    new_img_dim = (original_image.size[0], original_image.size[1] + font_size[1] + 20)
    
    # creat the new blank image, write the text, and paste the original image under it
    new_img = Image.new('RGB', new_img_dim, (255,255,255,255))

    d = ImageDraw.Draw(new_img)
    d.text((10, 10), meme_text, font=font, fill=(0,0,0))

    new_img.paste(original_image, box=(0, font_size[1] + 20), mask=None)
    with open(out_file, mode='wb') as out_f:
        new_img.save(out_f)
    

"""TODO possible addition in the future
def get_font_autoline(img_size: Tuple[int, int], font_name: str, text: str):
    pass
"""