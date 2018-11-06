from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

pageLink = "http://nomads.ncep.noaa.gov/"

driver = webdriver.Chrome( executable_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe" )
driver.get( pageLink )

searchFor = raw_input( "Enter the specific data set you want to download: " )
elements = None
clicks = None

rowCount = len( driver.find_elements( By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/center/table[3]/tbody/tr" ) )

for i in driver.find_elements( By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/center/table[3]" ):
    for j in range( rowCount ):
        
        elements = i.find_elements_by_tag_name( "tr" )[j]
        
        if elements.text.find( searchFor ) == -1:
            
            print( "No: " + searchFor  )

        else:
            
            clicks = elements.find_elements_by_link_text( "grib filter" )


clicks[0].click()
listClicks = driver.find_elements_by_tag_name( 'a' )

for link in listClicks:
    driver.execute_script( "window.open('" + link.get_attribute( "href" ) + "');" )
    time.sleep( 5 )
    clicker = driver.find_element( By.XPATH, "/html/body/form/p[8]/input" )
    clicker.click()
    #driver.implicitly_wait( 20 )
    #download = driver.find_element_by_tag_name( "Start download" )
    #download.click()
