import json
import os
from pathlib import Path, PosixPath
from typing import List
from urllib import request

from cv2 import initUndistortRectifyMap
from numpy import isin
import requests


file_path_bug_bash_2 = Path("src", "files", "bug_bash_2_reference")
file_path_bug_bash = Path("src", "files", "bug_bash_reference")
sample_1 = Path("src", "files", "sample_1")


def get_json(path: PosixPath):
    files = os.listdir(path)
    return files


def transform_to_dict(files: list, path: PosixPath):
    full_paths = [path.joinpath(file) for file in files]

    loading_jsons = []
    for file in full_paths:
        with open(file, "r") as j:
            loading_jsons.append(json.loads(j.read()))

    return loading_jsons


def get_snippets(dict_objs: List[dict]):

    student_list = [
        dict_obj.get("process_assets").get("student_list") for dict_obj in dict_objs
    ]

    assets = [asset.get("assets") for item in student_list for asset in item]
    snippets = [
        snippet.get("snippets")
        for item in assets
        for snippet in item
        if isinstance(snippet, dict)
    ]

    snippets_urls = []
    for item in snippets:
        if isinstance(item, list):
            for value in item:
                if isinstance(value, dict):
                    url = value.get("value")
                    snippets_urls.append(url)

    return snippets_urls


def download_images(urls):
    destination_path = Path("src", "files", "snippets")

    for i, url in enumerate(urls):
        name = f"pic_{str(i)}.png"
        dest_path_file = destination_path.joinpath(name)

        with open(dest_path_file, "wb") as d:
            response = requests.get(url, stream=True).content
            d.write(response)


def main():
    all_snippets = []
    paths = [file_path_bug_bash_2, file_path_bug_bash_2, sample_1]
    for path in paths:
        files = get_json(path)
        reading_objects = transform_to_dict(files, path)
        snippets_url = get_snippets(reading_objects)
        all_snippets.extend(snippets_url)

    download_images(all_snippets)


if __name__ == "__main__":
    main()
