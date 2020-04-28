from PIL import Image, ImageChops
from uuid import uuid4

from skimage.metrics import structural_similarity
from skimage.transform import resize
import cv2 as cv


def get_images_difference(image1, image2):
    """ This function compares two images and creates the
        new image with the information about the differences
        between two source images.
    """

    img1 = Image.open(image1)
    img2 = Image.open(image2)

    # Get difference of two images:
    diff = ImageChops.difference(img1, img2)

    # Add white background:
    background = Image.new('RGB', img1.size, color=(255, 255, 255))
    diff = ImageChops.difference(background, diff.convert('RGB'))

    # Save to separate file:
    file_name = 'compare_{0}.png'.format(uuid4())
    diff.save(file_name)

    return file_name


def compare_images(image1, image2):
    """ This function measures the index of similarity
        of two images.
    """

    # Get two images - resize both to 1024 x 1024
    img_a = resize(cv.imread(image1), (2 ** 10, 2 ** 10))
    img_b = resize(cv.imread(image2), (2 ** 10, 2 ** 10))

    # If score == 1 it means that images are equal
    score, diff = structural_similarity(img_a, img_b,
                                        full=True, multichannel=True)
    return score


get_images_difference('new_screenshot.png', 'base.png')

score = compare_images('new_screenshot.png', 'base.png')
print('Score with bug: ', score)

score = compare_images('random_screenshot.png', 'base.png')
print('Score of random images: ', score)
