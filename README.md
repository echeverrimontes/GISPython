# GISPython
We open our grib2 file with the ReadExcel component from TTToolbox.
There are 3 columns per WorkSheet, the xlsx file is created from a Python 2.7 
script that opens the grib2 file and saves
the values stored according to their coordinates (MultipleInputs.py).
![docsone](https://user-images.githubusercontent.com/21000020/47823284-8fc72b80-dd35-11e8-93c5-5b6b6cf7c807.JPG)
We reproject our points into three
different famous projections:
WebMercator, Cassini and
Spherical.
For some unknown reason the
WebMercator projection gives nulls for 
some coordinates, it might have to do 
with the undefined character of the
natural logarithm function for values
smaller than zero.
The Mercator projection gives good 
results for values bigger than 
-85 degrees and smaller than 
85 degrees of longitude. Latitude on the
other hand is not a problem.
![docstwo](https://user-images.githubusercontent.com/21000020/47823281-8fc72b80-dd35-11e8-8500-e6c6e40ef32d.JPG)
![docsthree](https://user-images.githubusercontent.com/21000020/47823280-8fc72b80-dd35-11e8-9dd6-1973d7c5bec9.JPG)
![docsfour](https://user-images.githubusercontent.com/21000020/47823283-8fc72b80-dd35-11e8-8d11-91cd00f51b58.JPG)
![docsfive](https://user-images.githubusercontent.com/21000020/47823282-8fc72b80-dd35-11e8-9f58-8869d03876b5.JPG)

