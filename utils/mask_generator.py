import os
import configurations as cfg
import json
import cv2
import numpy as np
import re


class MaskGenerator:
    def __init__(self):
        pass

    # Returns a list[] of absolute paths of json label output files.
    def get_all_json_files(self):
        json_files = []
        for root, dirs, files in os.walk(cfg.LABEL_JSON_OUTPUT_FOLDER):
            for name in files:
                if name.endswith(".json"):
                    json_files.append(os.path.join(root, name))
                else:
                    continue
        return json_files

    def convert_json_to_contours(self, json_file_dir):
        with open(json_file_dir, "r") as json_file:
                data = json_file.read()
                obj = json.loads(data)

                contours = []
                for region in obj["labels"]:
                    if region.get("vertices") is not None:
                        contour = np.array(
                            [
                                np.array([np.array([i["x"], i["y"]], dtype=np.int32)])
                                for i in region.get("vertices")
                            ]
                        )
                        contours.append(contour)
                return contours

    # Generate the Y label masks from json files
    def generate_masks(self):
        json_files_dirs = self.get_all_json_files()
        for json_file_dir in json_files_dirs:

            contours = self.convert_json_to_contours(json_file_dir)

            # Draw the white contours filled onto black image.
            imgName = re.search(rf'{cfg.LABEL_JSON_OUTPUT_FOLDER}/(.*?)__labels.json',json_file_dir).group(1)
            black = np.zeros((cfg.IMG_WIDTH,cfg.IMG_HEIGHT,1), np.uint8)
            mask = cv2.drawContours(black, contours, -1, (255, 255, 255), -1)
            cv2.imwrite(cfg.MASK_OUTPUT_FOLDER + '/' + imgName + '_mask.jpg', mask)