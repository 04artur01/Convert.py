import os

import ConvertFunctions
import Decor
from Config import INPUT_DIR, OUTPUT_DIR


@Decor.timer
@Decor.memoize
def main():
    choice = input("1. Convert image from PNG to WEBP\n"
                   "2. Convert image from PNG to WEBP with watermark\n\n"
                   " Choice:  ")

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith('.png'):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + '.webp')
            if choice == '1':
                ConvertFunctions.convert_image(input_path, output_path)
            elif choice == '2':
                ConvertFunctions.convert_image_with_watermark(input_path, output_path)
            else:
                print("Wrong input")
                exit(-1)


if __name__ == "__main__":
    main()
