import os

IMG_WIDTH = 4608
IMG_HEIGHT = 3456
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LABEL_JSON_OUTPUT_FOLDER = os.path.join(ROOT_DIR, 'label-tool/images')
MASK_OUTPUT_FOLDER = os.path.join(ROOT_DIR, 'masks')