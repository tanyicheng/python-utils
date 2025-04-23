import cv2
import numpy as np
import os


def images_concat_vertical(left_img_path, right_img_path, concat_image_path, text=None):
    """
    :param left_img_path: 左侧图片本地路径（现在为上方图片路径）
    :param right_img_path: 右侧图片本地路径（现在为下方图片路径）
    :param concat_image_path: 拼接结果保存路径
    :param text: 批注文字
    :return: None
    """
    if not left_img_path and not right_img_path:
        return

    left_img = None
    right_img = None
    h_left, w_left = 0, 0
    h_right, w_right = 0, 0

    if left_img_path:
        left_img = cv2.imread(left_img_path)
        if left_img is not None:
            h_left, w_left = left_img.shape[:2]
    if right_img_path:
        right_img = cv2.imread(right_img_path)
        if right_img is not None:
            h_right, w_right = right_img.shape[:2]

    # 处理图像宽度不一致的情况
    if w_left!= w_right:
        if w_left > w_right:
            right_img = cv2.resize(right_img, (w_left, h_right))
        else:
            left_img = cv2.resize(left_img, (w_right, h_left))
        h_right, w_right = right_img.shape[:2]
        h_left, w_left = left_img.shape[:2]

    h_final = h_left + h_right
    w_final = max(w_left, w_right)
    if text:
        h_final += 20

    canvas = np.zeros([h_final, w_final, 3], np.uint8)

    if left_img_path and right_img_path:
        if left_img is not None and right_img is not None:
            canvas[0:h_left, 0:w_final] = left_img
            canvas[h_left:h_final, 0:w_final] = right_img
    elif left_img_path:
        if left_img is not None:
            canvas[0:h_left, 0:w_final] = left_img
    elif right_img_path:
        if right_img is not None:
            canvas[0:h_right, 0:w_final] = right_img

    if text:
        cv2.putText(canvas, text, (5, h_final - 5), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)

    cv2.imwrite(concat_image_path, canvas)


# 示例用法，这里假设图片在以下三个具体目录中，可根据实际情况修改
img_a_dir = r'D:\my_images\top_image_folder'
img_b_dir = r'D:\my_images\bottom_image_folder'
img_c_dir = r'D:\my_images\concat_image_folder'

a_name = os.listdir(img_a_dir)
b_name = os.listdir(img_b_dir)

for a in a_name:
    for b in b_name:
        if a == b:
            top_img_path = os.path.join(img_a_dir, a)
            bottom_img_path = os.path.join(img_b_dir, b)
            concat_image_path = os.path.join(img_c_dir, a)

            images_concat_vertical(top_img_path, bottom_img_path, concat_image_path)

print(len(a_name))
print('success')