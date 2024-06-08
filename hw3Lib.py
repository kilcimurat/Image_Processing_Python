import cv2
import numpy as np



def contrast_stretching(img,blackT,whiteT):
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

    cdfDict= dict(zip(newlistPixel, newlistCDF))
    cdfDictEq = dict(zip(newlistPixel, newlistEq))
    for l in range(row):
        for m in range(column):
            img[l, m, 0] = cdfDictEq[img[l, m, 0]]
            img[l, m, 1] = cdfDictEq[img[l, m, 1]]
            img[l, m, 2] = cdfDictEq[img[l, m, 2]]

    return img