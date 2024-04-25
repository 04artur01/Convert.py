# Define the path to the watermark image file
WATERMARK_PATH = ""  # Insert the path to the watermark image file

# Define the input directory containing PNG images to be processed
INPUT_DIR = ""  # Insert the path to the input directory containing PNG images

# Define the output directory where converted WEBP images will be saved
OUTPUT_DIR = ""  # Insert the path to the output directory for saving WEBP images

# Define the width of the output images
OUT_WIDTH = int(input("Insert output width\n"))

# Define the height of the output images
OUT_HEIGHT = int(input("Insert output height\n"))


def set_paths(watermark_path: str, input_dir: str, output_dir: str, out_width: int, out_height: int):
    """
    Set the paths and dimensions for image conversion.

    Args:
        watermark_path (str): The path to the watermark image file.
        input_dir (str): The path to the input directory containing PNG images.
        output_dir (str): The path to the output directory for saving WEBP images.
        out_width (int): The width of the output images.
        out_height (int): The height of the output images.
    """
    global WATERMARK_PATH, INPUT_DIR, OUTPUT_DIR, OUT_WIDTH, OUT_HEIGHT
    WATERMARK_PATH = watermark_path
    INPUT_DIR = input_dir
    OUTPUT_DIR = output_dir
    OUT_WIDTH = out_width
    OUT_HEIGHT = out_height


# Example usage:
# set_paths(r"D:\Pharm Center\PHC photos end 1\watermark.png",
#           r"D:\Pharm Center\PHC photos end 1\test",
#           r"D:\Pharm Center\PHC photos end 1\test2",
#           int(input("Insert output width\n")),
#           int(input("Insert output height\n")))
