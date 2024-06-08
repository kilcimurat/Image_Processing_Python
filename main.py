# Murat KILCI 190403023
# Image Process Homework 3

import math
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QScrollBar, QLabel, QTextBrowser, QTextEdit, QLineEdit, QRadioButton,QMessageBox,QSlider
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import cv2 as cv
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from PIL import Image
import os
import numpy as np
from hw2Lib import ImageProcessing
import hw3Lib
import hw4Lib
import hw6Lib
from matplotlib import pyplot as plt
import webbrowser
import noises
from skimage import io, img_as_float, color, restoration
from PIL.ImageQt import fromqpixmap





class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("image_and_ui/imageUi.ui",self)

        self.image = None
        self.file_path = ""
        self.imageHistory = None

        #Dashboard
        self.logOutButton = self.findChild(QPushButton, "logOutButton")
        self.youtubeButton = self.findChild(QPushButton, "youtubeButton")
        self.instagramButton = self.findChild(QPushButton, "instagramButton")
        self.linkedInlBUtton = self.findChild(QPushButton, "linkedInlBUtton")
        self.githubButton = self.findChild(QPushButton, "githubButton")
        self.supportButton = self.findChild(QPushButton, "supportButton")
        self.logoButton = self.findChild(QPushButton, "logoButton")
        
        self.logOutButton.clicked.connect(self.log_out)
        self.youtubeButton.clicked.connect(self.youtube_logo)
        self.instagramButton.clicked.connect(self.intagram_logo)
        self.linkedInlBUtton.clicked.connect(self.linkedIn_logo)
        self.githubButton.clicked.connect(self.github_logo)
        self.logoButton.clicked.connect(self.uni_logo)
        self.supportButton.clicked.connect(self.support_logo)


        #HW1
        self.convertButton = self.findChild(QPushButton, "convert")
        self.fileButton = self.findChild(QPushButton, "pushButton")
        self.mainImage = self.findChild(QLabel, "mainImage")
        self.processedImage = self.findChild(QLabel, "newImage")
        self.path = self.findChild(QLabel, "label")
        self.rgb = self.findChild(QLabel, "label_2")
        self.row = self.findChild(QLineEdit, "Row")
        self.column = self.findChild(QLineEdit, "Column")
        self.grayscale = self.findChild(QRadioButton, "radioButton")
        self.convertButton.clicked.connect(self.makeBlur)
        self.fileButton.clicked.connect(self.chooseImage)

        #HW2
        self.chooseBtn = self.findChild(QPushButton,"chooseBtn")
        self.push_button_reflect = self.findChild(QPushButton,"push_button_reflect")
        self.push_button_crop = self.findChild(QPushButton,"push_button_crop")
        self.push_button_resize = self.findChild(QPushButton,"push_button_resize")
        self.push_button_shift = self.findChild(QPushButton,"push_button_shift")
        self.push_button_rgb_hsi = self.findChild(QPushButton,"push_button_rgb_hsi")
        self.btn_refresh = self.findChild(QPushButton,"btn_refresh")
        self.line_edit_shift = self.findChild(QLineEdit,"line_edit_shift")
        self.radio_button_vertical = self.findChild(QRadioButton,"radio_button_vertical")
        self.radio_button_horizontal = self.findChild(QRadioButton,"radio_button_horizontal")
        self.radio_button_crossed = self.findChild(QRadioButton,"radio_button_crossed")
        self.radio_button_up = self.findChild(QRadioButton,"radio_button_up")
        self.radio_button_down = self.findChild(QRadioButton,"radio_button_down")
        self.radio_button_left = self.findChild(QRadioButton,"radio_button_left")
        self.radio_button_right = self.findChild(QRadioButton,"radio_button_right")
        self.line_edit_height = self.findChild(QLineEdit,"line_edit_height")
        self.line_edit_width = self.findChild(QLineEdit,"line_edit_width")
        self.line_edit_height_2 = self.findChild(QLineEdit,"line_edit_height_3")
        self.line_edit_width_2 = self.findChild(QLineEdit,"line_edit_width_3")
        self.resize_width = self.findChild(QLineEdit,"resize_width")
        self.resize_height = self.findChild(QLineEdit,"resize_height")
        self.radio_button_up = self.findChild(QRadioButton,"radio_button_up")
        self.radio_button_down = self.findChild(QRadioButton,"radio_button_down")
        self.radio_button_left = self.findChild(QRadioButton,"radio_button_left")
        self.radio_button_right = self.findChild(QRadioButton,"radio_button_right")
        self.chooseBtn.clicked.connect(self.open_file)
        self.push_button_reflect.clicked.connect(self.reflect_image)
        self.push_button_crop.clicked.connect(self.crop_image)
        self.push_button_resize.clicked.connect(self.resize_image)
        self.push_button_shift.clicked.connect(self.shift_image)
        self.push_button_rgb_hsi.clicked.connect(self.rgb_hsi)
        self.btn_refresh.clicked.connect(self.refresh)


        #HW3
        self.mainImage_2 = self.findChild(QLabel, "mainImage_2")
        self.processedImage_2 = self.findChild(QLabel, "newImage_2")
        self.openFile = self.findChild(QPushButton, "openFile")
        self.label_select = self.findChild(QLabel, "label_select")
        self.openFile.clicked.connect(self.coose_file_hw3)
        self.blackSlider = self.findChild(QSlider, "blackSlider")
        self.whiteSlider = self.findChild(QSlider, "whiteSlider")
        self.whiteSlider.valueChanged.connect(self.update)
        self.blackSlider.valueChanged.connect(self.update)
        self.equButton = self.findChild(QPushButton, "equButton")
        self.equButton.clicked.connect(self.equalzation)
        self.stretchButton = self.findChild(QPushButton, "strecthButton")
        self.stretchButton.clicked.connect(self.stretching)
        self.transferButton = self.findChild(QPushButton, "transferButton")
        self.transferButton.clicked.connect(self.transferFucntion)
        self.histogramButton = self.findChild(QPushButton, "histogramBtn")
        self.histogramButton.clicked.connect(self.showHistogram)

        #HW4      
        self.mainImage_HW4 = self.findChild(QLabel, "mainImage_HW4")
        self.processedImage_HW4 = self.findChild(QLabel, "newImage_HW4")
        self.row_HW4 = self.findChild(QLineEdit, "Row_HW4")
        self.column_HW4 = self.findChild(QLineEdit, "Column_HW4")
        self.fileButton_HW4 = self.findChild(QPushButton, "pushButton_HW4")
        self.path_HW4 = self.findChild(QLabel, "label_HW4")
        self.maxButton_HW4 = self.findChild(QPushButton, "maxFilter_HW4")
        self.minButton_HW4 = self.findChild(QPushButton, "minFilter_HW4")
        self.median_HW4 = self.findChild(QPushButton, "median_HW4")
        self.average_HW4 = self.findChild(QPushButton, "average_HW4")
        self.lapButton_HW4 = self.findChild(QPushButton, "laplacian_HW4")
        self.sharpButton_HW4 = self.findChild(QPushButton, "sharpenedIm_HW4")
        self.sobelButton_HW4 = self.findChild(QPushButton, "sobel_HW4")
        self.sobelMaskButton_HW4 = self.findChild(QPushButton, "sobelMask_HW4")
        self.partfButton_HW4 = self.findChild(QPushButton, "partF_HW4")
        self.partgButton_HW4 = self.findChild(QPushButton, "partG_HW4")
        self.powerlowButton_HW4 = self.findChild(QPushButton, "powerLow_HW4")
        self.powerlowButton_HW4.clicked.connect(self.power)
        self.fileButton_HW4.clicked.connect(self.fileClicker)
        self.maxButton_HW4.clicked.connect(self.max)
        self.minButton_HW4.clicked.connect(self.min)
        self.median_HW4.clicked.connect(self.medianFilter)
        self.average_HW4.clicked.connect(self.mean)
        self.lapButton_HW4.clicked.connect(self.laplacian1)
        self.sharpButton_HW4.clicked.connect(self.sharpened)
        self.sobelButton_HW4.clicked.connect(self.sobel1)
        self.sobelMaskButton_HW4.clicked.connect(self.sobelMask1)
        self.partfButton_HW4.clicked.connect(self.partF1)
        self.partgButton_HW4.clicked.connect(self.partG1)

        #HW5
        self.image_HW5_one = self.findChild(QLabel, "image_HW5_one")
        self.image_HW5_two = self.findChild(QLabel, "image_HW5_two")
        self.image_HW5_three = self.findChild(QLabel, "image_HW5_three")
        self.load_image_hw5 = self.findChild(QPushButton, "load_image_HW5")
        self.bhpf_button = self.findChild(QPushButton, "BHPF_button")
        self.bnr_button = self.findChild(QPushButton, "BNR_button")
        self.load_image_hw5.clicked.connect(self.clickloadimage)
        self.bhpf_button.clicked.connect(self.thumb_print)
        self.bnr_button.clicked.connect(self.pattern)

        #HW6
        self.mainImage6 = self.findChild(QLabel, "mainImage6")
        self.processedImage6 = self.findChild(QLabel, "newImage6")
        self.row6 = self.findChild(QLineEdit, "Row6")
        self.column6 = self.findChild(QLineEdit, "Column6")
        self.fileButton6 = self.findChild(QPushButton, "pushButton6")
        self.path6 = self.findChild(QLabel, "label6")
        self.fileButton6.clicked.connect(self.fileClicker6)
        self.grayscale6 = self.findChild(QRadioButton, "radioButton6")
        self.maxButton6 = self.findChild(QPushButton, "maxFilter6")
        self.maxButton6.clicked.connect(self.max6)
        self.minButton6 = self.findChild(QPushButton, "minFilter6")
        self.minButton6.clicked.connect(self.min6)
        self.median6 = self.findChild(QPushButton, "median6")
        self.median6.clicked.connect(self.medianFilter6)
        self.average6 = self.findChild(QPushButton, "average6")
        self.average6.clicked.connect(self.mean6)
        self.lapButton6 = self.findChild(QPushButton, "laplacian6")
        self.lapButton6.clicked.connect(self.laplacian16)
        self.sharpButton6 = self.findChild(QPushButton, "sharpenedIm6")
        self.sharpButton6.clicked.connect(self.sharpened6)
        self.sobelButton6 = self.findChild(QPushButton, "sobel6")
        self.sobelButton6.clicked.connect(self.sobel16)
        self.sobelMaskButton6 = self.findChild(QPushButton, "sobelMask6")
        self.sobelMaskButton6.clicked.connect(self.sobelMask16)
        self.partfButton6 = self.findChild(QPushButton, "partF6")
        self.partfButton6.clicked.connect(self.partF16)
        self.geometricFilterButton6 = self.findChild(QPushButton, "geometricFilter6")
        self.geometricFilterButton6.clicked.connect(self.geometricFilter)
        self.harmonicFilterButton6 = self.findChild(QPushButton, "harmonicFilter6")
        self.harmonicFilterButton6.clicked.connect(self.harmonicFilter)

        #HW7
        self.mainImage7 = self.findChild(QLabel, "mainImage7")
        self.newImage7 = self.findChild(QLabel, "newImage7")
        self.load7 = self.findChild(QPushButton, "load7")
        self.image71 = self.findChild(QPushButton, "image71")
        self.image72 = self.findChild(QPushButton, "image72")
        self.image73 = self.findChild(QPushButton, "image73")
        self.load7.clicked.connect(self.loadImage)
        self.image71.clicked.connect(self.image71func)
        self.image72.clicked.connect(self.image72func)

        #HW8
        
        self.load_button = QPushButton()
        self.main_window = uic.loadUi("image_and_ui/imageUi.ui", self)  
        self.main_window.dilation_button.clicked.connect(self.dilation)
        self.main_window.erosion_button.clicked.connect(self.erosion)
        self.main_window.opening_button.clicked.connect(self.opening)
        self.main_window.closing_button.clicked.connect(self.closing)
        self.main_window.gradient_button.clicked.connect(self.gradient)
        self.main_window.thresholding_button.clicked.connect(self.thresholding)
        self.main_window.that_button.clicked.connect(self.T_hat_transformation)
        self.main_window.bhat_button.clicked.connect(self.B_hat_transformation)
        self.main_window.threshold_that_button.clicked.connect(self.Thresholded_T_hat_transformation)
        self.main_window.closing_of_opening_button.clicked.connect(self.closingofopening)
        self.load_buttons.clicked.connect(self.load_image)
        self.main_window.th_value_slider.valueChanged.connect(self._slider_th_changed)
        self.main_window.th_value_slider.setValue(5)
        self.th_value = self.main_window.th_value_slider.value()
        self.main_window.th_value_slider.setMinimum(0)
        self.main_window.th_value_slider.setMaximum(10)

        self.main_window.kernel_slider.valueChanged.connect(self.kernel_size_changed)
        self.main_window.kernel_slider.setValue(3)
        self.kernel_size = self.main_window.kernel_slider.value()
        self.main_window.kernel_slider.setMinimum(0)
        self.main_window.kernel_slider.setMaximum(60)

        self.show()
        

#Dashboard

    def uni_logo(self):
        webbrowser.open('https://www.ikcu.edu.tr/')

    def github_logo(self):
        webbrowser.open('https://github.com/muratkilci')

    def youtube_logo(self):
        webbrowser.open('https://www.youtube.com/@ikcuelectricalandelectroni2451')
  
    def linkedIn_logo(self):
        webbrowser.open('https://www.linkedin.com/in/murat-kilci-4615961b9/')

    def intagram_logo(self):
        webbrowser.open('https://www.instagram.com/murat_kilci/?igshid=YmMyMTA2M2Y%3D')

    def log_out(self):
        self.close()

    def support_logo(self):
        recipient = 'murat_kilci@hotmail.com'
        subject = 'mysubject'
        body = 'This is a message' 
        mailto_link = f'mailto:{recipient}?subject={subject}&body={body}'
        webbrowser.open(mailto_link, new=1)



#HW 1
    def chooseImage(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self, "Open File", "c\\", "Image Files (*.jpg *.gif *.png)")
            image = cv.imread(self.fname[0])
            self.path.setText(self.fname[0])
            print(image)
            row_image, col_image = image.shape[:2]
            if len(image.shape) == 2:
                self.rgb.setText("Grayscale")
            else:
                self.rgb.setText("RGB")
            self.c = image
            new = self.fname[0]
            if self.row.text() or self.row.text() != "":
                new = self.makeBlur()
            if self.fname[0]:
                self.mainImage.setPixmap(QPixmap(self.fname[0]))
                self.mainImage.setScaledContents(True)
                self.mainImage.setAlignment(QtCore.Qt.AlignCenter)
            return self.fname[0]
        except:
            print("error")

    def makeBlur(self):
        try:
            if self.grayscale.isChecked():
                # Open an image
                image = cv.imread(self.path.text())
                # Convert the image to grayscale
                img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                # Get the block dimensions from the user
                block_dim_tuple = (int(float(self.row.text())), int(float(self.column.text())))
                # Get the dimensions of the image
                row_image, column_image = img.shape[:2]
                # If the block dimensions evenly divide the image dimensions
                if row_image % block_dim_tuple[0] == 0:                    
                    if column_image % block_dim_tuple[1] == 0:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            for j in range(0, column_image, block_dim_tuple[1]):
                                img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()
                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            for j in range(0, column_image, block_dim_tuple[1]):
                                if j + block_dim_tuple[1] > column_image:
                                    img[i:i + block_dim_tuple[0], j:column_image] = img[i:i + block_dim_tuple[0],j:column_image].mean()
                                else:
                                    img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()
                # If the block dimensions don't evenly divide the image dimensions
                if row_image % block_dim_tuple[0] != 0:
                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        img[i:row_image, j:column_image] = img[i:row_image,j:column_image].mean()
                                    else:
                                        img[i:row_image, j:j + block_dim_tuple[1]] = img[i:row_image,j:j + block_dim_tuple[1]].mean()
                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        img[i:i + block_dim_tuple[0], j:column_image] = img[i:i + block_dim_tuple[0],j:column_image].mean()
                                    else:
                                        img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()

                    else:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    img[i:row_image, j:j + block_dim_tuple[1]] = img[i:row_image,j:j + block_dim_tuple[1]].mean()
                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()

                cv.imwrite("new.png", img)
                print(img)
                self.processedImage.setPixmap(QPixmap("new.png"))
                self.processedImage.setScaledContents(True)
                self.processedImage.setAlignment(QtCore.Qt.AlignCenter)

                return img
            else:
                img = cv.imread(self.path.text())

                block_dim_tuple = (int(float(self.row.text())), int(float(self.column.text())))

                row_image, column_image = img.shape[:2]
                if row_image % block_dim_tuple[0] == 0:
                    if column_image % block_dim_tuple[1] == 0:

                        for i in range(0, row_image, block_dim_tuple[0]):
                            for j in range(0, column_image, block_dim_tuple[1]):
                                for k in  range(0,3):
                                    img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()


                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            for j in range(0, column_image, block_dim_tuple[1]):
                                if j + block_dim_tuple[1] > column_image:
                                    for k in range(0, 3):
                                        img[i:i + block_dim_tuple[0], j:column_image, k] = img[i:i + block_dim_tuple[0], j:column_image, k].mean()
                                else:
                                    for k in range(0, 3):
                                        img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()

                if row_image % block_dim_tuple[0] != 0:
                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        for k in range(0, 3):
                                            img[i:row_image, j:column_image, k] = img[i:row_image, j:column_image, k].mean()
                                    else:
                                        for k in range(0, 3):
                                            img[i:row_image, j:j + block_dim_tuple[1], k] = img[i:row_image, j:j + block_dim_tuple[1], k].mean()
                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        for k in range(0, 3):
                                            img[i:i + block_dim_tuple[0], j:column_image, k] = img[i:i + block_dim_tuple[0], j:column_image, k].mean()

                                    else:
                                        for k in range(0, 3):
                                            img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()
                    else:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    for k in range(0, 3):
                                        img[i:row_image, j:j + block_dim_tuple[1], k] = img[i:row_image, j:j + block_dim_tuple[1], k].mean()

                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    for k in range(0, 3):
                                        img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()
                cv.imwrite("new.png", img)
                print(img)

                self.processedImage.setPixmap(QPixmap("new.png"))
                self.processedImage.setScaledContents(True)
                self.processedImage.setAlignment(QtCore.Qt.AlignCenter)
        except:
            print("error")

        try:
            if self.grayscale.isChecked():
                # Open an image
                image = cv.imread(self.path.text())
                # Convert the image to grayscale
                img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                # Get the block dimensions from the user
                block_dim_tuple = (int(float(self.row.text())), int(float(self.column.text())))

                # Blur the image using block averaging with padding
                blurred_image = self.block_blur_with_padding(img, block_dim_tuple)

                cv.imwrite("new.png", blurred_image)
                print(blurred_image)
                self.processedImage.setPixmap(QPixmap("new.png"))
                self.processedImage.setScaledContents(True)
                self.processedImage.setAlignment(QtCore.Qt.AlignCenter)

                return blurred_image
            else:
                # Open an image
                image = cv.imread(self.path.text())

                # Get the block dimensions from the user
                block_dim_tuple = (int(float(self.row.text())), int(float(self.column.text())))

                # Blur the image using block averaging with padding
                blurred_image = self.block_blur_with_padding(image, block_dim_tuple)

                cv.imwrite("new.png", blurred_image)
                print(blurred_image)

                self.processedImage.setPixmap(QPixmap("new.png"))
                self.processedImage.setScaledContents(True)
                self.processedImage.setAlignment(QtCore.Qt.AlignCenter)
        except:
            print("error")

#HW2
    def refresh(self):
        self.image.refresh()
        self.image.show_image(self.graphics_view_output)

    def rgb_hsi(self):
        while True:
            if self.radio_button_vertical.isChecked():
                self.image.rgb_to_hsi_process()
            elif self.radio_button_horizontal.isChecked():
                self.image.hsi_to_rgb_process()
            self.image.show_image(self.graphics_view_output)
            break

    def shift_image(self):
        try:
            # if line_edit_shift is not empty take the value from the user and send it to the function
            if self.line_edit_shift.text() == "":
                return

            shift_value = int(self.line_edit_shift.text())
            # right or left or up or down
            if self.radio_button_up.isChecked():
                self.image.shifting_image_process("up", shift_value)
            elif self.radio_button_down.isChecked():
                self.image.shifting_image_process("down", shift_value)
            elif self.radio_button_left.isChecked():
                self.image.shifting_image_process("left", shift_value)
            elif self.radio_button_right.isChecked():
                self.image.shifting_image_process("right", shift_value)
            # convert brg to rgb
            if self.image.image_gray_scale is False:
                self.image.convert_image_bgr_to_rgb()
            self.image.show_image(self.graphics_view_output)
        except ValueError:
            QMessageBox.warning(self, "Warning", "Please enter a number")

    def crop_image(self):
        # take the values from the user and send them to the function
        try:
            x1 = int(self.line_edit_width.text())
            y1 = int(self.line_edit_height.text())
            x2 = int(self.line_edit_width_2.text())
            y2 = int(self.line_edit_height_2.text())
            self.image.crop_image_process(x1, y1, x2, y2)
            # bgr to rgb
            if self.image.image_gray_scale is False:
                self.image.convert_image_bgr_to_rgb()
            self.image.show_image(self.graphics_view_output)
        except ValueError:
            QMessageBox.warning(self, "Warning", "Please enter a number")

    def resize_image(self):
        # take the values from the user and send them to the function
        try:
            row = int(self.resize_height.text())
            column = int(self.resize_width.text())
            self.image.resize_image_process(row, column, self.graphics_view_output)
        except ValueError:
            QMessageBox.warning(self, "Warning", "Please enter a number")

    def open_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        self.image = ImageProcessing(self.file_path)
        self.image.show_image(self.graphics_view_input)

    def reflect_image(self):
        # check radio_button_horizontal and radio_button_vertical state assign the state of these buttons to the
        # variable and send the variable to the function
        if self.radio_button_crossed.isChecked():
            self.image.reflect_image_process(reflect_type="crossed")
        elif self.radio_button_horizontal.isChecked():
            self.image.reflect_image_process(reflect_type="horizontal")
        elif self.radio_button_vertical.isChecked():
            self.image.reflect_image_process(reflect_type="vertical")
        else:
            QMessageBox.warning(self, "Warning", "Please select a reflection type")

            # convert image bgr to rgb
        if self.image.image_gray_scale is False:
            self.image.convert_image_bgr_to_rgb()
        self.image.show_image(self.graphics_view_output)

#HW3
    def update(self):
        self.row.setText(str(self.blackSlider.value()))
        self.column.setText(str(self.whiteSlider.value()))

    def transferFucntion(self):
        try:

            image = cv.imread(self.label_select.text())
            image = hw3Lib.contrast_stretching(image, self.blackSlider.value(), self.whiteSlider.value())
            self.imageHistory =image
            cv.imwrite("new.png", image)
            self.processedImage_2.setPixmap(QPixmap("new.png"))
            self.processedImage_2.setScaledContents(True)
            self.processedImage_2.setAlignment(QtCore.Qt.AlignCenter)
            image = self.imageHistory

        except:
            print("error")

    def equalzation(self):
        image = cv.imread(self.label_select.text())
        image = hw3Lib.histogram_equalization(image)
        self.imageHistory =image
        cv.imwrite("new.png", image)
        self.processedImage_2.setPixmap(QPixmap("new.png"))
        self.processedImage_2.setScaledContents(True)
        self.processedImage_2.setAlignment(QtCore.Qt.AlignCenter)
        image = self.imageHistory

    def stretching(self):
        image = cv.imread(self.label_select.text())
        image = hw3Lib.histogram_stretching(image)
        self.imageHistory =image
        cv.imwrite("new.png", image)
        self.processedImage_2.setPixmap(QPixmap("new.png"))
        self.processedImage_2.setScaledContents(True)
        self.processedImage_2.setAlignment(QtCore.Qt.AlignCenter)

    def coose_file_hw3(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
            image = cv.imread(self.fname[0])
            self.imageHistory =image
            self.label_select.setText(self.fname[0])
            print(image)
            row_image, col_image = image.shape[:2]
            self.c = image
            new = self.fname[0]
            if self.fname[0]:
                self.mainImage_2.setPixmap(QPixmap(self.fname[0]))
                self.mainImage_2.setScaledContents(True)
                self.mainImage_2.setAlignment(QtCore.Qt.AlignCenter)

            return self.fname[0]
        except:
            print("error")

    def showHistogram(self):
        try:
            image = self.imageHistory
            dst = cv.calcHist(image, [0], None, [256], [0,256])
            plt.hist(image.ravel(),256,[0,256])
            plt.title('Histogram for gray scale image')
            plt.show()
            
        except:
            print("error")

#HW4

    def imageUpdate(self):
        self.processedImage_HW4.setPixmap(QPixmap("new.png"))
        self.processedImage_HW4.setScaledContents(True)
        self.processedImage_HW4.setAlignment(QtCore.Qt.AlignCenter)

    def max(self):
        try:
            image = cv.imread(self.path_HW4.text())
            image = hw4Lib.max_filter(image,int(self.row_HW4.text()),int(self.column_HW4.text()))
            cv.imwrite("new.png", image)
            self.imageUpdate()
        except:
            QMessageBox.warning(self, "Warning", "Please enter row and collumn")

    def min(self):
        try:
            image = cv.imread(self.path_HW4.text())
            image = hw4Lib.min_filter(image,int(self.row_HW4.text()),int(self.column_HW4.text()))
            cv.imwrite("new.png", image)
            self.imageUpdate()
        except:
            QMessageBox.warning(self, "Warning", "Please enter row and collumn")
  
    def medianFilter(self):
        try:
            image = cv.imread(self.path_HW4.text())
            image = hw4Lib.median_filter(image,int(self.row_HW4.text()),int(self.column_HW4.text()))
            cv.imwrite("new.png", image)
            self.imageUpdate()
        except:
            QMessageBox.warning(self, "Warning", "Please enter row and collumn")
 
    def mean(self):
        try:
            image = cv.imread(self.path_HW4.text())
            image = hw4Lib.average_filter(image,int(self.row_HW4.text()),int(self.column_HW4.text()))
            cv.imwrite("new.png", image)
            self.imageUpdate()
        except:
            QMessageBox.warning(self, "Warning", "Please enter row and collumn")

    def laplacian1(self):
        image = cv.imread(self.path_HW4.text(),0)
        image = hw4Lib.laplacian_filter(image)
        cv.imwrite("new.png", image)
        self.imageUpdate()

    def sharpened(self):
        image = cv.imread(self.path_HW4.text(),0)
        image = hw4Lib.sharpened_filter(image)
        cv.imwrite("new.png", image)
        self.imageUpdate()

    def sobel1(self):
        image = cv.imread(self.path_HW4.text(),0)
        image = hw4Lib.sobel_filter(image)
        cv.imwrite("new.png", image)
        self.imageUpdate()

    def sobelMask1(self):
        image = cv.imread(self.path_HW4.text(),0)
        image = hw4Lib.sobel_mask_filter(image)
        cv.imwrite("new.png", image)
        self.imageUpdate()

    def partF1(self):
        image = cv.imread(self.path_HW4.text(),0)
        image = hw4Lib.f_filter(image)
        cv.imwrite("new.png", image)
        self.imageUpdate()

    def partG1(self):
        image = cv.imread(self.path_HW4.text(),0)
        image = hw4Lib.g_filter(image)
        cv.imwrite("new.png", image)
        self.imageUpdate()
  
    def power(self):
        image = cv.imread(self.path_HW4.text(),0)
        image = hw4Lib.power_low_filter(image)
        cv.imwrite("new.png", image)
        self.imageUpdate()

    def fileClicker(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
            image = cv.imread(self.fname[0])
            self.path_HW4.setText(self.fname[0])
            print(image)
            row_image, col_image = image.shape[:2]
            self.c = image
            new = self.fname[0]
            if self.row_HW4.text() or self.row_HW4.text() != "":
                new = self.change_block_size()
            if self.fname[0]:
                self.mainImage_HW4.setPixmap(QPixmap(self.fname[0]))
                self.mainImage_HW4.setScaledContents(True)
                self.mainImage_HW4.setAlignment(QtCore.Qt.AlignCenter)

            return self.fname[0]
        except:
            print("error")
  
    def change_block_size(self):
        try:
            if self.grayscale.isChecked():




                image = cv.imread(self.path_HW4.text())
                img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                block_dim_tuple = (int(float(self.row_HW4.text())), int(float(self.column_HW4.text())))



                row_image, column_image = img.shape[:2]
                if row_image % block_dim_tuple[0] == 0:
                    if column_image % block_dim_tuple[1] == 0:

                        for i in range(0, row_image, block_dim_tuple[0]):
                            for j in range(0, column_image, block_dim_tuple[1]):
                                img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()


                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):

                            for j in range(0, column_image, block_dim_tuple[1]):
                                if j + block_dim_tuple[1] > column_image:
                                    img[i:i + block_dim_tuple[0], j:column_image] = img[i:i + block_dim_tuple[0],j:column_image].mean()
                                else:
                                    img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()



                if row_image % block_dim_tuple[0] != 0:
                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        img[i:row_image, j:column_image] = img[i:row_image,j:column_image].mean()

                                    else:
                                        img[i:row_image, j:j + block_dim_tuple[1]] = img[i:row_image,j:j + block_dim_tuple[1]].mean()
                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        img[i:i + block_dim_tuple[0], j:column_image] = img[i:i + block_dim_tuple[0],j:column_image].mean()
                                    else:
                                        img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()

                    else:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    img[i:row_image, j:j + block_dim_tuple[1]] = img[i:row_image,j:j + block_dim_tuple[1]].mean()
                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()

                cv.imwrite("new.png", img)
                print(img)


                self.processedImage_HW4.setPixmap(QPixmap("new.png"))
                self.processedImage_HW4.setScaledContents(True)
                self.processedImage_HW4.setAlignment(QtCore.Qt.AlignCenter)

                return img
            else:
                img = cv.imread(self.path_HW4.text())

                block_dim_tuple = (int(float(self.row_HW4.text())), int(float(self.column_HW4.text())))

                row_image, column_image = img.shape[:2]
                if row_image % block_dim_tuple[0] == 0:
                    if column_image % block_dim_tuple[1] == 0:

                        for i in range(0, row_image, block_dim_tuple[0]):
                            for j in range(0, column_image, block_dim_tuple[1]):
                                for k in  range(0,3):
                                    img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()


                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):

                            for j in range(0, column_image, block_dim_tuple[1]):
                                if j + block_dim_tuple[1] > column_image:
                                    for k in range(0, 3):
                                        img[i:i + block_dim_tuple[0], j:column_image, k] = img[i:i + block_dim_tuple[0], j:column_image, k].mean()

                                else:
                                    for k in range(0, 3):
                                        img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()

                if row_image % block_dim_tuple[0] != 0:
                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        for k in range(0, 3):
                                            img[i:row_image, j:column_image, k] = img[i:row_image, j:column_image, k].mean()


                                    else:
                                        for k in range(0, 3):
                                            img[i:row_image, j:j + block_dim_tuple[1], k] = img[i:row_image, j:j + block_dim_tuple[1], k].mean()

                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        for k in range(0, 3):
                                            img[i:i + block_dim_tuple[0], j:column_image, k] = img[i:i + block_dim_tuple[0], j:column_image, k].mean()

                                    else:
                                        for k in range(0, 3):
                                            img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()

                    else:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    for k in range(0, 3):
                                        img[i:row_image, j:j + block_dim_tuple[1], k] = img[i:row_image, j:j + block_dim_tuple[1], k].mean()

                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    for k in range(0, 3):
                                        img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()


                cv.imwrite("new.png", img)
                print(img)

                self.processedImage_HW4.setPixmap(QPixmap("new.png"))
                self.processedImage_HW4.setScaledContents(True)
                self.processedImage_HW4.setAlignment(QtCore.Qt.AlignCenter)

        except:
            print("error")

#HW5
        
    def clickloadimage(self):  
        self.findimage = QFileDialog.getOpenFileName(self,"Select Image file to import",""," (*.jpg *.jpeg *.png *.tif *.bmp)")[0] #select open image
        self.openimage = cv.imread(self.findimage,0)#image to array
        self.images = Image.fromarray(self.openimage)
        self.images.save("newsizeimage.jpeg")
        self.newsizeimage = Image.open("newsizeimage.jpeg")
        self.newsizeimage = self.newsizeimage.resize((512, 512))
        self.newsizeimage.save("newsizeimage.jpeg")
        self.newsizeimage = QPixmap("newsizeimage.jpeg")
        self.image_HW5_one.setPixmap(self.newsizeimage)
        
    def butterworth_high_pass_filter(self,shape):
        d0 = 50  
        n = 4  
        rows, columns = shape
        mask = np.zeros((rows, columns))
        mid_R, mid_C = int(rows / 2), int(columns / 2) 
        for i in range(rows):
            for j in range(columns):
                d = math.sqrt((i - mid_R) ** 2 + (j - mid_C) ** 2) 
                if d == 0: 
                    mask[i, j] = 0
                else:
                    mask[i, j] = 1 / (1 + (d0 / d) ** (2 * n))
        return mask
    
    def thumb_print(self):
        fft = np.fft.fft2(self.openimage) 
        fft_shift = np.fft.fftshift(fft) 
        mask = self.butterworth_high_pass_filter(np.shape(self.openimage)) 
        filtered_image = np.multiply(mask, fft_shift) 
        shiftifft = np.fft.ifftshift(filtered_image) 
        ifft = np.uint8(np.real(np.fft.ifft2(shiftifft))) 
        mag = np.abs(np.fft.ifft2(shiftifft)) 
        filtered_image = np.uint8(mag) 
        thresholding_image = np.uint8(ifft) 
        
        im2 = Image.fromarray(filtered_image) 
        im2.save("resize.jpeg")                                    
        imag2 = Image.open("resize.jpeg")
        imag2 = imag2.resize((512, 512))
        imag2.save("newblurimages.jpeg")
        imag2= QPixmap("newblurimages.jpeg")
        self.image_HW5_two.setPixmap(imag2)

        im = Image.fromarray(thresholding_image) 
        im.save("resize.jpeg")                                    
        imag = Image.open("resize.jpeg")
        imag = imag.resize((512, 512))
        imag.save("newblurimages.jpeg")
        imag= QPixmap("newblurimages.jpeg")
        self.image_HW5_three.setPixmap(imag)
    
    def butterworth_notch_filter(self,image, d0=3, W=100, n=4):
        row, col = image.shape
        fftI = np.fft.fftshift(np.fft.fft2(image, (2*row-1, 2*col-1)))
        S = np.log(np.abs(fftI))
        
        x, y = np.meshgrid(np.arange(-256, 256), np.arange(-256, 256))
        D = np.sqrt(x**2 + y**2)
        
        notch_reject_filter = 1. / (1 + ((D * W) / (D**2 - d0**2))**(2 * n))
        
        filter_notch = np.zeros_like(fftI, dtype=np.complex128)
        
        for i in range(2*row-1):
            for j in range(2*col-1):
                dist = np.sqrt((i - (row))**2 + (j - (col))**2)
                band_pass_filter = 1. / (1 + ((dist * W) / (dist**2 - d0**2))**(2 * n))
                filter_notch[i, j] = 1 - band_pass_filter
        
        filtered_image = filter_notch * fftI
        filtered_image = np.fft.ifftshift(filtered_image)
        filtered_image = np.fft.ifft2(filtered_image, (2*row-1, 2*col-1))
        filtered_image = np.real(filtered_image[:row, :col])
        filtered_image = np.uint8(filtered_image)
        
        return S / np.max(S), filtered_image
        
    def pattern(self):
        image = self.openimage
        S, filtered_image = self.butterworth_notch_filter(image)


        # Display the magnitude spectrum
        im2 = Image.fromarray((S * 255).astype(np.uint8))  # normalize to 0-255
        im2.save("magnitude_spectrum.jpeg")
        imag2 = Image.open("magnitude_spectrum.jpeg")
        imag2 = imag2.resize((512, 512))
        imag2.save("magnitude_spectrum_resized.jpeg")
        imag2 = QPixmap("magnitude_spectrum_resized.jpeg")
        self.image_HW5_two.setPixmap(imag2)

        # Display the filtered image
        im = Image.fromarray(filtered_image)
        im.save("filtered_image.jpeg")
        imag = Image.open("filtered_image.jpeg")
        imag = imag.resize((512, 512))
        imag.save("filtered_image_resized.jpeg")
        imag = QPixmap("filtered_image_resized.jpeg")
        self.image_HW5_three.setPixmap(imag)


#HW6
    def laplacian16(self):
        image = cv.imread(self.path6.text(),0)
        image = hw6Lib.sp_noise_pep(image,float(0.1))
        cv.imwrite("new.png", image)
        self.imageUpdate6()        

    def sobel16(self):
        image = cv.imread(self.path6.text(),0)
        image = hw6Lib.sp_noise_salt(image,float(0.1))
        cv.imwrite("new.png", image)
        self.imageUpdate6()

    def sobelMask16(self):
        image = cv.imread(self.path6.text(),0)
        image = hw6Lib.sp_noise_sandp(image,float(0.1))
        cv.imwrite("new.png", image)
        self.imageUpdate6()

    def sharpened6(self):
        image = cv.imread(self.path6.text(),0)
        image = hw6Lib.gaus(image)
        cv.imwrite("new.png", image)
        self.imageUpdate6()

    def partF16(self):
        image = cv.imread(self.path6.text(),0)
        R = noises.add_periodic(image)
        image = np.clip(R, 0, 255).astype(np.uint8)
        cv.imwrite("new.png", image)
        self.imageUpdate6()

    def imageUpdate6(self):
        self.processedImage6.setPixmap(QPixmap("new.png"))
        self.processedImage6.setScaledContents(True)
        self.processedImage6.setAlignment(QtCore.Qt.AlignCenter)    

    def max6(self):
        image = cv.imread("new.png")
        image = hw6Lib.max_filter(image,int(self.row6.text()),int(self.column6.text()))
        cv.imwrite("new.png", image)
        self.imageUpdate6()

    def min6(self):
        image = cv.imread("new.png")
        image = hw6Lib.min_filter(image,int(self.row6.text()),int(self.column6.text()))
        cv.imwrite("new.png", image)
        self.imageUpdate6()
 
    def medianFilter6(self):
        image = cv.imread("new.png")
        image = hw6Lib.median_filter(image,int(self.row6.text()),int(self.column6.text()))
        cv.imwrite("new.png", image)
        self.imageUpdate6()
   
    def mean6(self):
        image = cv.imread("new.png")
        image = hw6Lib.average_filter(image,int(self.row6.text()),int(self.column6.text()))
        cv.imwrite("new.png", image)
        self.imageUpdate6()
    
    def partG16(self):
        image = cv.imread(self.path6.text(),0)
        image = hw6Lib.g_filter(image)
        cv.imwrite("new.png", image)
        self.imageUpdate6()
   
    def power6(self):        
        image = cv.imread(self.path6.text(),0)
        image = hw6Lib.power_low_filter(image)
        cv.imwrite("new.png", image)
        self.imageUpdate6()
   
    def harmonicFilter(self):
        a1 = int(self.row6.text())
        a2 = int(self.column6.text())
        image = cv.imread(self.path6.text(),0)
        [a, b] = image.shape
        array = np.zeros(shape=(a + a1 - 1, b + a2 - 1))

        for i in range(a):
            for j in range(b):
                x = image[i, j]
                array[i + a1 - 2, j + a2 - 2] = x

        filter_harmonic = np.ones([a1, a2])
        filter_harmonic = np.double(filter_harmonic)
        array = np.double(array)
        output_harmonic = np.zeros([a, b])

        for i in range(a - (a1 - 1)):
            for j in range(b - (a2 - 1)):
                temp_harmonic = array[i:i + a1, j:j + a2]
                non_zero_values = temp_harmonic[temp_harmonic != 0]

                if len(non_zero_values) > 0:
                    output_harmonic[i, j] = (a1 * a2) / np.sum(1 / non_zero_values)
                else:
                    output_harmonic[i, j] = 0

        img_harmonic = np.uint8(output_harmonic)    
        cv.imwrite("new.png", img_harmonic)
        self.imageUpdate6()
   
    def geometricFilter(self): 
        a1 = int(self.row6.text())
        a2 = int(self.column6.text())
        image = cv.imread(self.path6.text(),0)
        [a, b] = image.shape
        array = np.zeros(shape=(a + a1 - 1, b + a2 - 1))

        for i in range(a):
            for j in range(b):
                x = image[i, j]
                array[i + a1 - 2, j + a2 - 2] = x

        filter_geometric = np.ones([a1, a2])
        filter_geometric = np.double(filter_geometric)
        array = np.double(array)
        output_geometric = np.zeros([a, b])

        for i in range(a - (a1 - 1)):
            for j in range(b - (a2 - 1)):
                temp_geometric = np.log(array[i:i + a1, j:j + a2])
                output_geometric[i, j] = np.exp(np.mean(temp_geometric))

        img_geometric = np.uint8(output_geometric)
        cv.imwrite("new.png", img_geometric)
        self.imageUpdate6()

    def fileClicker6(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
            image = cv.imread(self.fname[0])
            self.path6.setText(self.fname[0])
            print(image)
            row_image, col_image = image.shape[:2]
            self.c = image
            new = self.fname[0]
            if self.row6.text() or self.row6.text() != "":
                new = self.change_block_size6()
            if self.fname[0]:
                self.mainImage6.setPixmap(QPixmap(self.fname[0]))
                self.mainImage6.setScaledContents(True)
                self.mainImage6.setAlignment(QtCore.Qt.AlignCenter)

            return self.fname[0]
        except:
            print("error")

    def change_block_size6(self):
        try:
            if self.grayscale6.isChecked():
                image = cv.imread(self.path6.text())
                img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                block_dim_tuple = (int(float(self.row6.text())), int(float(self.column6.text())))
                row_image, column_image = img.shape[:2]
                if row_image % block_dim_tuple[0] == 0:
                    if column_image % block_dim_tuple[1] == 0:

                        for i in range(0, row_image, block_dim_tuple[0]):
                            for j in range(0, column_image, block_dim_tuple[1]):
                                img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()
                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):

                            for j in range(0, column_image, block_dim_tuple[1]):
                                if j + block_dim_tuple[1] > column_image:
                                    img[i:i + block_dim_tuple[0], j:column_image] = img[i:i + block_dim_tuple[0],j:column_image].mean()
                                else:
                                    img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()

                if row_image % block_dim_tuple[0] != 0:
                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        img[i:row_image, j:column_image] = img[i:row_image,j:column_image].mean()

                                    else:
                                        img[i:row_image, j:j + block_dim_tuple[1]] = img[i:row_image,j:j + block_dim_tuple[1]].mean()
                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        img[i:i + block_dim_tuple[0], j:column_image] = img[i:i + block_dim_tuple[0],j:column_image].mean()
                                    else:
                                        img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()

                    else:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    img[i:row_image, j:j + block_dim_tuple[1]] = img[i:row_image,j:j + block_dim_tuple[1]].mean()
                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = img[i:i + block_dim_tuple[0],j:j + block_dim_tuple[1]].mean()

                cv.imwrite("new.png", img)
                print(img)
                self.processedImage6.setPixmap(QPixmap("new.png"))
                self.processedImage6.setScaledContents(True)
                self.processedImage6.setAlignment(QtCore.Qt.AlignCenter)

                return img
            else:
                img = cv.imread(self.path6.text())

                block_dim_tuple = (int(float(self.row6.text())), int(float(self.column6.text())))

                row_image, column_image = img.shape[:2]
                if row_image % block_dim_tuple[0] == 0:
                    if column_image % block_dim_tuple[1] == 0:

                        for i in range(0, row_image, block_dim_tuple[0]):
                            for j in range(0, column_image, block_dim_tuple[1]):
                                for k in  range(0,3):
                                    img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()
                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):

                            for j in range(0, column_image, block_dim_tuple[1]):
                                if j + block_dim_tuple[1] > column_image:
                                    for k in range(0, 3):
                                        img[i:i + block_dim_tuple[0], j:column_image, k] = img[i:i + block_dim_tuple[0], j:column_image, k].mean()

                                else:
                                    for k in range(0, 3):
                                        img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()
                if row_image % block_dim_tuple[0] != 0:
                    if column_image % block_dim_tuple[1] != 0:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        for k in range(0, 3):
                                            img[i:row_image, j:column_image, k] = img[i:row_image, j:column_image, k].mean()
                                    else:
                                        for k in range(0, 3):
                                            img[i:row_image, j:j + block_dim_tuple[1], k] = img[i:row_image, j:j + block_dim_tuple[1], k].mean()
                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    if j + block_dim_tuple[1] > column_image:
                                        for k in range(0, 3):
                                            img[i:i + block_dim_tuple[0], j:column_image, k] = img[i:i + block_dim_tuple[0], j:column_image, k].mean()
                                    else:
                                        for k in range(0, 3):
                                            img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()
                    else:
                        for i in range(0, row_image, block_dim_tuple[0]):
                            if i + block_dim_tuple[0] > row_image:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    for k in range(0, 3):
                                        img[i:row_image, j:j + block_dim_tuple[1], k] = img[i:row_image, j:j + block_dim_tuple[1], k].mean()
                            else:
                                for j in range(0, column_image, block_dim_tuple[1]):
                                    for k in range(0, 3):
                                        img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k] = img[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1], k].mean()
                cv.imwrite("new.png", img)
                print(img)
                self.processedImage6.setPixmap(QPixmap("new.png"))
                self.processedImage6.setScaledContents(True)
                self.processedImage6.setAlignment(QtCore.Qt.AlignCenter)
        except:
            print("error")

#HW7
    def loadImage(self):  
        self.findimage = QFileDialog.getOpenFileName(self,"Select Image file to import",""," (*.jpg *.jpeg *.png *.tif *.bmp)")[0] #select open image
        self.openimage = cv.imread(self.findimage,0)#image to array
        self.images = Image.fromarray(self.openimage)
        self.images.save("newsizeimage.jpeg")
        self.newsizeimage = Image.open("newsizeimage.jpeg")
        self.newsizeimage = self.newsizeimage.resize((512, 512))
        self.newsizeimage.save("newsizeimage.jpeg")
        self.newsizeimage = QPixmap("newsizeimage.jpeg")
        self.mainImage7.setPixmap(self.newsizeimage)

    def image71func(self):        
        original = io.imread('C:/Users/murat/OneDrive/Resimler/original.png')
        original = img_as_float(original)

        # Convert the image to grayscale
        img_gray = None  # Initialize img_gray

        if len(self.openimage.shape) == 2:
            # Already a grayscale image, no need to convert
            img_gray = img_as_float(self.openimage)
        elif len(self.openimage.shape) == 3 and self.openimage.shape[2] == 3:
            # Convert color image to grayscale
            img_gray = cv.cvtColor(self.openimage, cv.COLOR_BGR2GRAY)
            img_gray = img_as_float(img_gray)
        else:
            print("Unsupported image format. Check the number of channels.")

        # Compute and plot the Fourier transform of the original image
        crispfft = np.fft.fft2(original)

        plt.figure(figsize=(15, 10))
        plt.suptitle('Inverse Filter (Wiener) Process')
        plt.subplot(2, 3, 1)
        plt.imshow(original, cmap='gray')
        plt.title('Original Image')
        plt.subplot(2, 3, 3)
        plt.imshow(img_gray, cmap='gray')
        plt.title('Motion Blurred Image')

        plt.subplot(2, 3, 2)
        plt.imshow(np.log(1 + np.abs(np.fft.fftshift(crispfft))), cmap='gray')
        plt.title('Fourier Transform (Original)')

        # Compute and plot the Fourier transform of the input image
        blurredfft = np.fft.fft2(img_gray)
        plt.subplot(2, 3, 4)
        plt.imshow(np.log(1 + np.abs(np.fft.fftshift(blurredfft))), cmap='gray')
        plt.title('Fourier Transform (Input)')

        # Compute the PSF and deconvolve
        PSFfft = blurredfft / crispfft
        PSF = np.fft.ifftshift(np.fft.ifft2(PSFfft))
        image2 = restoration.wiener(img_gray, PSF, balance=1)

        # Plot the deconvolution result
        plt.subplot(2, 3, 6)
        plt.imshow((1 + np.abs(image2)), cmap='gray')
        plt.title('Inverse Filter (Wiener) Result')

        # Plot the Fourier transform of the PSF
        plt.subplot(2, 3, 5)
        plt.imshow(np.log(1 + np.abs(np.fft.fftshift(PSFfft))), cmap='gray')
        plt.title('Point Spread Function')

        # Show the plots
        plt.show()

    def image72func(self):                
        original = io.imread('original.png')
        original = img_as_float(original)

        # Convert the image to grayscale
        img_gray = None  # Initialize img_gray

        if len(self.openimage.shape) == 2:
            # Already a grayscale image, no need to convert
            img_gray = img_as_float(self.openimage)
        elif len(self.openimage.shape) == 3 and self.openimage.shape[2] == 3:
            # Convert color image to grayscale
            img_gray = cv.cvtColor(self.openimage, cv.COLOR_BGR2GRAY)
            img_gray = img_as_float(img_gray)
        else:
            print("Unsupported image format. Check the number of channels.")

        # Compute and plot the Fourier transform of the original image
        crispfft = np.fft.fft2(original)        

        # Compute and plot the Fourier transform of the input image
        blurredfft = np.fft.fft2(img_gray)

        # Compute the PSF and deconvolve
        PSFfft = blurredfft / crispfft
        PSF = np.fft.ifftshift(np.fft.ifft2(PSFfft))
        image2 = restoration.wiener(img_gray, PSF, balance=1)

        # Plot the deconvolution result
        plt.imshow((1 + np.abs(image2)), cmap='gray')
        plt.axis('off')
        plt.savefig("filtered_image.png", bbox_inches='tight', pad_inches=0.0)
        self.newsizeimage = Image.open("filtered_image.png")
        self.newsizeimage = self.newsizeimage.resize((512, 512))
        self.newsizeimage.save("filtered_image.png")
        self.newsizeimage = QPixmap("filtered_image.png")
        self.newImage7.setPixmap(self.newsizeimage)


    #HW8
    def load_image(self):
        self.image2 = fromqpixmap(self.filter_img_label.pixmap())
        self.image2.save('images.png')
        pixmap = QPixmap('images.png')
        self.orgin_img_label.setPixmap(QPixmap(pixmap))
        self.image = cv.imread('images.png')

    def load_image(self):
        filename = QFileDialog.getOpenFileName(self,'Open File',os.getcwd())
        self.imagePath = filename[0]
        self.image = cv.imread(self.imagePath)
        pixmap = QPixmap(self.imagePath)
        self.orgin_img_label.setPixmap(QPixmap(pixmap))
        self.original_img = self.imagePath


    def DilationFunction(self,image,kernel):
        row, col = image.shape
        dilationimage = image.copy()
        row_kernel, col_kernel = kernel.shape
        mid_row = int((row_kernel - 1) / 2)
        mid_col = int((col_kernel - 1) / 2)
        for i in range(row - row_kernel):
            for j in range(col - col_kernel):
                dilationimage[mid_row + i, mid_col + j] = np.amax(image[i:i + row_kernel, j:j + col_kernel])

        return dilationimage

    def dilation(self):
        image = self.image
        image = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
        kernel = np.ones([self.kernelsize, self.kernelsize])
        dilationimage = self.DilationFunction(image,kernel)
        self.saved_img = 'dilationImage.jpg'
        cv.imwrite(self.saved_img, dilationimage)
        self.main_window.filtered_label.setText("Dilation Operation")
        pixmap = QPixmap(self.saved_img)
        self.filter_img_label.setPixmap(QPixmap(self.saved_img))

    def ErosionFunction(self,image,kernel):
        row, col = image.shape
        erosion_image = image.copy()
        row_kernel, col_kernel = kernel.shape
        mid_row = int((row_kernel - 1) / 2)
        mid_col = int((col_kernel - 1) / 2)

        for i in range(row - row_kernel):
            for j in range(col - col_kernel):
                erosion_image[mid_row + i, mid_col + j] = np.amin(image[i:i + row_kernel, j:j + col_kernel])
        return erosion_image

    def erosion(self):
        image = self.image
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        kernel = np.ones([self.kernelsize, self.kernelsize])
        erosion_image = self.ErosionFunction(image,kernel)
        self.saved_img = 'erosionImage.jpg'
        cv.imwrite(self.saved_img, erosion_image)
        self.main_window.filtered_label.setText("Erosion Operation")
        pixmap = QPixmap(self.saved_img)
        self.filter_img_label.setPixmap(QPixmap(self.saved_img))

    def opening(self):
        image = self.image
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        kernel = np.ones([self.kernelsize, self.kernelsize])
        erosion_image = self.ErosionFunction(image, kernel)
        opening_image = self.DilationFunction(erosion_image,kernel)
        opening_image = cv.morphologyEx(self.image, cv.MORPH_OPEN, kernel)
        self.saved_img = 'OpeningImage.jpg'
        cv.imwrite(self.saved_img, opening_image)
        self.main_window.filtered_label.setText("Opening Operation")
        pixmap = QPixmap(self.saved_img)
        self.filter_img_label.setPixmap(QPixmap(self.saved_img))

    def closingofopening(self):
        image = self.image
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        kernel = np.ones([self.kernelsize, self.kernelsize])
        erosion_image = self.ErosionFunction(image, kernel)
        opening_image = self.DilationFunction(erosion_image, kernel)
        x = self.DilationFunction(opening_image,kernel)
        closingofopening = self.ErosionFunction(x,kernel)
        self.saved_img = 'ClosingOfOpeningImage.jpg'
        cv.imwrite(self.saved_img, closingofopening)
        self.main_window.filtered_label.setText("Closing of Opening")
        pixmap = QPixmap(self.saved_img)
        self.filter_img_label.setPixmap(QPixmap(self.saved_img))

    def closing(self):
        image = self.image
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        kernel = np.ones([self.kernelsize, self.kernelsize])
        dilationimage = self.DilationFunction(image, kernel)
        closing_image = self.ErosionFunction(dilationimage,kernel)
        closing_image = cv.morphologyEx(self.image, cv.MORPH_CLOSE, kernel)
        self.saved_img = 'ClosingImage.jpg'
        cv.imwrite(self.saved_img, closing_image)
        self.main_window.filtered_label.setText("Closing Operation")
        pixmap = QPixmap(self.saved_img)
        self.filter_img_label.setPixmap(QPixmap(self.saved_img))

    def gradient(self):
        image = self.image
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        kernel = np.ones([self.kernelsize, self.kernelsize])
        dilationimage = self.DilationFunction(image, kernel)
        erosion_image = self.ErosionFunction(image, kernel)
        gradient_image = dilationimage - erosion_image
        self.saved_img = 'GradientImage.jpg'
        cv.imwrite(self.saved_img, gradient_image)
        self.main_window.filtered_label.setText("Morphological Gradient Operation")
        pixmap = QPixmap(self.saved_img)
        self.filter_img_label.setPixmap(QPixmap(self.saved_img))

    def _slider_th_changed(self):
        self.main_window.th_label.setText(str(self.main_window.th_value_slider.value() / 10))
        self.th_value = self.main_window.th_value_slider.value()

    def kernel_size_changed(self):
        self.main_window.kernel_label.setText(str(self.main_window.kernel_slider.value()))
        self.kernelsize = self.main_window.kernel_slider.value()

    def thresholding(self):
        image = self.image
        rows, cols, channel = image.shape
        self.th_value = self.th_value / 10
        for k in range(0, 3):
            for i in range(0, rows):
                for j in range(0, cols):
                    if image[i, j, k] >= self.th_value * 255:
                        image[i, j, k] = 255

                    if image[i, j, k] < self.th_value * 255:
                        image[i, j, k] = 0

        self.saved_img = 'thresholdingImage.jpg'
        cv.imwrite(self.saved_img, image)
        self.main_window.filtered_label.setText("Thresholding")
        pixmap = QPixmap(self.saved_img)
        self.filter_img_label.setPixmap(QPixmap(self.saved_img))

    def T_hat_transformation(self):
        image = self.image
        image_gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        kernel = np.ones((self.kernelsize, self.kernelsize), np.uint8)

        # Opening operasyonunu OpenCV fonksiyonuyla gerçekleştir
        opening_image = cv.morphologyEx(image_gray, cv.MORPH_OPEN, kernel)

        # T-hat dönüşümü
        transformation_image = cv.subtract(image_gray, opening_image)

        self.saved_img = 'ThatTransformationImage.jpg'
        cv.imwrite(self.saved_img, transformation_image)
        self.main_window.filtered_label.setText("T hat Transformation")
        pixmap = QPixmap(self.saved_img)
        self.filter_img_label.setPixmap(QPixmap(self.saved_img))

    def B_hat_transformation(self):
        image = self.image

        # Disk çekirdekli kapanma (Kernel Size = 30)
        kernel30 = np.ones((30, 30), np.uint8)

        disk_kernel_closing = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel30)

        # Disk çekirdekli açılma (Kernel Size = 100)
        kernel100 = np.ones((100, 100), np.uint8)
        disk_kernel_opening = cv.morphologyEx(disk_kernel_closing, cv.MORPH_OPEN, kernel100)

        # Kare çekirdekli gradyan (Kernel Size = 3)
        kernel3 = np.ones((3, 3), np.uint8)
        square_kernel_gradient = cv.morphologyEx(disk_kernel_opening, cv.MORPH_GRADIENT, kernel3)

        # Sonucu kaydet
        self.saved_img = 'BhatTransformationImage.jpg'
        cv.imwrite(self.saved_img, square_kernel_gradient)
        self.main_window.filtered_label.setText("B hat Transformation")
        pixmap = QPixmap(self.saved_img)
        self.filter_img_label.setPixmap(QPixmap(self.saved_img))

    def Thresholded_T_hat_transformation(self):
        image = self.image
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        kernel = np.ones([self.kernelsize, self.kernelsize])
        erosion_image = self.ErosionFunction(image, kernel)
        opening_image = self.DilationFunction(erosion_image, kernel)
        transformationimage = image - opening_image
        image = transformationimage
        row, col = image.shape
        self.th_value = self.th_value / 10

        for i in range(0, row):
            for j in range(0, col):
                if image[i, j] >= self.th_value * 255:
                    image[i, j] = 255

                if image[i, j] < self.th_value * 255:
                    image[i, j] = 0

        self.saved_img = 'BhatTransformationImage.jpg'
        cv.imwrite(self.saved_img, image)
        self.main_window.filtered_label.setText("Thresholded T hat Transformation")
        pixmap = QPixmap(self.saved_img)
        self.filter_img_label.setPixmap(QPixmap(self.saved_img))

    def get_region(self,x, y, shape):
        out = []
        maxx = shape[1] - 1
        maxy = shape[0] - 1

        out.append((min(max(x - 1, 0), maxx), min(max(y - 1, 0), maxy)))
        out.append((x, min(max(y - 1, 0), maxy)))
        out.append((min(max(x + 1, 0), maxx), min(max(y - 1, 0), maxy)))
        out.append((min(max(x - 1, 0), maxx), y))
        out.append((min(max(x + 1, 0), maxx), y))
        out.append((min(max(x - 1, 0), maxx), min(max(y + 1, 0), maxy)))
        out.append((x, min(max(y + 1, 0), maxy)))
        out.append((min(max(x + 1, 0), maxx), min(max(y + 1, 0), maxy)))

        return out

    def region_growing_function(self,image,seed):
        list = []
        region_growing_image = np.zeros_like(image)
        list.append((seed[0], seed[1]))

        region = []
        count = 0
        while(len(list) > 0):
            pix = list[0]
            region_growing_image[pix[0], pix[1]] = 255
            for i in self.get_region(pix[0], pix[1], image.shape):
                if image[i[0], i[1]] != 0:
                    region_growing_image[i[0], i[1]] = 255
                    if not i in region:
                        list.append(i)
                    region.append(i)
                    count +=1
            list.pop(0)
        return region_growing_image,count


    


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    UIWindow = Ui()
    app.exec_()
