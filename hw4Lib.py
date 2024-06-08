import cv2
import numpy as np

def max_filter(img, row, columm):
    spatial_filter = np.zeros((img.shape[0], img.shape[1]))
    filterType = "max"

    for i in range(img.shape[0] - row - 1):
        for j in range(img.shape[1] - columm - 1):
            if filterType == "max":
                spatial_filter[i + 1][j + 1] = np.amax(img[i:i + row, j:j + columm])

    final_image_array = spatial_filter
    final_image_array = np.require(final_image_array, np.uint8, 'C')

    return final_image_array

def min_filter(img, row, columm):
    spatial_filter = np.zeros((img.shape[0], img.shape[1]))

    for i in range(img.shape[0] - row - 1):
        for j in range(img.shape[1] - columm - 1):
            spatial_filter[i + 1][j + 1] = np.amin(img[i:i + row, j:j + columm])

    final_image_array = spatial_filter
    final_image_array = np.require(final_image_array, np.uint8, 'C')

    return final_image_array

def median_filter(img, row, columm):
    spatial_filter = np.zeros((img.shape[0], img.shape[1]))

    for i in range(img.shape[0] - row - 1):
        for j in range(img.shape[1] - columm - 1):
            spatial_filter[i + 1][j + 1] = np.median(img[i:i + row, j:j + columm])

    final_image_array = spatial_filter
    final_image_array = np.require(final_image_array, np.uint8, 'C')

    return final_image_array

def average_filter(img, row, columm):
    spatial_filter = np.zeros((img.shape[0], img.shape[1]))

    for i in range(img.shape[0] - row - 1):
        for j in range(img.shape[1] - columm - 1):
            spatial_filter[i + 1][j + 1] = np.mean(img[i:i + row, j:j + columm])

    final_image_array = spatial_filter
    final_image_array = np.require(final_image_array, np.uint8, 'C')

    return final_image_array

def laplace(img):
    F1 = [[0, 1, 0], [1, -4, 1], [0, 1, 0]];
    filteredImage = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0] - 2):
        for j in range(img.shape[1] - 2):
            dot_product = np.dot(F1, img[i:i + 3, j:j + 3])
            summationResult = sum(map(sum, dot_product))
            filteredImage[i + 1][j + 1] = summationResult
    "Laplace"
    filteredImage = cv2.Laplacian(img, cv2.CV_64F)
    return filteredImage

def sobels(img):
    kernel_x = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
    kernel_y = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])
    [rows, columns] = np.shape(img)
    sobel_filtes = np.zeros(shape=(rows, columns))
    for i in range(rows - 2):
        for j in range(columns - 2):
            gx = np.sum(np.multiply(kernel_x, img[i:i + 3, j:j + 3]))
            gy = np.sum(np.multiply(kernel_y, img[i:i + 3, j:j + 3]))
            sobel_filtes[i + 1, j + 1] = np.sqrt(gx ** 2 + gy ** 2)
    sobel_filtes = np.require(sobel_filtes, np.uint8, 'C')
    return sobel_filtes

def sobel_filter(img):
    final_image_array = sobels(img)
    return final_image_array

def sobelMask(img):
    mask = cv2.blur(img, (5, 5))
    return mask

def sobel_mask_filter(img):
    final_image_array = sobels(img)
    final_image_array = sobelMask(final_image_array)
    return final_image_array

def laplacian_filter(img):
    laplacia_array = laplace(img)
    laplacia_array = (((laplacia_array - laplacia_array.min()) / (
            laplacia_array.max() - laplacia_array.min())) * 255.9).astype(np.uint8)
    return laplacia_array

def sharpened_filter(img):
    laplacia_array = laplace(img)
    laplacia_array = np.uint8(np.absolute((laplacia_array)))
    sharpened_filter = cv2.add(img, laplacia_array)
    return sharpened_filter

def f_filter(img):
    final_image_array = sobels(img)
    blur_filter = sobelMask(final_image_array)
    laplacia_array = laplace(img)
    laplacia_array = np.uint8(np.absolute((laplacia_array)))
    shape_filter = cv2.add(img, laplacia_array)
    masked_image = cv2.bitwise_and(blur_filter, shape_filter)
    return masked_image

def g_filter(img):
    final_image_array = sobels(img)
    blur_filter = sobelMask(final_image_array)
    laplacia_array = laplace(img)
    laplacia_array = np.uint8(np.absolute((laplacia_array)))
    shape_filter = cv2.add(img, laplacia_array)
    masked_image = cv2.bitwise_and(blur_filter, shape_filter)
    g_filters = cv2.add(img, masked_image)
    return g_filters

def power_low_filter(img):
    final_image_array = sobels(img)
    blur_filter = sobelMask(final_image_array)

    laplacia_array = laplace(img)
    laplacia_array = np.uint8(np.absolute((laplacia_array)))
    shape_filter = cv2.add(img, laplacia_array)

    masked_image = cv2.bitwise_and(blur_filter, shape_filter)
    g_filters = cv2.add(img, masked_image)
    powerImg = np.array(255 * (g_filters / 255) ** 0.5, dtype='uint8')
    return powerImg
