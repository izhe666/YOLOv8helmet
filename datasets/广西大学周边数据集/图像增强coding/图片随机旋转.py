# -*- coding: utf-8 -*-
import random
import os
import math
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os
os.environ["OPENCV_IO_ENABLE_UTF8"] = "1"

def random_rotate_opencv(image_path, output_path=None, angle_range=(-180, 180)):
    """
    使用OpenCV实现图像随机旋转

    Args:
        image_path: 输入图像路径
        output_path: 输出图像路径（可选）
        angle_range: 旋转角度范围，默认(-180, 180)

    Returns:
        rotated_image: 旋转后的图像
    """
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"无法读取图像: {image_path}")

    # 生成随机旋转角度
    angle = random.uniform(angle_range[0], angle_range[1])

    # 获取图像尺寸
    height, width = image.shape[:2]
    center = (width // 2, height // 2)

    # 计算旋转矩阵
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # 计算旋转后的图像边界
    cos_val = abs(rotation_matrix[0, 0])
    sin_val = abs(rotation_matrix[0, 1])
    new_width = int((height * sin_val) + (width * cos_val))
    new_height = int((height * cos_val) + (width * sin_val))

    # 调整旋转矩阵以避免裁剪
    rotation_matrix[0, 2] += (new_width / 2) - center[0]
    rotation_matrix[1, 2] += (new_height / 2) - center[1]

    # 执行旋转
    rotated_image = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))

    # 保存图像
    if output_path:
        cv2.imwrite(output_path, rotated_image)
        print(f"旋转角度: {angle:.2f}°")
        print(f"图像已保存到: {output_path}")

    return rotated_image, angle



# 使用示例
if __name__ == "__main__":
    # 设置随机种子（可选，用于复现结果）
    random.seed(42)

    # 示例1: 使用OpenCV旋转单张图像
    try:
        image_path = r"C:\Users\25311\Desktop\YOLOv8helmet\datasets\7.png"  # 替换为你的图像路径
        output_path = "/datasets/广西大学周边数据集/图片/7rotated_opencv.png"

        rotated_img, angle = random_rotate_opencv(image_path, output_path, (-45, 45))
        print("OpenCV旋转完成")
    except Exception as e:
        print(f"OpenCV旋转失败: {e}")