from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#waiting until page is loaded
driver.get('https://www.kwcelebration.com/our-agents/')
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

#finding the list of all agents
agents_details = []
agents_list = driver.find_elements(By.XPATH, '//div[@class="agent-information"]')

#iterating over the list and finding all neccessary information
for agent in agents_list:
    f_name = agent.find_element(By.CLASS_NAME, 'first').text
    l_name = agent.find_element(By.CLASS_NAME, 'last').text
    mobile = agent.find_element(By.TAG_NAME, 'a').get_attribute('href').replace('tel:', '')
    email = agent.find_element(By.XPATH, './/a[contains(@href, "mailto:")]').get_attribute('href')

#appending data to the list      
    agents_details.append({
        'first_name': f_name,
        'last_name': l_name,
        'mobile_phone': mobile.replace('.', '-'),
        'email': email.replace('mailto:','')
        })

driver.quit()

#converting list as a data frame
df = pd.DataFrame(agents_details)

#saving data to an Excel file
df.to_excel(r'C:\Users\Nowy_użytkownik\Desktop\kwcelebration.xlsx',index=False)

