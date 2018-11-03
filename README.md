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

4.) Go to: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal and search for the GDAL wheel: GDAL‑2.2.4‑cp27‑cp27m‑win_amd64.whl download it (note that this the wheel that I need as I am running a 64 bits system and python 2.7, if you have a different configuration you should download the wheel that matches your machine and python version). Once it is in your computer type something like: pip install C:\Users\admin\donwloads\GDAL‑2.2.4‑cp27‑cp27m‑win_amd64.whl (look where the file is located).

5.) Repeat step 4 but this time download the Basemap wheel: basemap‑1.2.0‑cp27‑cp27m‑win_amd64.whl, install through pip as step 4 showed.

6.) Download Pandas, we need this to format and translate our data to Excel. Go to cmd.exe: pip install pandas

7.) Now open the command-line again and type: pip install openpyxl 

# Mac
1.) Download and install python 2.7.

2.) Go to terminal, you can do so by pressing at the same time the Command and Space keys, than type terminal.

3.) Go to http://www.kyngchaos.com/software/frameworks/ and download and install the GDAL 1.11 version.

4.) Now open the file explorer and press the Command, Shift and G key at the same time, this should enable you to search a directory. Type /Library/Frameworks/GDAL.framework/Versions/1.11/Python/2.7/site-packages and press enter. We need these files to be on our python site-packages folders. So copy all the files and folders.

5.) Repeat the Command, Shift and G press to go to another directory, this time is our python's directory which is at: /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/ once you are inside the directory paste all the files you have already copied from step 4.).

6.) Check if we have succesfully installed the library: go to Terminal and type: python than press enter, now type: import gdal if there are no errors we can continue with step 7.).

7.) Install homebrew:
Here is a detailed guide on how to install homebrew: http://osxdaily.com/2018/03/07/how-install-homebrew-mac-os/

8.) Go to Terminal and type:

brew install matplotlib

brew install numpy

brew install geos

brew install proj

9.) Download the basemap tar: https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/

10.) Untar the file.

11.) Go to the file explorer and repeat our favourite new combo of Command, Shift and G, than type /usr/local/Cellar/ 
Now search for the geos folder, once you are in you should see a version folder something like 3.7.0 in my case
Right click on the folder and press alt at the same time now you should be able to do: Copy "name of your folder" as Pathname click that one.

11.) Type on the Terminal: touch ~/.bash_profile; open ~/.bash_profile
Now add to the recently opened file: export GEOS_DIR="paste here your path name" 
so it should look something like: 
export GEOS_DIR=/usr/local/Cellar/geos/3.7.0/
Save the file and close it.

12.) Go to Terminal and type: source ~/.bash_profile

13.) In Terminal type: cd "the path of your untared basemap directory" 
in my case it looks like this: 
cd /Users/FelipeGutierrez/Downloads/basemap-1.0.7
You can get the path by going to where you untared the downloaded version of basemap right clicking on the folder and press alt at the same time now you should be able to do: Copy "name of your folder" as Pathname click that one.

14.) When you are in the directory type: python setup.py install

15.) Check your basemap install: Go to Terminal and type: python
Than type: import mpl_toolkits.basemap as bm
If it doesnt show any error you are good to go.

16.) Download Pandas, we need this to format and translate our data to Excel. Go to Terminal: pip install pandas

17.) Download openpyxl, Pandas needs this to be able to write to xlsl, do it through Terminal: pip install openpyxl 

You should be ready to run the python scripts.

# Note
The Basemap library is used for viz from python, if you are only interested in extracting the data to Excel than you might not need it.

Although I used python 2.7, this process should be easily extended to newer python versions, but I haven't personally tried it.

If you want to visualize the data from python uncomment line 58 from MultipleInputs.py and uncomment the end of the file from lines 150 to 172. You should also comment the lines that do the transfer to xlsl those go from 136 to 149.

# Data Manipulation and Viz using Rhinoceros and its famous Grasshopper plugin. 
# The definition is in this repo, its name is: Workshop (1).gh
# **Note: You must have installed the plugins TTToolbox and Tarsier, you can grab them respectively from: 
# https://www.food4rhino.com/app/tt-toolbox
# https://www.food4rhino.com/app/tarsier
# I haven't tested the Grasshopper definition on the MacOS version of Rhino.
We open our grib2 file with the ReadExcel component from TTToolbox. For the sake of organization I have multiple instances of the ReadExcel component, each one opens a different work sheet from the same Excel file. We could instead modify the python script to extract the data into different columns of the same work sheet for performance gains as we would only have one instance of the component but as I said it would lead to messy index lookups in comparison to our nice 0 for latitude, 1 for longitude and 2 for data.
The xlsx file is created from a Python 2.7 script that opens the grib2 file and saves
the values stored according to their coordinates. The python file is in this repo as MultipleInputs.py you should be able to mod it with not much hassle for your particular needs.
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
Note that we could do the projections in our python script to speed up the Grasshopper definition but for the sake of keeping everything in the scope of a more versed in Grasshopper scripting audience we are not going to. If you are still curious on how to implement this via python, the Basemap library that we use for our map creatiom provides some out of the box projections in our MultipleInputs.py file from line 151 to 162. If we wanted our data to be written to a xlsl, translating the projections nodes Cassini, WebMercator and Spherical from the Workshop (1).gh from C# to python shouldnt be that hard but we'll leave that as an excersice for the more coding savy readers.
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

