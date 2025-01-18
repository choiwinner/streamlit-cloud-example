import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Selenium 드라이버 설정
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Streamlit UI
st.title("Selenium을 이용한 웹 크롤링")
url = st.text_input("크롤링할 URL을 입력하세요:")

if st.button("크롤링 시작"):
    if url:
        with st.spinner("크롤링 중..."):
            driver = get_driver()
            driver.get(url)
            page_title = driver.title
            driver.quit()
        st.success(f"페이지 제목: {page_title}")
    else:
        st.error("URL을 입력하세요!")