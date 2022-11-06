from asyncio.windows_events import NULL
import email
from email.parser import BytesParser
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
import asyncio
import threading
driver = webdriver.Chrome(
    executable_path="chromedriver.exe")
index, pageButton, cnt, solutionVector, ID, Index, page = 1, 1, 1, [], [], 3, 1
pb, names = [], []
inter = 0
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)


def swap(self, a, b):
    crt = self.a
    self.a = self.b
    self.b = self.crt


def Good(a):
    yes = ''
    for j in a:
        if j != '#':
            yes += j
    return yes


action = ActionChains(driver)

# DIALOGUE

#--------------------------------------------------------------------#
print("\n\n\n\n\n")
print("Welcome to the Official Unofficial very legal and non-controversial pbinfo bot made by the Future Pirate King Monkey D Luffy!!!!!!\n")
print("You want flex and drip, get all the girls and make the grannies around you wet as hell, then you are in the right place. With the help of this fantastic bot, you are gonna be top 1 in the pbinfo leaderboard\n\n\n")
print("##### Instructions!!!!! #####\n\n")
print("You may leave this bot AFK for severeal hours to do it's job. After you enter your credentials, place your mouse on the middle of the screen( or anywhere else but not the corners) \n")
print("This bot uses a software that takes control of your mouse and uses it to simulate the activity of a real human( a very good problem solver as well ) \n")
print("Enter your credential down below:\n\n")
print("Use this commands for easier times\n")
print("cd 1 for Typing pbinfo username \n")
print("cd 2 for Typing pbinfo password \n")
print("cd 3 for Typing solinfo username \n")
print("cd 4 for Typing solinfo password \n")
print("ready to start \n")
#--------------------------------------------------------------------#

# TAKING INPUT
#------------------------------------------#

while 1:
    print("Waiting for Command\n")
    command = input()
    if command == "cd 1":
        username = input("Enter your pbinfo username: \n")
    if command == "cd 2":
        password = input("Enter your password: \n")
    if command == "cd 3":
        solinfoUsername = input(
            "Enter your email for solinfo authentification: \n")
    if command == "cd 4":
        solinfoPassword = input("Enter your solinfo password: \n")
    if command == "ready":
        break

#-----------------------------------------#


class PbinfoBot:
    def __init__(self):
        driver.maximize_window()

    def EntartainUser(self):
        while 1:  # TO DO
            print("Hello nakama!!!\n")

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

    def StrictUploading(self, id):
        driver.get("https://www.pbinfo.ro/probleme/{}".format(Good(id)))
        pyautogui.moveTo(600, 700, duration=2)
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
        sleep(30)

    def FormatTitle(self, title):
        good = ''
        for i in range(0, len(title)):
            if title[i] == ' ' or title[i] == '_':
                good += '-'
            else:
                good += title[i]
        return good

    def UploadProblems(self):
        f = open("work.json")
        index = json.load(f)
        # print(index)
        for i in range(index, len(pb)):
            self.CreateJson(i, "work.json")
            driver.get("https://www.pbinfo.ro/probleme/{}".format(Good(ID[i])))
            WebDriverWait(driver, 30).until(EC.visibility_of((driver.find_element(
                By.XPATH, "//*[@id={}]/a".format("'meniu-problema-enunt'")))))
            actualScore = driver.find_element(
                By.XPATH, "//*[@id='zona-mijloc']/div/table/tbody/tr[2]/td[9]/div")
            if actualScore.text == "100":
                continue
            solution = ""
            sleep(1)
            left, right = 0, len(names) - 1
            while left <= right:
                mid = (left + right) >> 1
                if names[mid] == pb[i]:
                    solution = solutionVector[mid - 1]
                    break
                if names[mid] < pb[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            if solution == "":
                self.GoToSolinfo(self.FormatTitle(pb[i]), ID[i])
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
            self.StrictUploading(ID[i])

    def CreateJson(self, data, name):
        with open(name, 'w') as i:
            json.dump(data, i, indent=0)

    def LogIntoPbinfo(self):
        t = threading.Thread(target=self.EntartainUser)
        t.start()
        global password, username
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
        utilizator.send_keys(username)
        parola.send_keys(password)
        autButton = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/form/div[3]/div[1]/div/button[2]")
        autButton.click()
        self.Wait(driver.find_element(By.CLASS_NAME, "dropdown-toggle"))

    def LogIntoSolinfo(self, emaiL_adress, password):
        driver.get("https://solinfo.ro/")
        sleep(5)
        driver.find_element(
            By.XPATH, "//*[@id='_solinfo']/div[2]/div[1]/header/div/div[3]/button").click()
        driver.find_element(
            By.XPATH, "//*[@id='primary-menu']/div[3]/ul/a[1]/li/span[1]").click()
        sleep(2)
        driver.find_element(
            By.XPATH, "//*[@id='emailAddress']").send_keys(emaiL_adress)
        driver.find_element(
            By.XPATH, "//*[@id='_solinfo']/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div[2]/div/button").click()
        while 1:
            try:
                WebDriverWait(driver, 30).until(EC.visibility_of(
                    (driver.find_element(By.XPATH, "//*[@id='password']"))))
                break
            except:
                continue
        driver.find_element(
            By.XPATH, "//*[@id='password']").send_keys(password)
        driver.find_element(
            By.XPATH, "//*[@id='_solinfo']/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div[3]/div/button").click()
        sleep(5)

    def Wait(self, element):
        contor = 0
        while 1:
            contor += 1
            if contor > 1000:
                break
            # print("loop")
            try:
                driver.find_element(By.XPATH, element)
                break
            except:
                continue
        # print("yes")
        contor = 0
        while 1:
            # print("no")
            contor += 1
            if contor > 100:
                break
            try:
                driver.find_element(By.XPATH, element).click()
                break
            except:
                pass

    def GoToSolinfo(self, name, id):
        global inter, solinfoUsername, solinfoPassword
        inter += 1
        # print(inter)
        if inter == 1:
            self.LogIntoSolinfo(solinfoUsername, solinfoPassword)
        driver.get("https://solinfo.ro/problema/{}".format(name))
        WebDriverWait(driver, 30).until(EC.visibility_of(
            (driver.find_element(By.XPATH, "//*[@id='_solinfo']/div[2]/div[1]/header/div"))))
        try:
            sleep(5)
            WebDriverWait(driver, 30).until(EC.visibility_of((driver.find_element(
                By.XPATH, "//*[@id='_solinfo']/div[2]/div[3]/div/div/div/img"))))
            return
        except:
            pass
        form = driver.find_element(
            By.XPATH, "//*[@id='_solinfo']/div[2]/div[3]/div/div/div[3]/div/div[4]/div/div[1]/div[1]")
        form.click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((driver.find_element(
            By.XPATH, "//*[@id='_solinfo']/div[2]/div[3]/div/div/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/button"))))
        driver.find_element(
            By.XPATH, "//*[@id='_solinfo']/div[2]/div[3]/div/div/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/button").click()
        sleep(5)
        driver.find_element(
            By.XPATH, "//*[@id='_solinfo']/div[2]/div[3]/div/div/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/span[1]").click()
        self.StrictUploading(id)

    def IhateAdds(self):
        self.kill()


# Initializing Bot
Luffy = PbinfoBot()

# Traverse through Pastebin -> Get Solutions
# Luffy.GetSolutions()

# Logging into Pbinfo
Luffy.LogIntoPbinfo()

# Configuring problem ID'S
# Luffy.GetProblemsIDS()

# Getting the data from the JSON FILES
f = open("Problem_id.json")
ID = json.load(f)
f = open("A53_problem_names.json")
names = json.load(f)
f = open("Problem_name.json")
pb = json.load(f)
f = open("solutions.json")
solutionVector = json.load(f)


# Normalizing
for i in range(0, len(names)):
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
for i in range(0, len(pb)):
    pb[i] = pb[i].lower()

# Sorting the Problems for optimization

for i in range(0, len(names) - 1):
    for j in range(i + 1, len(names)):
        if names[i] > names[j]:
            names[i], names[j] = names[j], names[i]
            solutionVector[i - 1], solutionVector[j -
                                                  1] = solutionVector[j - 1], solutionVector[i - 1]

# Uploading the Problems
Luffy.UploadProblems()

# End Of Line
driver.quit()
