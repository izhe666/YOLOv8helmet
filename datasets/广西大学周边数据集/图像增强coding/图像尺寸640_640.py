# -*- coding: utf-8 -*-
from PIL import Image

# 加载图片
image_path = "C:\\Users\\25311\Desktop\YOLOv8helmet\datasets\广西大学南门口数据集\图片\\3.png"
image = Image.open(image_path)

# 设定裁剪尺寸
crop_size = 640
width, height = image.size

# 计算中心裁剪区域的坐标
left = (width - crop_size) / 2
top = (height - crop_size) / 2
right = (width + crop_size) / 2
bottom = (height + crop_size) / 2

# 裁剪图片
cropped_image = image.crop((left, top, right, bottom))

# 保存裁剪后的图片
cropped_image.save("C:\\Users\\25311\Desktop\YOLOv8helmet\datasets\广西大学南门口数据集\图片\\3_640_640.png")
