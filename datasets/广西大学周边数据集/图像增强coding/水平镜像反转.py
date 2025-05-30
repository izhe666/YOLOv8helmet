# -*- coding: utf-8 -*-
# 方法一：使用PIL/Pillow库
from PIL import Image


def flip_image_pil(image_path, output_path):
    """
    使用PIL库进行水平镜像反转
    """
    # 打开图片
    image = Image.open(image_path)

    # 水平镜像反转
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

    # 保存反转后的图片
    flipped_image.save(output_path)
    print(f"图片已保存到: {output_path}")


if __name__ == "__main__":
    input_path = "C:\\Users\\25311\Desktop\YOLOv8helmet\datasets\广西大学南门口数据集\图片\\5.png"  # 输入图片路径
    output_path = "C:\\Users\\25311\Desktop\YOLOv8helmet\datasets\广西大学南门口数据集\图片\\5flipped_image.png"  # 输出图片路径

    # 选择其中一种方法使用
    # 方法一：PIL (推荐，简单易用)
    flip_image_pil(input_path, output_path)