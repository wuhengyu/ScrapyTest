# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 10:48
# @Author  : Walter
# @File    : 缺口识别.py
# @License : (C)Copyright Walter
# @Desc    :
import cv2

GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 450

# 高斯滤波
def get_gaussian_blur_image(image):
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)

# 边缘检测
def get_canny_image(image):
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)


# 轮廓提取
def get_contours(image):
    contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def get_contour_area_threshold(image_width, image_height):
    contour_area_min = (image_width * 0.15) * (image_height * 0.25) * 0.8
    contour_area_max = (image_width * 0.15) * (image_height * 0.25) * 1.2
    return contour_area_min, contour_area_max

def get_arc_length_threshold(image_width, image_height):
    arc_length_min = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 0.8
    arc_length_max = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 1.2
    return arc_length_min, arc_length_max

def get_offset_threshold(image_width):
    offset_min = 0.2 * image_width
    offset_max = 0.85 * image_width
    return offset_min, offset_max

def main():
    image_raw = cv2.imread('img.png')
    # image_raw = cv2.imread('captcha.png')
    image_height, image_width, _ = image_raw.shape
    image_gaussian_blur = get_gaussian_blur_image(image_raw)
    image_canny = get_canny_image(image_gaussian_blur)
    contours = get_contours(image_canny)
    cv2.imwrite('image_canny.png', image_canny)
    cv2.imwrite('image_gaussian_blur.png', image_gaussian_blur)
    contour_area_min, contour_area_max = get_contour_area_threshold(image_width, image_height)
    arc_length_min, arc_length_max = get_arc_length_threshold(image_width, image_height)
    offset_min, offset_max = get_offset_threshold(image_width)
    offset = None
    n = 0
    for contour in contours:
        n += 1
        # print(contour)
        x, y, w, h = cv2.boundingRect(contour)
        print("x, y, w, h:", x, y, w, h)
        print("contour_area_min:", contour_area_min)
        print("contour_area_max:", contour_area_max)
        print("arc_length_min:", arc_length_min)
        print("arc_length_max:", arc_length_max)
        print("offset_min:", offset_min)
        print("offset_max:", offset_max)
        print(f"cv2.contourArea(contour):第{n}次", cv2.contourArea(contour))
        n += 1
        if contour_area_min < cv2.contourArea(contour) < contour_area_max and \
                arc_length_min < cv2.arcLength(contour, True) < arc_length_max and \
                offset_min < x < offset_max:
            cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 0, 255), 2)
            offset = x
    cv2.imwrite('image_label.png', image_raw)
    print('offset', offset)


if __name__ == '__main__':
    main()
