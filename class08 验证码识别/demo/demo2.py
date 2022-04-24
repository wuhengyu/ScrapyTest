# -*- coding: utf-8 -*-
# @Time    : 2022/4/23 22:27
# @Author  : Walter
# @File    : demo2.py
# @License : (C)Copyright Walter
# @Desc    :
import cv2

GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 450


def get_gaussian_blur_image(image):
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)


def get_canny_image(image):
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)


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
    image_raw1 = cv2.imread('img.png')
    image_raw2 = cv2.imread('captcha.png')

    image_height1, image_width1, _1 = image_raw1.shape
    image_height2, image_width2, _2 = image_raw2.shape

    image_gaussian_blur1 = get_gaussian_blur_image(image_raw1)
    image_gaussian_blur2 = get_gaussian_blur_image(image_raw2)

    image_canny1 = get_canny_image(image_gaussian_blur1)
    image_canny2 = get_canny_image(image_gaussian_blur2)

    contours1 = get_contours(image_canny1)
    contours2 = get_contours(image_canny2)

    cv2.imwrite('image_canny1.png', image_canny1)
    cv2.imwrite('image_canny2.png', image_canny2)

    cv2.imwrite('image_gaussian_blur1.png', image_gaussian_blur1)
    cv2.imwrite('image_gaussian_blur2.png', image_gaussian_blur2)

    contour_area_min1, contour_area_max1 = get_contour_area_threshold(image_width1, image_height1)
    contour_area_min2, contour_area_max2 = get_contour_area_threshold(image_width2, image_height2)

    arc_length_min1, arc_length_max1 = get_arc_length_threshold(image_width1, image_height1)
    arc_length_min2, arc_length_max2 = get_arc_length_threshold(image_width2, image_height2)

    offset_min1, offset_max1 = get_offset_threshold(image_width1)
    offset_min2, offset_max2 = get_offset_threshold(image_width1)

    offset1 = None
    offset2 = None

    for contour1 in contours1:
        x1, y1, w1, h1 = cv2.boundingRect(contour1)
        if contour_area_min1 < cv2.contourArea(contour1) < contour_area_max1 and \
                arc_length_min1 < cv2.arcLength(contour1, True) < arc_length_max1 and \
                offset_min1 < x1 < offset_max1:
            cv2.rectangle(image_raw1, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
            offset1 = x1

    for contour2 in contours2:
        x2, y2, w2, h2 = cv2.boundingRect(contour2)
        if contour_area_min2 < cv2.contourArea(contour2) < contour_area_max2 and \
                arc_length_min2 < cv2.arcLength(contour2, True) < arc_length_max2 and \
                offset_min2 < x2 < offset_max2:
            cv2.rectangle(image_raw2, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)
            offset2 = x2

    cv2.imwrite('image_label1.png', image_raw1)
    cv2.imwrite('image_label2.png', image_raw2)

    print('offset1', offset1)
    print('offset2', offset2)





if __name__ == '__main__':
    main()