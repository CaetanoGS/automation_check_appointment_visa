import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from services.notification import play_visa_alarm, send_visa_notification

def check_appointment(team_id, button_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-notifications")  # Disable notifications

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://termine.staedteregion-aachen.de/auslaenderamt/")

        cookies_btn = driver.find_element(By.ID, 'cookie_msg_btn_yes')
        cookies_btn.click()

        btn = driver.find_element(By.ID, "buttonfunktionseinheit-1")
        btn.click()

        time.sleep(1)

        aufenthalt = driver.find_element(By.ID, 'header_concerns_accordion-456')
        aufenthalt.click()

        time.sleep(1)

        add_person = driver.find_element(By.ID, button_id)
        add_person.click()
        add_person.click()

        weiter_btn = driver.find_element(By.ID, 'WeiterButton')
        weiter_btn.click()

        time.sleep(1)

        okay_btn = driver.find_element(By.ID, 'OKButton')
        okay_btn.click()

        time.sleep(1)

        submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @name='select_location' and @value='Ausländeramt Aachen, 2. Etage auswählen']")
        submit_button.click()

        time.sleep(1)

        try:
            h2_element = driver.find_element(By.CLASS_NAME, "h1like")

            expected_text = "Kein freier Termin verfügbar"
            if h2_element.text != expected_text:
                send_visa_notification(f"team {team_id}")
                play_visa_alarm()

        except Exception as e:
            send_visa_notification(f"team {team_id}")
            play_visa_alarm()

    except Exception as e:
        print(f"An error occurred: {e}")
        send_visa_notification(f"team {team_id}")
        play_visa_alarm()
    finally:
        driver.quit()
