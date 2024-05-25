import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Specify the path to the chromedriver executable
chromedriver_path = "D:\Downloads\chromedriver-win64\chromedriver.exe"  # Update with your actual path

# Set up the webdriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the NSE India option chain page
    url = "https://www.nseindia.com/option-chain"
    driver.get(url)

    # Wait for the page to load completely
    time.sleep(5)  # Adjust this sleep time based on your internet speed and page load time

    # Handle cookie consent if present
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cookieConsentButtonId"))  # Update with actual ID if needed
        )
        cookie_button.click()
    except:
        pass  # Ignore if the cookie consent button is not found

    # Wait until the download button is present
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "download_csv"))
    )

    # Loop to click the download button every 10 seconds
    while True:
        try:
            # Locate the download button by its ID
            download_button = driver.find_element(By.ID, "download_csv")

            # Click the download button
            download_button.click()

            print("Download button clicked.")

        except Exception as e:
            print(f"Error occurred: {e}")

        # Wait for 10 seconds before the next click
        time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
