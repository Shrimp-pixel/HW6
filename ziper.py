import os

import zipfile

name = "resources"
TO_ZIP = 'resources'

with zipfile.ZipFile(f'{name}.zip', 'w') as zip_file:
    for root, dirs, files in os.walk(TO_ZIP):
        for file in files:
            zip_file.write(filename=os.path.join(root, file), arcname=file)


os.rename(os.path.join(os.getcwd(), f"{name}.zip"), os.path.join(os.getcwd(), f"resources/{name}.zip"))
