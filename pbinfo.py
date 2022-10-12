from asyncio.windows_events import NULL
from hashlib import pbkdf2_hmac
from hmac import new
from multiprocessing.connection import wait
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,  NoSuchWindowException, TimeoutException, StaleElementReferenceException
import json
driver = webdriver.Chrome(
    executable_path="chromedriver.exe")
index, pageButton, cnt, solutionVector, ID, Index, page = 1, 15, 1, [], [], 3, 1
pb, names = [], []
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)


def swap(a, b):
    crt = a
    a = b
    b = crt


class PbinfoBot:

    def GetSolutions():
        driver.get("https://pastebin.com/u/a53")
        global cnt, index, pageButton, solutionVector
        yes = 0
        while pageButton <= 20:
            if pageButton == 20 and index == 75:
                break
            problemName = driver.find_element(
                By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[{}]/td[1]/a'.format(index))
            names.append(problemName.text)
            if problemName.text == 'CPPREFERANCE':
                index = index + 1
                continue
            problemName.click()
            if yes == 0:
                try:
                    WebDriverWait(driver, 2).until(EC.presence_of_element_located(
                        (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]')))
                    agreeButton = driver.find_element(
                        By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[2]")
                    agreeButton.click()
                except (NoSuchWindowException, NoSuchElementException, TimeoutException):
                    pass
            yes += 1
            solution = driver.find_element(
                By.CLASS_NAME, 'text')
            solutionVector.append(solution.text)
            index = index + 1
            if index > 100:
                index = index - 100
                pageButton += 1
            driver.get("https://pastebin.com/u/a53/{}".format(pageButton))

    def PrintSomething():
        print("ONE PIECE")

    def LogIntoPbinfo():
        driver.get("https://www.pbinfo.ro/")
        username = driver.find_element(
            By.XPATH, '/html/body/div[2]/div[6]/div/div[4]/div[1]/div[2]/form/div/div[2]/div[1]/input')
        username.send_keys('MonkeyDLuffy')
        password = driver.find_element(
            By.XPATH, '/html/body/div[2]/div[6]/div/div[4]/div[1]/div[2]/form/div/div[2]/div[2]/input')
        password.send_keys('peakpiece1234')
        try:
            element = WebDriverWait(driver, 10).until_not(
                EC.presence_of_element_located((By.ID, "aswift_11")))
        except (StaleElementReferenceException, TimeoutException):
            driver.get("https://www.pbinfo.ro/")
            sleep(2)
            username = driver.find_element(
                By.XPATH, '/html/body/div[2]/div[6]/div/div[4]/div[1]/div[2]/form/div/div[2]/div[1]/input')
            password = driver.find_element(
                By.XPATH, '/html/body/div[2]/div[6]/div/div[4]/div[1]/div[2]/form/div/div[2]/div[2]/input')
            username.send_keys('MonkeyDLuffy')
            password.send_keys('peakpiece1234')
        driver.find_element(
            By.XPATH, '//*[@id="form-login"]/div/div[2]/div[4]/button').click()

    def GetProblemsIDS():
        global ID, Index, page
        driver.get("https://www.pbinfo.ro/probleme")
        while page <= 346:
            global id, name
            id = driver.find_elements(By.CLASS_NAME, "float-right")
            name = driver.find_elements(
                By.XPATH, "/html/body/div[3]/div[4]/div/div[5]/div[2]/div[4]/div[1]/h3/a[1]".format(Index))
            for i in id:
                ID.append(i.text)
            for i in name:
                pb.append(i.text)
            page += 1
            driver.get(
                "https://www.pbinfo.ro/probleme?start={}".format(page*10 - 10))

    def UploadProblems():
        for i in range(1, len(ID) - 1):
            currID, currName, lf, rg, solution = ID[i], pb[i], 0, name.length - 1, ''
            while st <= dr:
                mid = (st + dr) / 2
                if name[mid] == currName:
                    solution = solutionVector[mid]
                    break
                elif name[mid] < currName:
                    st = mid + 1
                else:
                    dr = mid - 1
            driver.get(
                "https://www.pbinfo.ro/probleme/{}/{}".format(currID, currName))
            form = driver.find_element(By.CLASS_NAME, "CodeMirror-scroll")
            form.send_keys(solution)
            driver.find_element(
                By.XPATH, "/html/body/div[2]/div[3]/div/div[11]/div/div[12]/div[2]/div/form/div[4]/button").click()

    def CreateJson(data, name):
        with open(name, 'w') as i:
            json.dump(data, i, indent=len(data))

    def AlternateSolution():
        driver.get("https://www.pbinfo.ro/")
        autIcon = driver.find_element(
            By.XPATH, "/html/body/div[2]/nav/div/div[2]/ul[2]/li[1]/a/i")
        autIcon.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/form/div[2]/div[1]/div/input")))
        utilizator = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/form/div[2]/div[1]/div/input")
        parola = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/form/div[2]/div[2]/div/input")
        utilizator.send_keys("MonkeyDLuffy")
        parola.send_keys("peakpiece1234")
        autButton = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/form/div[3]/div[1]/div/button[2]")
        autButton.click()


PbinfoBot.GetSolutions()
PbinfoBot.AlternateSolution()
PbinfoBot.GetProblemsIDS()
for i in range(1, len(names) - 1):
    for j in range(i + 1, len(names)-1):
        if i > j:
            swap(names[i], names[j]), swap(
                solutionVector[i], solutionVector[j])
