import os

import ConvertFunctions
import Decor
from Config import INPUT_DIR, OUTPUT_DIR


@Decor.timer
@Decor.memoize
def main():
    """
    Main function to convert PNG images to WEBP format with various options.

    This function prompts the user to choose from different conversion options:
    1. Convert image from PNG to WEBP without resize.
    2. Convert image from PNG to WEBP with watermark and resize.
    3. Convert image from PNG to WEBP with resize.

    It then iterates over all PNG files in the INPUT_DIR directory, processes each file based on the chosen option,
    and saves the resulting WEBP files to the OUTPUT_DIR directory.

    Returns:
        None
    """
    choice = input("1. Convert image from PNG to WEBP without resize\n"
                   "2. Convert image from PNG to WEBP with watermark and resize\n"
                   "3. Convert image from PNG to WEBP with resize\n\n"
                   " Choice:  ")

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith('.png'):
            print(f'Processing {filename}...')
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + '.webp')
            if choice == '1':
                ConvertFunctions.convert_image(input_path, output_path)
            elif choice == '2':
                ConvertFunctions.convert_image_with_watermark_and_resize(input_path, output_path)
            elif choice == '3':
                ConvertFunctions.convert_image_with_resize(input_path, output_path)
            else:
                print("Wrong input")
                exit(-1)


if __name__ == "__main__":
    main()
