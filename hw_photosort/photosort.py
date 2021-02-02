import os
import PIL
from PIL import Image
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", help="input directory")
parser.add_argument("output_dir", help="output directory")
parser.add_argument("-m", "--map", help="generate html", action="store_true")
parser.add_argument("-x", "--delete", help="delete photos", action="store_true")
parser.add_argument("-r", "--recursively", help="process directories recursively", action="store_true")
args = parser.parse_args()

directory = args.input_dir
output_directory = args.output_dir
photos = []
delete_image = args.delete
generate_html = args.map
recursively = args.recursively

class Photo:
    def __init__ (self, path, name, date, year, latitude, longitude):
        self.path = path
        self.name = name
        self.date = date
        self.year = year
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}".format(self.path, self.name, self.date, self.year, self.latitude, self.longitude)


def open_directory(directory):
    print("directory: {0}".format(directory))
    list_of_photos = os.listdir(directory)   
    for photo in list_of_photos:
        path = os.path.join(directory, photo)
        if os.path.isdir(path):
            if(recursively):
                open_directory(path)
            else:
                print("ignore: {0}".format(path))
        else:
            if os.path.splitext(path)[1] == ".jpg":
                photos.append(exif_data(path))
            else:
                print("ignore: {0}".format(path))
    
def exif_tag_value(exif,tag) :
  for (k,v) in exif.items():
     if k == tag:
        return v

def exif_data(photo):    
    exif = Image.open(photo).getexif()
    name = os.path.splitext(os.path.split(photo)[1])[0]
    date = "unknown"
    year = "unknown"
    latitude = "unknown"
    longitude = "unknown"
    if exif is not None:
        date_exif = exif_tag_value(exif, 0x9003)
        gps = exif_tag_value(exif, 0x8825)
        if date_exif is not None:
            year = date_exif[0:4:]
            date = "{0}-{1}-{2}".format(date_exif[0:4:], date_exif[5:7:], date_exif[8:10:])
        if gps is not None:
            (x, y, z) = gps[0x0002]
            latitude = float(x + y/60 + z/3600)
            (x, y, z) = gps[0x0004]
            longitude = float(x + y/60 + z/3600)
            #latitude = gps[0x0002]
            #longitude = gps[0x0004]
    return Photo(photo, name, date, year, latitude, longitude)

def copy_photos(photos, output_directory):
    counters = dict()
    for photo in photos:
        new_directory = os.path.join(output_directory, photo.year)
        if not os.path.isdir(new_directory):
            os.makedirs(new_directory)
        counter = counters.get(photo.date,1)
        counters[photo.date] = counter + 1
        if photo.date == "unknown":
            new_file_name = os.path.join(new_directory, "{0:03d}.jpg".format(counter))
        else:
            new_file_name = os.path.join(new_directory, "{0}-{1:03d}.jpg".format(photo.date, counter))

        shutil.copy(photo.path, new_file_name)

def delete_photos(photos):
    for photo in photos:
        os.remove(photo.path)

def create_html(photos, file_name):
    result = """ 
    <!DOCTYPE html>
<html>
<head>
	
	<title>Mapa</title>

	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<link rel="shortcut icon" type="image/x-icon" href="docs/images/favicon.ico" />

    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
	
</head>
<body>



<div id="mapid" style="width: 800px; height: 800px;"></div>
<script>

	var mymap = L.map('mapid').setView([49.894634, 14.677734], 10);

	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(mymap);
    """
    for photo in photos:
        if photo.latitude != "unknown" and photo.longitude != "unknown":
            result += "L.marker([{0}, {1}]).addTo(mymap).bindPopup(\"{2}\");\n".format(photo.latitude, photo.longitude, photo.name)
    result += """
    </script>



</body>
</html>
    """
    html_file = open(file_name, "w")
    html_file.write(result)
    html_file.close()


open_directory(directory)
if generate_html:
    create_html(photos, "photos.html")
copy_photos(photos, output_directory)
if delete_image:
    delete_photos(photos)
