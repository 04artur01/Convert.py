from PIL import Image

import Decor
from Config import WATERMARK_PATH, OUT_HEIGHT, OUT_WIDTH


@Decor.memoize
def convert_image_with_watermark_and_resize(input_path, output_path, quality=100):
    """
    Convert an image from PNG to WEBP format with a watermark and resizing on a background.

    Args:
        input_path (str): The path to the input PNG image file.
        output_path (str): The path to save the output WEBP image file.
        quality (int, optional): The quality of the output WEBP image (default is 100).

    Returns:
        None
    """

    image = Image.open(input_path)
    if image.mode != 'RGBA':
        image = image.convert('RGBA')  # Ensure image has transparency

    image.convert('RGBA').putalpha(255)

    watermark = Image.open(WATERMARK_PATH).convert('RGBA')  # Ensure watermark has transparency
    # Remove background from watermark
    watermark_data = watermark.getdata()
    new_data = []
    for item in watermark_data:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            new_data.append((255, 255, 255, 0))  # Make white pixels transparent
        else:
            new_data.append(item)
    watermark.putdata(new_data)

    # Create background
    background_color = (241, 241, 241)  # Light gray background
    background = Image.new('RGB', (OUT_WIDTH, OUT_HEIGHT), background_color)

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

    # Paste the image onto the background, centering it
    offset = ((OUT_WIDTH - image.width) // 2, (OUT_HEIGHT - image.height) // 2)
    background.paste(image, offset, image)

    # Resize watermark to fit the background
    watermark.thumbnail((OUT_WIDTH, OUT_HEIGHT))

    # Add watermark to the background
    background.paste(watermark, (0, 0), watermark)  # Paste at top-left corner

    # Save as WEBP with desired quality
    background.save(output_path, 'WEBP', quality=quality)

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
