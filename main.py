import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService

# Chrome창 안보이게하기
options = webdriver.ChromeOptions()
options.add_argument("headless")

service = ChromService(executable_path="/.chromedriver")
driver = webdriver.Chrome(service=service, options=options)

#관악 아트홀
def gwanak():
    url = "https://www.gfac.or.kr/html/notify/notify1.html?sub=%EB%8C%80%EA%B4%80&keyword="

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        contents = soup.find("div", "notify1")
        wrap = contents.find("div", "wrap")
        table = wrap.find("table", "board-list")
        tbody = table.find("tbody")
        trList = tbody.find_all("tr")

        # 현재 게시물이 4개 밖에 없음
        if len(trList) > 4 :
            print("공고 떴다")
        else :
            print("아직 안떴다")

    except requests.exceptions.RequestException as e:
        print("Error Occured", e)


#인천문화예술회관
def incheon() :
    url = "https://www.incheon.go.kr/art/ART020101"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        art_wrapper = soup.find("div", "art wrapper")
        container = art_wrapper.find("div", "container")
        board_wrap = container.find("div", "board-wrap")
        board_data_list = board_wrap.find("div", "board-data-list board-has-sm-view")
        tbody = board_data_list.find("tbody")
        trList = tbody.find_all("tr")

        # 마지막 게시물이 35번 -> 새로운 게시물 번호는 36
        for tr in trList:
            number = tr.find_next("td")
            if number.text in "36":
                print("떴다")
                break

    except requests.exceptions.RequestException as e:
        print("Error Occured", e)

# 꿈의숲 (417 에러로 셀레니움 사용)
def dream_forest():
    url = "https://www.sejongpac.or.kr/portal/bbs/B0000002/list.do?menuNo=200012"

    try:
        driver.get(url)
        table_list = driver.find_element(By.CLASS_NAME, "bbs-list")
        tbody = table_list.find_element(By.TAG_NAME, "tbody")
        trList = tbody.find_elements(By.TAG_NAME, "tr")

        # 마지막 게시물이 409번 -> 새로운 게시물 번호는 410
        for tr in trList:
            number = tr.find_element(By.TAG_NAME, "td")
            if number.text in "410":
                print("떴다")
                break

    except requests.exceptions.RequestException as e:
        print("Error Occured", e)


#과천시민회관
def gwacheon():
    url = "https://www.gcart.or.kr/kr/commu/noticeList.do"

    try:
        driver.get(url)
        ul = driver.find_element(By.CLASS_NAME, "notice_list")
        li_list = ul.find_elements(By.TAG_NAME, "li")

        for li in li_list:
            if not li.text:
                continue
            name = li.find_element(By.CLASS_NAME, "name")
            if name.text in "대관":
                print(name.text)
                print("과천 시민회관 떴다")
                break


    except requests.exceptions.RequestException as e:
        print("Error Occured", e)




if __name__ == '__main__':
    gwanak()
    incheon()
    dream_forest()
    gwacheon()


