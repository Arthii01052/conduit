# TC008_test - My blog post delete (pytest)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = True


def test_blog_delete():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    # Load page
    driver.get("http://localhost:1667/")
    time.sleep(3)

    # Enter the data to be uploaded
    email = 'testuser1@example.com'
    username = 'testuser1'
    pwd = 'Abcd123$'

    # Fields xpath
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
    username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
    sign_button_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
    sign_in_btn_x = '//*[@id="app"]/div/div/div/div/form/button'
    mytitle_btn_x = '//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a'
    posttilte_x = '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1'
    delete_btn_x = '//*[@id="app"]/div/div[1]/div/div/span/button/span'
    article_preview = '//*[@class="article-preview"]'

    # Sign in
    sign_button = driver.find_element(By.XPATH, sign_button_x)
    sign_button.click()
    driver.find_element(By.XPATH, email_x).send_keys(email)
    driver.find_element(By.XPATH, pwd_x).send_keys(pwd)
    sign_in_btn = driver.find_element(By.XPATH, sign_in_btn_x)
    sign_in_btn.click()
    time.sleep(2)

    # Check box
    assert username == driver.find_element(By.XPATH, username_x).text
    time.sleep(2)

    # Post find
    driver.find_element(By.XPATH, username_x).click()  # username click
    time.sleep(2)
    driver.find_element(By.XPATH, mytitle_btn_x).click()  # my title click
    time.sleep(2)

    article_number = driver.find_elements(By.XPATH, article_preview)
    original_num = int(len(article_number))

    # Post delete
    driver.find_element(By.XPATH, posttilte_x).click()  # post title click
    time.sleep(2)
    driver.find_element(By.XPATH, delete_btn_x).click()  # delete button click
    time.sleep(2)
    driver.find_element(By.XPATH, username_x).click()  # username click
    time.sleep(2)

    # Control
    article_number = driver.find_elements(By.XPATH, article_preview)
    new_num = int(len(article_number))
    assert new_num < original_num

    driver.close()
    driver.quit()