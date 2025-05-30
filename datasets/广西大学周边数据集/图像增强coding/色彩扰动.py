# -*- coding: utf-8 -*-
"""
灰度变化处理示例：
1. 把任意 RGB 图像转换为灰度图；
2. 随机调整灰度图的亮度与对比度，得到“灰度扰动”版本；
3. 保存并对比显示三张图：原图（彩色）、标准灰度、扰动后灰度。
"""

from PIL import Image, ImageOps, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt

# === ① 读取原图 ===
img_path = 'C:\\Users\\25311\Desktop\YOLOv8helmet\datasets\广西大学南门口数据集\图片\8.png'          # ——>> 换成你的图片文件或绝对路径
img = Image.open(img_path).convert('RGB')

# === ② 转为灰度 ===
gray = ImageOps.grayscale(img)   # 仍然返回 PIL.Image，只是 mode='L'

# === ③ 自定义灰度扰动函数 ===
def grayscale_perturb(
    image: Image.Image,
    brightness_range=(0.8, 1.2),  # 整体亮度随机缩放系数
    contrast_range=(0.8, 1.2),    # 对比度随机缩放系数
    seed=None                     # 固定随机种子可复现
) -> Image.Image:
    if seed is not None:
        np.random.seed(seed)
    # 随机亮度
    b_factor = np.random.uniform(*brightness_range)
    image_b = ImageEnhance.Brightness(image).enhance(b_factor)
    # 随机对比度
    c_factor = np.random.uniform(*contrast_range)
    image_bc = ImageEnhance.Contrast(image_b).enhance(c_factor)
    return image_bc

# === ④ 生成扰动灰度图 ===
gray_perturbed = grayscale_perturb(gray)     # 可改 seed=123 复现

# === ⑤ 保存结果 ===
out_path = 'C:\\Users\\25311\Desktop\YOLOv8helmet\datasets\广西大学南门口数据集\图片\8_gray_perturbed.png'
gray_perturbed.save(out_path)

# === ⑥ 对比显示 ===
titles = ['Original (RGB)', 'Grayscale', 'Grayscale Perturbed']
images = [img, gray, gray_perturbed]
for i, im in enumerate(images):
    plt.figure(figsize=(4, 4))
    plt.imshow(im if i == 0 else im, cmap=None if i == 0 else 'gray')
    plt.axis('off')
    plt.title(titles[i])
    plt.tight_layout()
    plt.show()

print(f'扰动后灰度图已保存为: {out_path}')
