from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
import osr, gdal
import matplotlib.pyplot as plt
import numpy as np

def convertXY(xy_source, inproj, outproj):
    # function to convert coordinates

    shape = xy_source[0,:,:].shape
    size = xy_source[0,:,:].size

    # the ct object takes and returns pairs of x,y, not 2d grids
    # so the the grid needs to be reshaped (flattened) and back.
    ct = osr.CoordinateTransformation(inproj, outproj)
    xy_target = np.array(ct.TransformPoints(xy_source.reshape(2, size).T))

    xx = xy_target[:,0].reshape(shape)
    yy = xy_target[:,1].reshape(shape)

    return xx, yy

# Read the data and metadata
# Pluviocidad.
#ds = gdal.Open( 'C:\Users\Paula\Downloads\enspost.t00z.prcp_24hbc (1).grib2', gdal.GA_ReadOnly )
# Sea Ice
ds = gdal.Open( 'C:\Users\Paula\Downloads\seaice.t00z.grb (2).grib2', gdal.GA_ReadOnly )
data = ds.ReadAsArray()
gt = ds.GetGeoTransform()
proj = ds.GetProjection()

xres = gt[1]
yres = gt[5]

xsize = ds.RasterXSize
ysize = ds.RasterYSize

# get the edge coordinates and add half the resolution 
# to go to center coordinates
xmin = gt[0] + xres * 0.5
xmin -= 180.0
xmax = gt[0] + (xres * xsize) - xres * 0.5
xmax -= 180.0
ymin = gt[3] + (yres * ysize) + yres * 0.5
ymax = gt[3] - yres * 0.5

ds = None

# create a grid of xy coordinates in the original projection
xy_source = np.mgrid[xmin:xmax+xres:xres, ymax+yres:ymin:yres]

# Create the figure and basemap object
fig = plt.figure(figsize=(12, 6))

m = Basemap(projection='robin', lon_0=0, resolution='c')
#m = Basemap(projection='merc', lon_0=0, llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='c',)

#m = Basemap(projection='merc',llcrnrlat=-85,urcrnrlat=85,\
#            llcrnrlon=-180,urcrnrlon=180,lat_ts=0,resolution='c')

#m = Basemap(llcrnrlon=-180,llcrnrlat=-90,urcrnrlon=180,urcrnrlat=59.5,
#            resolution='i',projection='cass',lon_0=-4.36,lat_0=54.7)

# Create the projection objects for the convertion
inproj = osr.SpatialReference()
inproj.ImportFromWkt(proj)

# Get the target projection from the basemap object
outproj = osr.SpatialReference()
outproj.ImportFromProj4(m.proj4string)

# Convert from source projection to basemap projection
xx, yy = convertXY(xy_source, inproj, outproj)

temp = np.zeros( ( ysize, xsize ) )
temp[:,0:ysize] = data[:,ysize:xsize]
temp[:,ysize:xsize] = data[:,0:ysize]
data[:] = temp[:]

# plot the data (first layer) data[0,:,:].T
im1 = m.pcolor(xx, yy, data.T, cmap=plt.cm.jet)

# annotate
m.drawcountries()
m.drawcoastlines(linewidth=.5)

plt.show()


