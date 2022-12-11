import cv2
from skimage import data

# from: https://scikit-image.org/docs/stable/auto_examples/data/plot_scientific.html#sphx-glr-auto-examples-data-plot-scientific-py

images = (
    "hubble_deep_field",
    "immunohistochemistry",
    # "lily", # .tif file, ignoring for simplicity
    "microaneurysms",
    "moon",
    "retina",
    "shepp_logan_phantom",
    "skin",
    "cell",
    "human_mitosis",
)

for name in images:
    # images might not be png, does not really matter much for this proof of concept
    cv2.imwrite(f"images/{name}.png", getattr(data, name)())
