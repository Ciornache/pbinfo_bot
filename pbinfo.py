from asyncio.windows_events import NULL
from hashlib import pbkdf2_hmac
from hmac import new
from multiprocessing.connection import wait
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,  NoSuchWindowException, TimeoutException
driver = webdriver.Chrome(
    executable_path="chromedriver.exe")
driver.get("https://pastebin.com/u/a53")
index, pageButton, cnt, solutionVector, ID, Index, page = 1, 1, 1, [], [], 3, 1
pb, names = [], []


class PbinfoBot:

    def GetSolutions():
        global cnt, index, pageButton, solutionVector
        while cnt <= 20:
            problemName = driver.find_element(
                By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[{}]/td[1]/a'.format(index))
            names.append(problemName.text)
            if problemName.text == 'CPPREFERANCE':
                index = index + 1
                continue
            problemName.click()
            try:
                print("here")
                WebDriverWait(driver, 2).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]')))
                agreeButton = driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[2]")
                agreeButton.click()
            except (NoSuchWindowException, NoSuchElementException, TimeoutException):
                pass
            solution = driver.find_element(
                By.CLASS_NAME, 'text')
            solutionVector.append(solution.text)
            print(solution.text)
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
            WebDriverWait(driver, 10).until_not(
                EC.element_located_to_be_selected((By.ID, "aswift_11")))
        except:
            driver.get("https://www.pbinfo.ro/")
            username.send_keys('MonkeyDLuffy')
            password.send_keys('peakpiece1234')
        driver.find_element(
            By.XPATH, '//*[@id="form-login"]/div/div[2]/div[4]/button').click()

    def GetProblemsIDS():
        global ID, Index, page
        driver.get("https://www.pbinfo.ro/probleme")
        while 1:
            global id, name
            id = driver.find_elements(By.CLASS_NAME, "float-right")
            name = driver.find_elements(By.CLASS_NAME, "float-right")
            for i in id:
                ID.append(i)
            for i in name:
                pb.append(i)
            page += 1
            driver.get(
                "https://www.pbinfo.ro/probleme?start={}".format(page*10 - 10))

    def UploadProblems():
        for i in range(1, ID.length - 1):
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


def swap(a, b):
    crt = a
    a = b
    b = crt


PbinfoBot.GetSolutions()
PbinfoBot.LogIntoPbinfo()
PbinfoBot.GetProblemsIDS()
for i in range(1, names.length - 1):
    for j in range(i + 1, names.length-1):
        if i > j:
            swap(names[i], names[j]), swap(
                solutionVector[i], solutionVector[j])
PbinfoBot.UploadProblems()
