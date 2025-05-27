# -*- coding: utf-8 -*-
import random
import os
from PIL import Image
import cv2
import numpy as np


# Method 3: Random crop with scale factor (percentage of original size)
def random_crop_scale(image_path, output_path, scale_range=(0.5, 0.9)):
    """
    Random crop with random scale factor
    Args:
        scale_range: tuple (min_scale, max_scale) as percentage of original size
    """
    image = Image.open(image_path)
    img_width, img_height = image.size

    # Random scale factor
    scale = random.uniform(scale_range[0], scale_range[1])
    crop_width = int(img_width * scale)
    crop_height = int(img_height * scale)

    # Generate random crop coordinates
    left = random.randint(0, img_width - crop_width)
    top = random.randint(0, img_height - crop_height)
    right = left + crop_width
    bottom = top + crop_height

    # Crop the image
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)
    print(f"Random scaled crop saved to: {output_path}")
    print(f"Scale factor: {scale:.2f}, Crop size: ({crop_width}, {crop_height})")
    return True

if __name__ == "__main__":
    input_image = "C:\\Users\\25311\Desktop\YOLOv8helmet\datasets\广西大学南门口数据集\图片\\6.png"
    random_crop_scale(input_image, "C:\\Users\\25311\Desktop\YOLOv8helmet\datasets\广西大学南门口数据集\图片\\6cropped_scale.jpg", (0.5, 0.8))