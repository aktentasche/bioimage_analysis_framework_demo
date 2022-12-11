# type: ignore
import cv2
import matplotlib.pyplot as plt

from service.task_detect_ridges import task_detect_ridges

image_filename = "images/retina.png"

# read some image
image = cv2.imread(image_filename)

# execute the task
processed = task_detect_ridges(image)

# show original and processed images
f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(image)
axarr[0, 1].imshow(processed.grayscale_image, cmap="gray")
axarr[1, 0].imshow(processed.processed_image, cmap="gray")
axarr[1, 1].imshow(processed.processed_image_inverted, cmap="gray")

plt.show()
