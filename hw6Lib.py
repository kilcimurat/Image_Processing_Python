import cv2
import numpy as np
import random


def contrast_stretching(img, blackT, whiteT):
    row, column, channel = img.shape
    new_image = np.zeros((row, column, channel), np.uint8)
    treshold_1 = blackT
    treshold_2 = whiteT
    if treshold_1 > treshold_2:
        treshold_1 = whiteT
        treshold_2 = blackT
    for l in range(row):
        for m in range(column):
            if treshold_1 <= img[l, m, 0] <= treshold_2:
                new_image[l, m, 0] = round(((img[l, m, 0] - treshold_1) / (treshold_2 - treshold_1)) * 255)
            elif img[l, m, 0] < treshold_1:
                new_image[l, m, 0] = 0
            elif img[l, m, 0] > treshold_2:
                new_image[l, m, 0] = 255
            if treshold_1 <= img[l, m, 1] <= treshold_2:
                new_image[l, m, 1] = round(((img[l, m, 1] - treshold_1) / (treshold_2 - treshold_1)) * 255)
            elif img[l, m, 1] < treshold_1:
                new_image[l, m, 1] = 0
            elif img[l, m, 1] > treshold_2:
                new_image[l, m, 1] = 255
            if treshold_1 <= img[l, m, 2] <= treshold_2:
                new_image[l, m, 2] = round(((img[l, m, 2] - treshold_1) / (treshold_2 - treshold_1)) * 255)
            elif img[l, m, 2] < treshold_1:
                new_image[l, m, 2] = 0
            elif img[l, m, 2] > treshold_2:
                new_image[l, m, 2] = 255
    return new_image


def histogram_stretching(img):
    img = img.astype(np.float64)

    img = (img - img.min()) / (img.max() - img.min()) * 255
    img = img.astype(np.uint8)
    return img


def histogram_equalization(img):
    row, column, channel = img.shape
    unique, counts = np.unique(img, return_counts=True)
    sum = 0
    newlistValue = []
    newlistPixel = []
    newlistCDF = []
    newlistEq = []
    for i in range(len(counts)):
        a = unique[i]
        b = counts[i] = counts[i] / 3
        newlistValue.append(b)
        newlistPixel.append(a)

    for j in range(len(newlistValue)):
        sum = sum + newlistValue[j]
        newlistCDF.append(sum)

    for k in range(len(newlistValue)):
        cdfMin = np.min(newlistCDF)
        a = round(((newlistCDF[k] - cdfMin) / ((row * column) - cdfMin)) * 255)
        newlistEq.append(a)

    cdfDict = dict(zip(newlistPixel, newlistCDF))
    cdfDictEq = dict(zip(newlistPixel, newlistEq))
    for l in range(row):
        for m in range(column):
            img[l, m, 0] = cdfDictEq[img[l, m, 0]]
            img[l, m, 1] = cdfDictEq[img[l, m, 1]]
            img[l, m, 2] = cdfDictEq[img[l, m, 2]]

    return img


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


def gaus(img):

    row,col= img.shape

    mean = 0
    var = 300
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, (row, col)) #  np.zeros((224, 224), np.float32)

    noisy_image = np.zeros(img.shape, np.float32)

    if len(img.shape) == 2:
        noisy_image = img + gaussian
    else:
        noisy_image[:, :, 0] = img[:, :, 0] + gaussian
        noisy_image[:, :, 1] = img[:, :, 1] + gaussian
        noisy_image[:, :, 2] = img[:, :, 2] + gaussian

    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    noisy_image = noisy_image.astype(np.uint8)



    return noisy_image



def sp_noise_salt(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()

            if rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def sp_noise_pep(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0

            else:
                output[i][j] = image[i][j]
    return output


def sp_noise_sandp(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255

            else:
                output[i][j] = image[i][j]
    return output


def passion_noise(image):
    row, col = image.shape
    mean =0
    var = 2

    sigma = var ** 0.2
    poisson_noisy = np.random.poisson(image / 255.0 * sigma) / sigma * 255
    return poisson_noisy


