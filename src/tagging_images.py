import os
from pathlib import Path
import cv2 as cv
from img_transform import image_transformation


def tag_w_user(file: Path):

    # snippets = Path("src", "files", "snippets")
    # files = os.listdir(snippets)
    # file_paths = [snippets.joinpath(file) for file in files]
    img = cv.imread(str(file))

    cv.imshow("snippet", img)
    cv.waitKey(0)

    value = int(input("Escolha um threshold: "))
    transformed = image_transformation(image=img, thresh_param=value)

    cv.imshow("transformed", transformed)
    cv.waitKey(0)


if __name__ == "__main__":
    file = Path("src", "files", "snippets", "pic_6.png")
    tag_w_user(file)
