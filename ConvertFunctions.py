from PIL import Image

import Decor
from Config import WATERMARK_PATH


@Decor.memoize
def convert_image_with_watermark(input_path, output_path, quality=100):
    image = Image.open(input_path)

    # Check if the image has an alpha channel (transparency)
    if image.mode != 'RGBA':
        # If no alpha channel, convert to RGBA for transparency support
        image = image.convert('RGBA')

    # Remove the background using white pixels (replace with desired background color if needed)
    image.convert('RGBA').putalpha(255)  # 255 for fully opaque (remove background)

    # Load watermark image (adjust path and watermark size as needed)
    watermark = Image.open(WATERMARK_PATH).convert('RGBA')  # Ensure watermark has transparency

    # Resize watermark to fit the image (optional)
    watermark_width, watermark_height = watermark.size
    image_width, image_height = image.size
    watermark_ratio = watermark_width / watermark_height
    if watermark_width > image_width:  # Adjust this factor to control watermark size //////////////////////
        new_watermark_width = int(image_width)  # /////////////////////////////////////////////////////////
        new_watermark_height = int(new_watermark_width / watermark_ratio)
        watermark = watermark.resize((new_watermark_width, new_watermark_height))

    # Add watermark to the bottom right corner (adjust position as needed)
    # watermark_position = (image_width - watermark_width, image_height - watermark_height)
    image.alpha_composite(watermark)

    # Save as WEBP with desired quality
    image.save(output_path, 'WEBP', quality=quality)


def convert_image(input_path, output_path, quality=100):
    image = Image.open(input_path)

    # Check if the image has an alpha channel (transparency)
    if image.mode != 'RGBA':
        # If no alpha channel, convert to RGBA for transparency support
        image = image.convert('RGBA')

    # Remove the background using white pixels (replace with desired background color if needed)
    image.convert('RGBA').putalpha(255)  # 255 for fully opaque (remove background)

    # Save as WEBP with desired quality
    image.save(output_path, 'WEBP', quality=quality)
