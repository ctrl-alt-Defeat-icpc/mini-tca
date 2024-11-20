import os, zipfile

here = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(here)
for file in files:
    if file.endswith('.zip'):
        name = os.path.splitext(file)[0].replace('samples-', '').lower()
        target_folder = os.path.join(here, name)
        file_address = os.path.join(here, file)
        os.makedirs(target_folder, exist_ok=True)
        with zipfile.ZipFile(file_address, 'r') as zip_ref:
            zip_ref.extractall(target_folder)
        os.remove(file_address)