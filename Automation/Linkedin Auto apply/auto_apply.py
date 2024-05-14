from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "Jatin123"
ACCOUNT_PASSWORD = "<PASSWORD>"
PHONE_NUMBER = "+91123456789"

def abort_application():
    # Click close Button
    close_buttons = driver.find_element(by = By.CLASS_NAME,value = "artdeco-modal__dismiss")
    close_buttons.click()

    time.sleep(2)

    # Click Discard button
    discard_button = driver.find_element(by = By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


# keep the browser open if script crashes.
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options = edge_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3816175760&f_LF=f_AL&f_WT=2&geoId=102713980&keywords=python%20developer&location=India&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by = By.CSS_SELECTOR, value = 'button[action-type="DENY"]')
reject_button.click()

# click sign-in button
time.sleep(5)
email_box = driver.find_element(by = By.ID, value = "username")
email_box.send_keys(ACCOUNT_EMAIL)
password_box = driver.find_element(by = By.ID, value = "password")
password_box.send_keys(ACCOUNT_PASSWORD)
password_box.send_keys(Keys.ENTER)

# CAPTCHA
input("Please Enter any key to continue")

# get listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value = '.job-card-container--clickable')

# apply for jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)

    try:
        # click apply button
        apply_button = driver.find_element(by = By.CSS_SELECTOR, value = '.jobs-s-apply button')
        apply_button.click()

        # insert phone number
        time.sleep(5)
        phone = driver.find_element(by = By.CSS_SELECTOR, value = 'input[id*=phoneNumber')
        if phone.text == "":
            phone.send_keys(PHONE_NUMBER)

        # Check the submit button
        submit_button = driver.find_element(by = By.CSS_SELECTOR, value = 'footer button')
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # click submit button
            print("Submitting application...")
            submit_button.click()

        time.sleep(2)

        # click close button
        close_button = driver.find_element(by = By.CLASS_NAME, value = 'artdeco-modal__dismiss')
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No apply button, skipped.")
        continue

time.sleep(5)
driver.quit()

