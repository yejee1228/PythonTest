import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np


class Service:
    def __init__(self):
        pass

    def create_model(self):
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) \
            = fashion_mnist.load_data()
        train_images = train_images / 255.0
        test_images = test_images / 255.0
        plt.figure()
        plt.imshow(train_images[15])
        plt.colorbar()
        plt.grid(False)
        plt.show()
        """
        for i in range(25):
            plt.subplots(5,5,i+1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(train_images[i], cmap=plt.cm.binary)
            plt.xlabel(self.class_names[train_labels[i]])
        plt.show()
        """


