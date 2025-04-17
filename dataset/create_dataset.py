import os
import io
import requests
from bs4 import BeautifulSoup
import zipfile

# Base URL of the data source
base_url = 'https://danepubliczne.imgw.pl/pl/datastore/getfiledown/Arch/Telemetria/Hydro/' #2023/Hydro_2023-02.zip
# Output folder to save downloaded files
output_folder = "data"
os.makedirs(output_folder, exist_ok=True)

years_to_download = [2025]

def download_and_extract_file(url, output_path):
    """Download a file from a given URL and save it to the specified path."""
    response = requests.get(base_url)
    if response.status_code == 200:
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall(output_path)
        print(f"Downloaded and extracted: {output_path}")
    else:
        print(f"Failed to download: {url} (Status: {response.status_code})")

def unpack_zip(file_path, extract_to):
            """Unpack a zip file to the specified directory."""
            try:
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_to)
                print(f"Unpacked: {file_path}")
            except zipfile.BadZipFile:
                print(f"Failed to unpack: {file_path} (Bad zip file)")

for year in years_to_download:
    for month in range(1, 5):
        file_name = f"Hydro_{year}-{month:02d}.zip"
        file_path = os.path.join(output_folder, file_name) 
        url = f"{base_url}{year}/{file_name}"
        download_and_extract_file(url, file_path)
