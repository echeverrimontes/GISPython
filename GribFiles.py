from osgeo import gdal
import numpy as np
np.set_printoptions( threshold = np.nan )
import struct
import pandas as pd

# Read the GRIB file
dataset = gdal.Open( 'C:\Users\Paula\Downloads\estofs.mic.t00z.guam.f000.grib2', gdal.GA_ReadOnly )
band = dataset.GetRasterBand(1)
pd.set_option( 'display.max_rows', band.YSize )
pd.set_option( 'display.max_columns', band.XSize )

'''
scanline = band.ReadRaster(xoff=0, yoff=0,
                           xsize=band.XSize, ysize=1,
                           buf_xsize=band.XSize, buf_ysize=1,
                           buf_type=gdal.GDT_Float32)
tuple_of_floats = struct.unpack( 'f' * band.XSize, scanline )

print( ( tuple_of_floats ) )

'''

meta = band.GetMetadata()

print( meta )

data = band.ReadAsArray().astype( np.float32 )

#print( pd.DataFrame.from_records( data ) )

# Number of items in numpy array.
#print( sum( len( x ) for x in data ) )
#print( data )



