import easyocr
import cv2
from matplotlib import pyplot as plt

# Initialize reader
reader = easyocr.Reader(['en'])

# Load your image
image_path = 'download.png'  # Change this to your image
results = reader.readtext(image_path)

# Print OCR results
for (bbox, text, prob) in results:
    print(f"Detected: {text} (Confidence: {prob:.2f})")

    # Optional: Show bounding boxes
    top_left = tuple([int(val) for val in bbox[0]])
    bottom_right = tuple([int(val) for val in bbox[2]])
    image = cv2.rectangle(cv2.imread(image_path), top_left, bottom_right, (0, 255, 0), 2)

# Show the image with detected text
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
