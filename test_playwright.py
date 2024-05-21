from playwright.sync_api import sync_playwright

p = sync_playwright().start()

# browser = p.chromium.launch()
browser = p.chromium.launch(headless=False)  # # 웹페이지 보기 옵션

page = browser.new_page()

page.goto("https://google.com")
page.screenshot(path="./screenshots/screenshot.png")
