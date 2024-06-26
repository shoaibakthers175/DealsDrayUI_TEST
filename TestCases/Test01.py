
import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Defining the browsers, resolutions, and URL to test
browsers = ['chrome', 'edge', 'firefox']
resolutions = [(1920, 1080), (1366, 768), (1536, 864),(360, 640), (414, 896), (375, 667)]
url = ['https://www.getcalley.com/', 'https://www.getcalley.com/calley-call-from-browser/', 'https://www.getcalley.com/calley-pro-features/',
       'https://www.getcalley.com/best-auto-dialer-app/', 'https://www.getcalley.com/how-calley-auto-dialer-app-works/']




def start_browser(browser_name, resolution):
    if browser_name == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome()
    elif browser_name == 'edge':
        options = EdgeOptions()
        driver = webdriver.Edge()
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.set_window_size(resolution[0], resolution[1])
    return driver

# Define the main function to run the tests
def run_tests():
    for browser in browsers:
        for resolution in resolutions:
            for urls in url:
                driver = start_browser(browser, resolution)
                driver.get(urls)
                time.sleep(5)  # Wait for the page to load completely
                actual_size = driver.get_window_size()
                print(f"Window size for {browser} is set to {actual_size}")

                # Capture screenshot
                now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f"{browser}_{resolution[0]}x{resolution[1]}_{now}.png"
                folder_path = f"screenshots/{browser}/{resolution[0]}x{resolution[1]}"
                os.makedirs(folder_path, exist_ok=True)
                screenshot_path = os.path.join(folder_path, filename)
                driver.save_screenshot(screenshot_path)
                print(f"Screenshot saved at {screenshot_path}")

                # Close the browser
                driver.quit()




# Run the tests
if __name__ == "__main__":
    run_tests()