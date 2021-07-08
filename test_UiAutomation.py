

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from webdriver_manager.chrome import ChromeDriverManager

user_login="admin"
user_pass="admin"
host_ui="http://127.0.0.1:8080"

def test_Ui_CreateProject():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(host_ui)
    driver.maximize_window()

    driver.find_element(By.XPATH, "//span[contains(text(),'Sign in')]").click()

    driver.find_element(By.XPATH, "//input[@id='username-pulldown']").send_keys(user_login)

    driver.find_element(By.XPATH, "//input[@id='password-pulldown']").send_keys(user_pass)

    driver.find_element(By.XPATH, "//input[@id='login-pulldown']").click()

    ActionChains(driver).double_click(
        driver.find_element_by_xpath("//*[@id='content']/section[1]/div[2]/div[2]/a[1]/span")).perform()

    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='formly_3_textInput_name_0']").send_keys("PythonProject 1@2$3")

    name = driver.find_element(By.XPATH, "//input[@id='formly_3_textInput_name_0']").get_attribute('value')

    print(name)

    name1 = name.replace(' ', '-').lower()
    for char in name1:
        if char in "?.!:;/'@#$%^*()?/":
            name1 = name1.replace(char, '-')

    driver.find_element(By.XPATH, "//input[@id='formly_3_textInput_name_0']").clear()
    name1 = driver.find_element(By.XPATH, "//input[@id='formly_3_textInput_name_0']").send_keys(name1)

    driver.find_element(By.XPATH, "//button[contains(text(),'Advanced settings')]").click()

    advance_validation = driver.find_element(By.XPATH,
                                             "//body//div[@id='wrapper']//formly-field//formly-field[2]//op-dynamic-field-wrapper[1]//op-form-field[1]//label[1]//div[1]").text

    assert advance_validation == "Description"

    driver.find_element(By.XPATH,
                        "//body/div[@id='wrapper']/div[@id='main']/main[@id='content-wrapper']/div[@id='content']/openproject-base[1]/div[1]/ui-view[1]/op-new-project[1]/op-dynamic-form[1]/form[1]/formly-form[1]/formly-field[3]/op-dynamic-field-group-wrapper[1]/fieldset[1]/div[1]/formly-group[1]/formly-field[2]/op-dynamic-field-wrapper[1]/op-form-field[1]/div[2]/op-formattable-textarea-input[1]/op-formattable-control[1]/div[1]/op-ckeditor[1]/div[1]/div[2]/div[1]/p[1]").send_keys(
        "this is  Python Project")

    driver.find_element(By.XPATH,
                        "//body/div[@id='wrapper']/div[@id='main']/main[@id='content-wrapper']/div[@id='content']/openproject-base[1]/div[1]/ui-view[1]/op-new-project[1]/op-dynamic-form[1]/form[1]/formly-form[1]/formly-field[3]/op-dynamic-field-group-wrapper[1]/fieldset[1]/div[1]/formly-group[1]/formly-field[5]/op-dynamic-field-wrapper[1]/op-form-field[1]/label[1]/div[3]/op-select-project-status-input[1]/ng-select[1]/div[1]/span[1]").click()

    driver.find_element(By.XPATH, "//span[contains(text(),'On track')]").click()

    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()

    time.sleep(2)

    projectname = driver.find_element(By.XPATH, "//span[@class='op-app-menu--item-title ellipsis']").get_attribute(
        'value')

    assert projectname == name1

    driver.quit()


def test_Ui_CreateTask():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(host_ui)
    driver.maximize_window()

    driver.find_element(By.XPATH, "//span[contains(text(),'Sign in')]").click()

    driver.find_element(By.XPATH, "//input[@id='username-pulldown']").send_keys(user_login)

    driver.find_element(By.XPATH, "//input[@id='password-pulldown']").send_keys(user_pass)

    driver.find_element(By.XPATH, "//input[@id='login-pulldown']").click()

    driver.find_element(By.XPATH, "//span[@class='op-app-menu--item-title ellipsis']").click()

    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@id='project_autocompletion_input']").send_keys("TestProject1")

    ActionChains(driver).double_click(driver.find_element_by_xpath("//*[@id='ui-id-1']/li")).perform()

    driver.find_element(By.XPATH, "//a[@id='main-menu-work-packages']").click()

    time.sleep(2)

    table = driver.find_element(By.XPATH,
                                "//*[@id='content']/openproject-base/div/ui-view/openproject-base/div/ui-view/work-packages-base/div/ui-view/wp-view-page/div/div[3]/div[1]/wp-list-view/wp-table/div/div[1]/table")

    rowcount = len(table.find_elements(By.XPATH,
                                       "//*[@id='content']/openproject-base/div/ui-view/openproject-base/div/ui-view/work-packages-base/div/ui-view/wp-view-page/div/div[3]/div[1]/wp-list-view/wp-table/div/div[1]/table/tbody[1]/tr"))

    print(rowcount)

    driver.find_element(By.XPATH, "//div[@class='wp-create-button']").click()

    time.sleep(2)

    ActionChains(driver).double_click(
        driver.find_element_by_xpath("//*[@id='types-context-menu']/ul/li[1]/a")).perform()

    time.sleep(2)

    value1 = driver.find_element(By.XPATH,
                                 "//div[@class='inline-edit--container status wp-new-top-row--status -no-label']//div//span[@title='New'][normalize-space()='New']").text
    print(value1)
    value2 = driver.find_element(By.XPATH,
                                 "//div[@class='inline-edit--container type wp-new-top-row--type -no-label']//div//span[@title='Task'][normalize-space()='Task']").text
    print(value2)
    value = value1 + " " + value2

    assert value == "New TASK"

    driver.find_element(By.XPATH, "//input[@id='wp-new-inline-edit--field-subject']").send_keys("PYTHON")

    driver.find_element(By.XPATH, "//div[@aria-label='Rich Text Editor, main']").send_keys("THIS IS PYTHON PROJECT")

    driver.find_element(By.XPATH, "//button[@id='work-packages--edit-actions-save']").click()

    time.sleep(2)

    rowcount1 = len(driver.find_elements(By.XPATH,
                                         "//*[@id='content']/openproject-base/div/ui-view/openproject-base/div/ui-view/work-packages-base/div/ui-view/wp-view-page/div/div[3]/div[1]/wp-list-view/wp-table/div/div[1]/table/tbody[1]/tr"))

    print(rowcount)

    assert rowcount != rowcount1

    value3 = driver.find_element(By.XPATH,
                                 "//*[@id='content']/openproject-base/div/ui-view/openproject-base/div/ui-view/work-packages-base/div/ui-view/wp-view-page/div/div[3]/div[2]/wp-split-view-entry/div/div[1]/edit-form/div[1]/div/wp-subject/div/div[1]/editable-attribute-field/div/div[2]/span").text
    print(value3)
    assert value3 == "TASK"

    value4 = driver.find_element(By.XPATH,
                                 "//*[@id='content']/openproject-base/div/ui-view/openproject-base/div/ui-view/work-packages-base/div/ui-view/wp-view-page/div/div[3]/div[2]/wp-split-view-entry/div/div[1]/edit-form/div[1]/div/wp-subject/div/div[2]/editable-attribute-field/div/div[2]/span").text
    print(value4)
    assert value4 == "PYTHON"

    print("finished")
    driver.quit()

