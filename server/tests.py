from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    options = Options()
    #options.add_argument("--headless")  # run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)  # make sure chromedriver is in PATH

    try:
        url = "https://faridabad.dcourts.gov.in/court-orders-search-by-case-number/"
        driver.get(url)
        print("yes")  # confirm page loaded
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
