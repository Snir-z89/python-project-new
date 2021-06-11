from selenium import webdriver


def test_scores_service(url="http://127.0.0.1:5001/score"):
    driver = webdriver.Chrome(executable_path="/Users/snir.zack/Downloads/chromedriver")
    driver.get(url)
    get_score = driver.find_element_by_xpath('//*[@id="score"]')
    current_score = int(get_score.text)

    if 1 <= current_score <= 1000:
        return True
    else:
        return False


def main_function():
    test_scores_service()
    if test_scores_service(url="http://127.0.0.1:5001/score"):
        return 0
    else:
        return -1
