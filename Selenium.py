# -*- coding: cp1252 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
import glob
import os

# Function slightly modified from https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder-using-python
def downloadWait( path ):
    
    seconds = 0
    wait = True
    
    while wait and seconds < 120:
        
        time.sleep(1)
        wait = False
        
        for fname in os.listdir( path ):
            
            if fname.endswith( '.crdownload' ):
                
                wait = True

            else:

                wait = False
                
        seconds += 1
        
    return wait

path = raw_input( "Define the path to the directory where you want to download the data, (if it doesn't exist the program will create a new one): " );

if not os.path.exists( path ):
    os.mkdir( path )
else:
    print( "Folder already exists." )

pageLink = "http://nomads.ncep.noaa.gov/"

searchFor = raw_input( "Enter the specific data set you want to download: " )

# Setup our chrome preferences.
chromeOptions = webdriver.ChromeOptions()
prefs = { "download.default_directory" : path }
chromeOptions.add_experimental_option( "prefs", prefs )
chromedriver = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe"

driver = webdriver.Chrome( executable_path = chromedriver, chrome_options = chromeOptions )

driver.get( pageLink )

elements = None
clicks = None

rowCount = len( driver.find_elements( By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/center/table[3]/tbody/tr" ) )

for i in driver.find_elements( By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/center/table[3]" ):
    for j in range( rowCount ):
        
        elements = i.find_elements_by_tag_name( "tr" )[j]
        
        if elements.text.find( searchFor ) == -1:
            
            print( "No: " + searchFor  )

        else:

            print( "Eureka: " + searchFor )
            clicks = elements.find_elements_by_link_text( "grib filter" )
            break

clicks[0].click()
listClicks = driver.find_elements_by_tag_name( 'a' )
numberOfClicks = len( listClicks )
fileOriginal = ''
fileRenames = [None] * numberOfClicks
iterCounter = 0

for i in range( 0, numberOfClicks ):

    driver.execute_script( "window.open('" + listClicks[i].get_attribute( "href" ) + "');" )
    fileRenames[i] = listClicks[i].text
    print( fileRenames[i] )

fileRenames.reverse()
    
for handle in driver.window_handles:
    
    driver.switch_to.window( handle )
    links = driver.find_elements( By.XPATH, "/html/body/form/p[10]/input[1]" )
    
    if len( links ) > 0:
        
        links[0].click()
        #print( links )

        fileOriginal = ( driver.find_element( By.XPATH, "/html/body/form/p[2]/select/option" ) )
        fileOriginal = ( fileOriginal.text.strip().split( ' ' )[0] )
        boolean = downloadWait( path )

        if boolean == False:
        
            listOfFiles = glob.glob( path + "\\*" )
            latestFile = max( listOfFiles, key = os.path.getctime )

            os.rename( latestFile, path + "\\" + fileRenames[iterCounter] + ".grb2" )

            iterCounter += 1
