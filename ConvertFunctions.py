from PIL import Image

import Decor
from Config import WATERMARK_PATH, OUT_HEIGHT, OUT_WIDTH


@Decor.memoize
def convert_image_with_watermark_and_resize(input_path, output_path, quality=100):
    """
    Convert an image from PNG to WEBP format with a watermark and resizing.

    Args:
        input_path (str): The path to the input PNG image file.
        output_path (str): The path to save the output WEBP image file.
        quality (int, optional): The quality of the output WEBP image (default is 100).

    Returns:
        None
    """
    image = Image.open(input_path)

    # Check if the image has an alpha channel (transparency)
    if image.mode != 'RGBA':
        # If no alpha channel, convert to RGBA for transparency support
        image = image.convert('RGBA')

    # Remove the background using white pixels (replace with desired background color if needed)
    image.convert('RGBA').putalpha(255)  # 255 for fully opaque (remove background)

    # Load watermark image
    watermark = Image.open(WATERMARK_PATH).convert('RGBA')  # Ensure watermark has transparency

    # Resize watermark to fit the image
    watermark_width, watermark_height = watermark.size
    image_width, image_height = image.size

    # Calculate resizing coefficient
    if image_width > image_height:
        coefficient = OUT_WIDTH / image_width
    else:
        coefficient = OUT_HEIGHT / image_height

    # Resize image
    image_height = image_height * coefficient
    image_width = image_width * coefficient
    output_size = (int(image_width), int(image_height))
    image = image.resize(output_size)

    # Resize watermark
    watermark_ratio = watermark_width / watermark_height
    if watermark_width > image_width:
        new_watermark_width = int(image_width)
        new_watermark_height = int(new_watermark_width / watermark_ratio)
    else:
        new_watermark_height = int(image_height)
        new_watermark_width = int(new_watermark_height * watermark_ratio)
    watermark = watermark.resize((new_watermark_width, new_watermark_height))

    # Add watermark to the image
    watermark_position = (int((image_width / 2) - (new_watermark_width / 2)),
                          int((image_height / 2) - (new_watermark_height / 2)))
    image.alpha_composite(watermark, watermark_position)

    # Save as WEBP with desired quality
    image.save(output_path, 'WEBP', quality=quality)


@Decor.memoize
def convert_image(input_path, output_path, quality=100):
    """
    Convert an image from PNG to WEBP format without resizing or watermark.

    Args:
        input_path (str): The path to the input PNG image file.
        output_path (str): The path to save the output WEBP image file.
        quality (int, optional): The quality of the output WEBP image (default is 100).

    Returns:
        None
    """
    image = Image.open(input_path)

    # Check if the image has an alpha channel (transparency)
    if image.mode != 'RGBA':
        # If no alpha channel, convert to RGBA for transparency support
        image = image.convert('RGBA')

    # Remove the background using white pixels (replace with desired background color if needed)
    image.convert('RGBA').putalpha(255)  # 255 for fully opaque (remove background)

    # Save as WEBP with desired quality
    image.save(output_path, 'WEBP', quality=quality)


@Decor.memoize
def convert_image_with_resize(input_path, output_path, quality=100):
    """
    Convert an image from PNG to WEBP format with resizing but without watermark.

    Args:
        input_path (str): The path to the input PNG image file.
        output_path (str): The path to save the output WEBP image file.
        quality (int, optional): The quality of the output WEBP image (default is 100).

    Returns:
        None
    """
    image = Image.open(input_path)

    # Check if the image has an alpha channel (transparency)
    if image.mode != 'RGBA':
        # If no alpha channel, convert to RGBA for transparency support
        image = image.convert('RGBA')

    # Remove the background using white pixels (replace with desired background color if needed)
    image.convert('RGBA').putalpha(255)  # 255 for fully opaque (remove background)

    # Resize image
    image_width, image_height = image.size
    if image_width > image_height and image_width != OUT_WIDTH:
        coefficient = OUT_WIDTH / image_width
    else:
        coefficient = OUT_HEIGHT / image_height

    image_height = image_height * coefficient
    image_width = image_width * coefficient
    output_size = (int(image_width), int(image_height))
    image = image.resize(output_size)

    # Save as WEBP with desired quality
    image.save(output_path, 'WEBP', quality=quality)
