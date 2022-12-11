# type: ignore
import cv2
import matplotlib.pyplot as plt
from loguru import logger

from service.models import NpImage
from service.proxy import BioImageProcessingProxy
from service.task_detect_ridges import task_detect_ridges

image_filename = "images/retina.png"
logger.info(f"Analysing {image_filename}")

# create a proxy to talk to the bio image processing service
proxy = BioImageProcessingProxy()

# read some image
logger.info("Opening image...")

image: NpImage = cv2.imread(image_filename)

# send the image for processing to the service
logger.info("Send to service...")
processed = proxy.detect_ridges(image)
logger.info("Done!")


# show original and processed images
f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(image)
axarr[0, 1].imshow(processed.grayscale_image, cmap="gray")
axarr[1, 0].imshow(processed.processed_image, cmap="gray")
axarr[1, 1].imshow(processed.processed_image_inverted, cmap="gray")

plt.show()
