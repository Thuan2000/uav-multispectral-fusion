from utils.mask_generator import MaskGenerator


import cv2
import configurations

if __name__ == "__main__":

    maskGen = MaskGenerator()
    maskGen.generate_masks()
