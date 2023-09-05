import os
from random import shuffle
import requests

def synchronize():
    # Set the path to the local directory you want to synchronize
    local_path = os.path.expanduser("~/slideshow/images")

    # Make a GET request to the server to get the list of files and their hashes
    response = requests.get("https://example.de/smartpanel/austausch/utils/get_img_and_hash_list.php")

    if response.status_code == 200:
        # Parse the response and create a dictionary with file names and hashes
        server_files = {}
        for line in response.text.split("\n")[:-1]:
            hash_length = line.find("http")
            server_files[line[0:hash_length]] = line[hash_length:]

        for file_name in os.listdir(local_path):
            if not file_name in server_files:
                os.remove(f"{local_path}/{file_name}")

        local_files = os.listdir(local_path)

        for file_hash in server_files:
            if not file_hash in local_files:
                with open(f"{local_path}/{file_hash}", "wb") as f:
                    f.write(requests.get(server_files[file_hash]).content)
    else:
        print("Failed to get server file list")

def save():
    directory = os.path.expanduser("~/slideshow/images/")
    images = [f'<img src="{directory + image_name}"/>' for image_name in os.listdir(directory)]
    shuffle(images)
    images = "\n            ".join(images)

    with open(os.path.expanduser("~/slideshow/template_slideshow.html"),"r") as f:
        slideshow_html = f.read().replace("<!-- [INSERT IMAGES] -->", images)

    with open(os.path.expanduser("~/slideshow/generated_slideshow.html"), "w") as f:
        f.write(slideshow_html)


if __name__ == "__main__":
    #synchronize()
    save()
