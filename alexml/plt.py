import numpy as np
import matplotlib.pyplot as plt


def show_imgs(imgs, columns=1):
    """
    Plots a list of images side by side
    :param imgs: the list of images to plot
    :param columns: the number of columns to use on a line
    """
    fig = plt.figure()
    for n, img in enumerate(imgs):
        fig.add_subplot(columns, np.ceil(len(imgs) / float(columns)), n + 1)
        plt.imshow(img)
    fig.set_size_inches(np.array(fig.get_size_inches()) * len(imgs))
    plt.show
