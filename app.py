import streamlit as st
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.by import By

#@st.cache_resource
def get_driver():


    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,   #like Gecko) Chrome/58.0.3029.110 Safari/537.3')

    return webdriver.Chrome(
                service=Service(
                    ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

#options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.
# (KHTML,   #like Gecko) Chrome/58.0.3029.110 Safari/537.3')

if __name__ == "__main__":

    #st.write('최재일')

    driver = get_driver()

    url = 'https://www.coupang.com/vp/products/7335597976?itemId=18741704367&vendorItemId=85873964906&  q=%ED%9E%98%EB%82%B4%EB%B0%94+%EC%B4%88%EC%BD%94+%EC%8A%A4%EB%8B%88%EC%BB%A4%EC%A6%88&itemsCount=36&  searchId=0c5c84d537bc41d1885266961d853179&rank=2&isAddedCart=:'

    # 쿠팡 상품 페이지 열기
    driver.get(url)

    # 페이지 로딩 대기(5초)
    time.sleep(10) 

    results = driver.find_elements(By.CLASS_NAME, "sdp-review__article__list__review__content")

    for element in results:
        st.write(element.text)
        #if count >=5:
        #    st.info(f'{count}의 Review가 성공적으로 검색되었습니다.')