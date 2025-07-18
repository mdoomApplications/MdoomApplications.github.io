#!/usr/bin/env python3
"""
Screenshot script to capture website appearance
"""

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_screenshot():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    try:
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Get the current directory
        current_dir = os.getcwd()
        index_path = os.path.join(current_dir, "index.html")
        
        # Navigate to the local HTML file
        driver.get(f"file://{index_path}")
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Wait a bit more for styling to load
        time.sleep(3)
        
        # Take screenshot
        screenshot_path = os.path.join(current_dir, "website_screenshot.png")
        driver.save_screenshot(screenshot_path)
        
        print(f"Screenshot saved to: {screenshot_path}")
        
        # Also take a screenshot of the documentation page
        doc_path = os.path.join(current_dir, "documentation.html")
        driver.get(f"file://{doc_path}")
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        time.sleep(3)
        
        # Take screenshot of documentation
        doc_screenshot_path = os.path.join(current_dir, "documentation_screenshot.png")
        driver.save_screenshot(doc_screenshot_path)
        
        print(f"Documentation screenshot saved to: {doc_screenshot_path}")
        
        return True
        
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return False
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    success = take_screenshot()
    sys.exit(0 if success else 1)