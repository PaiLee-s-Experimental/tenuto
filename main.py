import requests
from bs4 import BeautifulSoup



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

        for tr in trList:
            tr_parsed = BeautifulSoup(tr.text, "html.parser")
            print(tr_parsed.text)

    except requests.exceptions.RequestException as e:
        print("Error Occured", e)


if __name__ == '__main__':
    gwanak()
    incheon()