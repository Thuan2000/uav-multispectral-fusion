from utils.label import LabelToolParser


import cv2
import configurations

if __name__ == "__main__":

    toolParser = LabelToolParser()
    toolParser.generate_masks()
