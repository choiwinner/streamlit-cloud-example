import streamlit as st
import time
from bs4 import BeautifulSoup as bs

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    options = Options()
    options.add_argument("--disable-gpu")
    #options.add_argument("--headless")
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,   #like Gecko) Chrome/58.0.3029.110 Safari/537.3')

    driver = get_driver()
    driver.get("https://www.naver.com/")

    st.code(driver.page_source)

    # 쿠팡 상품 페이지 열기
    #driver.get(URL)

    # 페이지 로딩 대기(5초)
    time.sleep(5) 
    
    # bs4로 리뷰 찾기
    #html = driver.page_source
    #soup = bs(html, 'html.parser')
    #
    #result = soup.select('#sform > fieldset > div')
#
    #count = len(result) #review 개수 확인
#
    #st.write(result)
#
    #if count >=5:
    #    st.info(f'{count}의 Review가 성공적으로 검색되었습니다.')