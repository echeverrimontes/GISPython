from mpl_toolkits.basemap import Basemap, shiftgrid, addcyclic
import osr, gdal
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions( threshold = np.nan )
import cartopy.crs as ccrs
import pandas as pd
pd.set_option( "display.max_rows", None )

# Read the data and metadata
# Wind.
ds = gdal.Open( 'C:\Users\Paula\Downloads\pgbf2018102406.01.2018102406.grb2', gdal.GA_ReadOnly )
# Sea Ice
#ds = gdal.Open( 'C:\Users\Paula\Downloads\seaice.t00z.grb (2).grib2', gdal.GA_ReadOnly )

data = ds.ReadAsArray()
gt = ds.GetGeoTransform()
proj = ds.GetProjection()

print( data )

'''
xres = gt[1]
yres = gt[5]

xsize = ds.RasterXSize
ysize = ds.RasterYSize

# get the edge coordinates and add half the resolution 
# to go to center coordinates
xmin = gt[0] + xres * 0.5
xmax = gt[0] + (xres * xsize) - xres * 0.5
ymin = gt[3] + (yres * ysize) + yres * 0.5
ymax = gt[3] - yres * 0.5

ds = None

xx = np.arange( xmin, xmax + xres, xres )
yy = np.arange( ymax + yres, ymin, yres )

print( "xminimum: " + str( xmin ) )
print( "xmaximum: " + str( xmax ) )
print( "xres: " + str( xres ) )

data, xx = shiftgrid( 180.0, data, xx, start = False )

x, y = np.meshgrid( xx, yy )

df = pd.DataFrame( list( zip( x.flatten(), y.flatten(), data.flatten() ) ), columns = ["Latitude", "Longitude", "Wind"] )

writer = pd.ExcelWriter( "C:\Users\Paula\Desktop\Felipe\WindLatLong.xlsx" )
df.to_excel( writer, "Sheet1", index = False )
writer.save()
'''
'''

# Mercator
m = Basemap(projection='merc',llcrnrlat=-85,urcrnrlat=85,\
            llcrnrlon=-180,urcrnrlon=180,lat_ts=0,resolution='c')

# Robinson
#m = Basemap(projection='robin', lon_0=0, resolution='c')

# Cylindrical
#m = Basemap(llcrnrlon=-180.0,llcrnrlat=-85.0,urcrnrlon=180.0,urcrnrlat=85.0,
#            resolution='c',projection='cyl',lon_0=0.0,lat_0=0.0)

x, y = m(*np.meshgrid(xx,yy))

# plot the data (first layer) data[0,:,:].T
im1 = m.pcolormesh( x, y, data[0,:,:], shading = "flat", cmap=plt.cm.jet )

print( len( x ) * len( y ) )

# annotate
m.drawcountries()
m.drawcoastlines(linewidth=.5)

plt.show()
'''
