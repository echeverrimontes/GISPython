from osgeo import gdal
import numpy as np
np.set_printoptions( threshold = np.nan )
import struct
import pandas as pd
from mpl_toolkits.basemap import Basemap

# Read the GRIB file
dataset = gdal.Open( 'C:\Users\Paula\Downloads\pgbf2018101806.01.2018101806.grb2', gdal.GA_ReadOnly )

count = dataset.RasterCount

for i in range( 1, count ):
    
    print( 'Raster Band #: ' + str( i ) + ' has ' + str( dataset.GetRasterBand( i ).XSize ) + ' Rows' )
    print( 'Raster Band #: ' + str( i ) + ' has ' + str( dataset.GetRasterBand( i ).YSize ) + ' Columns' )

band = dataset.GetRasterBand( 1 )

# Use a C struct to store our band data.
'''
pd.set_option( 'display.max_rows', band.YSize )
pd.set_option( 'display.max_columns', band.XSize )
'''

'''
scanline = band.ReadRaster(xoff=0, yoff=0,
                           xsize=band.XSize, ysize=1,
                           buf_xsize=band.XSize, buf_ysize=1,
                           buf_type=gdal.GDT_Float32)
tuple_of_floats = struct.unpack( 'f' * band.XSize, scanline )

print( ( tuple_of_floats ) )

'''

meta = band.GetMetadata()

#print( dataset.GetProjection() )

#print( dataset.GetProjectionRef() )
#print( dataset.GetGeoTransform() )

print( meta )

# Read as numpy array.
#data = dataset.ReadAsArray().astype( np.float32 )

# Print using pandas.
#print( pd.DataFrame.from_records( data ) )

# Number of items in numpy array.
#print( sum( len( x ) for x in data ) )
#print( data )



