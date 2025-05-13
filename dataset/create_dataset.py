from datetime import date
import os
from river_data_collector.river_downloader import imgw
# install the package using:
# pip install -e git+https://github.com/FlowPredictorApp/RiverDataCollector.git#egg=river_data_collector

import json

output_folder = "data/"
os.makedirs(output_folder, exist_ok=True)

downloader = imgw.ImgwDownloader()
river_name = imgw.PolishRiversNames.BIALKA.value
station_name = imgw.StationsNames.TRYBSZ2.value
since_date = date(2023, 1, 1)
till_date = date(2023, 1, 1)

data = downloader.get_river_data(river_name, station_name, since_date, till_date, False)
if data:
    for measurement_name, collection in data.items():
        with open(f"{output_folder}{measurement_name}.json", "w") as file:
            json.dump([measurement.__dict__ for measurement in collection.measurements], file, default=str)
    print(f"Data saved to {measurement_name}.json")
else:
    print("No data collected.")

