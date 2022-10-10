import os

import zipfile


def ziper():
    name = "resources"
    TO_ZIP = 'resources'

    if os.path.exists(os.path.join(os.getcwd(), f"resources/{name}.zip")):
        os.remove(os.path.join(os.getcwd(), f"resources/{name}.zip"))

    with zipfile.ZipFile(f'{name}.zip', 'w') as zip_file:
        for root, dirs, files in os.walk(TO_ZIP):
            for file in files:
                zip_file.write(filename=os.path.join(root, file), arcname=file)

    os.rename(os.path.join(os.getcwd(), f"{name}.zip"), os.path.join(os.getcwd(), f"resources/{name}.zip"))

ziper()