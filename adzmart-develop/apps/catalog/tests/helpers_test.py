import os
import random

SUFFIX = random.randint(10000, 99999)

RESOURCES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "test", "resources")
TEST_IMAGE = os.path.join(RESOURCES_PATH, "logo.png")
TEST_TAG = "adzmart_cloudinary_test"
UNIQUE_TAG = "{0}_{1}".format(TEST_TAG, SUFFIX)
UNIQUE_TEST_ID = UNIQUE_TAG

TEST_IMAGE_W = 240
TEST_IMAGE_H = 50
