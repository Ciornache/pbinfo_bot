from hashlib import pbkdf2_hmac
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(
    executable_path="chromedriver.exe")
driver.get("https://pastebin.com/u/a53")
index, pageButton, cnt, solutionVectorm, ID, Index, page = 1, 2, 1, [], [], 3, 2


class PbinfoBot:
    global Id, Index

    def GetSolutions():
        global cnt, index, pageButton, solutionVector
        while cnt <= 20:
            print(index)
            sleep(3)
            problemName = driver.find_element(
                By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[{}]/td[1]/a'.format(index))
            if problemName.text == 'CPPREFERANCE':
                index = index + 1
                continue
            problemName.click()
            if index == 1:
                sleep(10)
            if index == 1:
                agreeButton = driver.find_element(
                    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]')
                agreeButton.click()
                print("USopp")
                sleep(3)
            correctOL = 1
            if index == 1:
                correctOL = 2
            print(correctOL)
            solution = driver.find_element(
                By.XPATH, '/html/body/div[{}]/div[2]/div[1]/div[2]/div[4]/div[2]/ol'.format(correctOL))
            solutionVector.append(solution.text)
            index = index + 1
            if index > 100:
                index = index - 100
                driver.find_element(
                    By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[102]/div/a[{}]'.format(pageButton))
                cnt = cnt + 1
                pageButton += 1
                if pageButton > 6:
                    pageButton -= 1
            driver.get("https://pastebin.com/u/a53")

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
        driver.find_element(
            By.XPATH, '/html/body/div[2]/div[6]/div/div[4]/div[1]/div[2]/form/div/div[2]/div[4]/button').click()

    def GetProblemsIDS():
        driver.get("https://www.pbinfo.ro/probleme")
        id = driver.find_element(
            By.XPATH, '/html/body/div[3]/div[5]/div/div[5]/div[2]/div[{}]/div[1]/h3/code').format(Index)
        name = driver.find_element(
            By.XPATH, '/html/body/div[2]/div[4]/div/div[5]/div[2]/div[{}]/div[1]/h3/a[1]').format(Index)
        ID.append(id.text, name.text)
        Index = Index + 1
        if Index == 13:
            Index = 3
            page += 1
            if page > 9:
                page -= 1
        if page <= 3:
            driver.find_element(
                By.XPATH, '/html/body/div[3]/div[4]/div/div[5]/div[2]/div[14]/nav/ul/li[{}]/a'.format(page)).click()
        else:
            driver.find_element(
                By.XPATH, '/html/body/div[2]/div[4]/div/div[5]/div[2]/div[13]/nav/ul/li[{}]/a'.format(page)).click()


PbinfoBot.LogIntoPbinfo()
PbinfoBot.GetProblemsIDS()
