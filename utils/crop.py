import cv2
import pytesseract
from PIL import Image
from pathlib import Path

pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"
# Load the image
img = cv2.imread("static/images/Gokyo_no_waza.jpeg")

# Assume the image is divided into a 5x8 grid
rows = 5
cols = 8

# Calculate the width and height of each cell
cell_width = img.shape[1] // cols
cell_height = img.shape[0] // rows

for i in range(rows):
    for j in range(cols):
        # Crop the image
        crop_img = img[
            i * cell_height : (i + 1) * cell_height,
            j * cell_width : (j + 1) * cell_width,
        ]
        # Save the cropped image
        cv2.imwrite(f"static/images/crop_{i}_{j}.png", crop_img)
        # Use pytesseract to recognize the text
        text = (
            pytesseract.image_to_string(Image.open(f"static/images/crop_{i}_{j}.png"))
            .replace(" ", "_")
            .strip()
            .replace("\n", "")
            .lower()
        )
        # Rename image to the text
        Path(f"static/images/crop_{i}_{j}.png").rename(f"static/images/{text}.png")
