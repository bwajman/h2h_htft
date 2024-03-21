from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://www.betexplorer.com/")

wait = WebDriverWait(driver,25)
element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer__bottom__info")))

rows = driver.find_elements(By.CSS_SELECTOR, "li[class*='showHide']")

matches = [row.text.replace('\n',';') for row in rows]
links = [row.find_element(By.TAG_NAME,"a").get_attribute('href') for row in rows]

print(matches)
print(links)

results = []
h2h = []
for link in links:
    ft,ht = ':',':'
    driver.get(link)
    try:
        ft = driver.find_element(By.ID, "js-score").text
        ht=driver.find_element(By.ID,"js-partial").text
    except NoSuchElementException:
        pass
    a = list([ft,ht])
    results.append(a)
    histories = driver.find_elements(By.CLASS_NAME,'head-to-head__row')
    for history in histories:
        match = history.text.replace('\n',';')
        print(f"{match};{link}")
    break


print(results)
driver.quit()

