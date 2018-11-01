# GISPython
# Obtaining the data from the NCEP, link: http://nomads.ncep.noaa.gov/
To get the data from the site we just navigate to the data set we want, for example GDAS, we click on the grib filter link, this sends us to a subdirectory where we can choose the grib2 file (https://en.wikipedia.org/wiki/GRIB) from a period of time, after you clicked on the time period you are interested in, you will find some checkboxes that you can leave unclicked for the whole data or you can cherry pick what you want. After you downloaded the file... for some reason the NCEP gives some wickedly named files in some of the data sets, to check if its wicked or not just look at the ending of the file you just downloaded, if it doesn't end in .grb2, you will have to rename your file with the name you want but making sure that it ends in .grb2 file. 
# Installing the libraries that we will use in our python script
# Windows:
1.) Download python 2.7 from https://www.python.org/download/releases/2.7/ select the MSI installer according to your system 64 or 32 bits.

2.) Press windows key and r, type: cmd, press enter, type: pip -V if it shows you the version of pip installed for example in my case it prints 
"pip 18.1 from c:\...." you can continue to step 4.) otherwise go to 3.)

3.) Go to https://pip.pypa.io/en/stable/installing/ right mouse click on the get-pip.py link and save it in your system. Then windows + r, cmd, enter,
and type python get-pip.py.

4.) Go to: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal and search for the GDAL wheel: GDAL‑2.2.4‑cp27‑cp27m‑win_amd64.whl download it. Once it is in your computer type something like: pip install C:\Users\admin\donwloads\GDAL‑2.2.4‑cp27‑cp27m‑win_amd64.whl (look where the file is located).

5.) Repeat step 4 but this time download the Basemap wheel: basemap‑1.2.0‑cp27‑cp27m‑win_amd64.whl, install through pip as step 4 showed.

6.) Now open the command-line again and type pip install openpyxl 

You should be ready to run the python scripts. 
# Data Manipulation and Viz using Rhinoceros and its famous Grasshopper plugin. 
# The definition is in this repo, its name is: Workshop (1).gh
# **Note: You must have installed the plugins TTToolbox and Tarsier, you can grab them respectively from: 
# https://www.food4rhino.com/app/tt-toolbox
# https://www.food4rhino.com/app/tarsier
We open our grib2 file with the ReadExcel component from TTToolbox.
There are 3 columns per WorkSheet, the xlsx file is created from a Python 2.7 
script that opens the grib2 file and saves
the values stored according to their coordinates (MultipleInputs.py). The data comes from http://nomads.ncep.noaa.gov/
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
Now that we have our geographical
coordinates projected to the cartesian
plane, we want to emphasize the data 
that each place contains, therefore we 
translate our points in the z vector to get
what is called in computer graphics
Heightmap.
![docsthree](https://user-images.githubusercontent.com/21000020/47823280-8fc72b80-dd35-11e8-9dd6-1973d7c5bec9.JPG)
In the same fashion, we want to get some
sort of cross-relationship between data.
So we move our points according to the
top rainy places in the world. We do so
by picking the peak of the rain data and 
assigning those points to a Spin-Force 
component from the class of
Vector-Fields.
![docsfour](https://user-images.githubusercontent.com/21000020/47823283-8fc72b80-dd35-11e8-8d11-91cd00f51b58.JPG)
We can do a similar process with our
Spherical Projection.
![docsfive](https://user-images.githubusercontent.com/21000020/47823282-8fc72b80-dd35-11e8-9f58-8869d03876b5.JPG)

