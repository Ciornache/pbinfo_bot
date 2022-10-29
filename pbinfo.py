from asyncio.windows_events import NULL
from hashlib import pbkdf2_hmac
from hmac import new
from http.client import NETWORK_AUTHENTICATION_REQUIRED
from multiprocessing.connection import wait
from telnetlib import LOGOUT
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,  NoSuchWindowException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import json
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(
    executable_path="chromedriver.exe")
index, pageButton, cnt, solutionVector, ID, Index, page = 1, 1, 1, [], [], 3, 1
pb, names = [], []
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)


def swap(a, b):
    crt = a
    a = b
    b = crt


def Good(a):
    yes = ''
    for j in a:
        if j != '#':
            yes += j
    return yes


action = ActionChains(driver)


class PbinfoBot:
    def __init__(self):
        driver.maximize_window()

    def GetSolutions(self):
        driver.get("https://pastebin.com/u/a53")
        global cnt, index, pageButton, solutionVector
        yes = 0
        while pageButton <= 20:
            try:
                problemName = driver.find_element(
                    By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[{}]/td[1]/a'.format(index))
            except (NoSuchElementException):
                break
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
        self.CreateJson(names, "A53_problem_names.json")
        self.CreateJson(solutionVector, "solutions.json")

    def GetProblemsIDS(self):
        global ID, Index, page
        driver.get("https://www.pbinfo.ro/probleme")
        while page <= 346:
            global id, name
            id = driver.find_elements(By.CLASS_NAME, "float-right")
            name = driver.find_elements(
                By.CLASS_NAME, "panel-title")
            for i in id:
                ID.append(i.text), print(i.text)
            for i in name:
                pb.append(i.text)
            page += 1
            driver.get(
                "https://www.pbinfo.ro/probleme?start={}".format(page*10 - 10))
        self.CreateJson(ID, "Problem_id.json")
        self.CreateJson(pb, "Problem_name.json")

    def UploadProblems(self):
        for i in range(0, len(pb) - 1):
            driver.get("https://www.pbinfo.ro/probleme/{}".format(Good(ID[i])))
            WebDriverWait(driver, 30).until(EC.visibility_of((driver.find_element(
                By.XPATH, "//*[@id={}]/a".format("'meniu-problema-enunt'")))))
            solution = ""
            sleep(1)
            for j in range(0, len(names) - 1):
                if names[j] == pb[i]:
                    solution = solutionVector[j - 1]
                    break
            if solution == "":
                continue
            sleep(2)
            driver.get("https://pastebin.com/")
            try:
                agree = driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[2]")
                agree.click()
                sleep(2)
            except:
                pass
            textArea = driver.find_element(
                By.XPATH, "//*[@id='postform-text']")
            textArea.send_keys(solution)
            pyautogui.moveTo(600, 700, duration=2)
            pyautogui.hotkey("ctrl", "a", "c")
            driver.get("https://www.pbinfo.ro/probleme/{}".format(Good(ID[i])))
            print(30)
            go = driver.find_element(
                By.CLASS_NAME, "CodeMirror-scroll")
            driver.execute_script("arguments[0].scrollIntoView();", go)
            pyautogui.move(0, -200, duration=1)
            pyautogui.click()
            pyautogui.hotkey("ctrl", "v")
            sub = driver.find_element(
                By.ID, "btn-submit")
            driver.execute_script("arguments[0].scrollIntoView();", sub)
            sub.click()
            while 1:
                if sub.text == "Adaugă soluția":
                    break

    def CreateJson(self, data, name):
        with open(name, 'w') as i:
            json.dump(data, i, indent=0)

    def LogIntoPbinfo(self):
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
        sleep(3)


# Initializing Bot
Luffy = PbinfoBot()

# Traverse through Pastebin -> Get Solutions
# Luffy.GetSolutions()

# Loggin into Pbinfo
Luffy.LogIntoPbinfo()

# Configuring problem ID'S
# Luffy.GetProblemsIDS()

# Storing the data into json files for later uses
f = open("Problem_id.json")
ID = json.load(f)
f = open("A53_problem_names.json")
names = json.load(f)
f = open("Problem_name.json")
pb = json.load(f)
f = open("solutions.json")
solutionVector = json.load(f)

# Normalizing
for i in range(0, len(names) - 1):
    names[i] = names[i].lower()


lool = []
for i in pb:
    newPb = ""
    OK = 0
    for j in i:
        if j == '#':
            continue
        if j.isalpha():
            OK = 1
        if OK:
            newPb += j
    lool.append(newPb)
pb = lool
for i in range(0, len(pb) - 1):
    pb[i] = pb[i].lower()


# Uploading the Problems
Luffy.UploadProblems()

driver.quit()
