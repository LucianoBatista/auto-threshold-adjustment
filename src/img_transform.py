import cv2 as cv
import numpy as np


def image_transformation(thresh_param, image):

    kernel_7_7 = np.ones((7, 7), np.float32) / 49
    card_warp_colored_blurred = cv.filter2D(image, -1, kernel_7_7)

    img_warp_gray = cv.cvtColor(card_warp_colored_blurred, cv.COLOR_BGR2GRAY)
    img_black_and_white = cv.threshold(
        img_warp_gray, thresh_param, 255, cv.THRESH_BINARY
    )[1]
    img_threshold = cv.threshold(img_black_and_white, 215, 350, cv.THRESH_BINARY_INV)[1]

    return img_threshold
