from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import win32gui, win32con

tekst = ''
jezyk = 'pl'  #<-- choose your language

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })

driver = webdriver.Chrome(chrome_options=opt,executable_path='C:\\Users\\Pc\\OneDrive\\Pulpit\\chromedriver.exe')
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
driver.get('https://www.textfromtospeech.com/'+jezyk+'/voice-to-text/')

while True:
    try:
        ciasteczka = driver.find_element_by_xpath('/html/body/div[17]/div/div/div/p[2]/span/button[2]')
        ciasteczka.click()
        break
    except:
        pass
    time.sleep(0.5)

def zacznij_sluchac():
    sluchaj1 = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/a[1]')
    sluchaj1.click()

def przestan_sluchac():
    sluchaj2 = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/a[1]')
    sluchaj2.click()

def usun_tekst():
    usun = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/a[4]')
    usun.click()

def sprawdzenie():
    global tekst
    while True:
        try:
            try:
                tekst1 = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[2]/div/span').text)
                time.sleep(0.4)
                tekst2 = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[2]/div/span').text)
                time.sleep(0.4)
                tekst3 = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[2]/div/span').text)
                time.sleep(0.4)
            except:
                time.sleep(0.4)
                pass
            if tekst1 != '':
                if tekst1 == tekst2:
                    if tekst2 == tekst3:
                        tekst = tekst3
                        print(tekst)
                        usun_tekst()
        except:
            continue

zacznij_sluchac()
print("Słucham...")
while True:
    sprawdzenie()
