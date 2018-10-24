from mpl_toolkits.basemap import Basemap, shiftgrid, addcyclic
import osr, gdal
import matplotlib.pyplot as plt
import numpy as np
#np.set_printoptions( threshold = np.nan )
import pandas as pd
#pd.set_option( "display.max_rows", None )

# Read the data and metadata
# Wind.
ds = gdal.Open( 'C:\Users\Paula\Downloads\pgbf2018102406.01.2018102406.grb2', gdal.GA_ReadOnly )
# Sea Ice
dsOne = gdal.Open( 'C:\Users\Paula\Downloads\seaice.t00z.grb (2).grib2', gdal.GA_ReadOnly )

data = ds.ReadAsArray()
dataOne = dsOne.ReadAsArray()
gt = ds.GetGeoTransform()
gtOne = dsOne.GetGeoTransform()
proj = ds.GetProjection()
projOne = dsOne.GetProjection()

xres = gt[1]
xresOne = gtOne[1]
yres = gt[5]
yresOne = gtOne[5]

xsize = ds.RasterXSize
ysize = ds.RasterYSize

xsizeOne = dsOne.RasterXSize
ysizeOne = dsOne.RasterYSize

# get the edge coordinates and add half the resolution 
# to go to center coordinates
xmin = gt[0] + xres * 0.5
xminOne = gtOne[0] + xresOne * 0.5
xmax = gt[0] + (xres * xsize) - xres * 0.5
xmaxOne = gtOne[0] + (xresOne * xsizeOne) - xresOne * 0.5
ymin = gt[3] + (yres * ysize) + yres * 0.5
yminOne = gtOne[3] + (yresOne * ysizeOne) + yresOne * 0.5
ymax = gt[3] - yres * 0.5
ymaxOne = gtOne[3] - yresOne * 0.5

ds = None
dsOne = None

xx = np.arange( xmin, xmax + xres, xres )
xxOne = np.arange( xminOne, xmaxOne + xresOne, xresOne )
yy = np.arange( ymax + yres, ymin, yres )
yyOne = np.arange( ymaxOne + yresOne, yminOne, yresOne )

data, xx = shiftgrid( 180.0, data, xx, start = False )

dataOne, xxOne = shiftgrid( 180.0, dataOne, xxOne, start = False )

x, y = np.meshgrid( xx, yy )

df = pd.DataFrame( list( zip( x.flatten(), y.flatten(), data.flatten(), dataOne.flatten() ) ), columns = ["Latitude", "Longitude", "Wind", "Ice"] )

writer = pd.ExcelWriter( "C:\Users\Paula\Desktop\Felipe\IceLatLong.xlsx" )
df.to_excel( writer, "Sheet1", index = False )
writer.save()

'''

# Mercator
#m = Basemap(projection='merc',llcrnrlat=-85,urcrnrlat=85,\
#            llcrnrlon=-180,urcrnrlon=180,lat_ts=0,resolution='c')

# Robinson
#m = Basemap(projection='robin', lon_0=0, resolution='c')

# Cylindrical
m = Basemap(llcrnrlon=-180.0,llcrnrlat=-85.0,urcrnrlon=180.0,urcrnrlat=85.0,
            resolution='c',projection='cyl',lon_0=0.0,lat_0=0.0)

x, y = m(*np.meshgrid(xx,yy))

# plot the data (first layer) data[0,:,:].T
im1 = m.pcolormesh( x, y, data[2,:,:], shading = "flat", cmap=plt.cm.jet )

print( len( x ) * len( y ) )

# annotate
m.drawcountries()
m.drawcoastlines(linewidth=.5)

plt.show()
'''
