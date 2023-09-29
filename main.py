from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# ur chrome driver version must be compatible with ur google chrome version
driver_path = "chromedriver_path "

# Set the system property to point to the ChromeDriver executable
webdriver.chrome.driver = driver_path

# Initialize the Chrome web driver
driver = webdriver.Chrome()

# Navigate to the web page you want to refresh
driver.get("your_link")

# Refresh the web page every 5 seconds (you can adjust the interval as needed)
refresh_interval = 1
try:
    while True:
        time.sleep(refresh_interval)
        driver.refresh()
except KeyboardInterrupt:
    # Press Ctrl+C to stop the script
    pass

# Close the browser when done
driver.quit()

