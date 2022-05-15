import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def continue_after_req_limit(start_param):
    """
    :param start_param: request limitine takildigim icin bu parametre ile kaldigim yerden veriyi cekip kaydetmeye devam ettim
    :return:
    """

    # verileri cekmek icin firefox kullanilmistir, geckodriver dosyasi bu dosya ile ayni pathte yer almalidir
    f_options = Options()
    f_options.add_argument('--no-sandbox')
    f_options.add_argument('--disable-dev-shm-usage')
    driver_path = "geckodriver.exe"
    w = open("player_and_stats.txt","a",encoding="utf-8")
    browser = webdriver.Firefox(executable_path=driver_path,options=f_options)
    browser.implicitly_wait(4)

    j = 0
    # toplamda sitede 558 sayfa yer almaktadir
    for i in range(start_param,558):
        print(i)
        browser.get("https://pesdb.net/pes2022/" + "?page=" + str(i))
        if j == 0:
            # attributelarin secilmesi icin sitenin sol altinda yer alan settings panelinin otomatik olarak acilmasi
            settings_button_xpath = '// *[ @ id = "filters"] / div[2] / button'
            settings_button = browser.find_element_by_xpath(settings_button_xpath)
            browser.execute_script("arguments[0].click();", settings_button)

            # attributelarin checkbox iceren listedeki xpath idlerini ogeyi denetle secenegi ile bulup degiskenlere atadim
            # ulke ve kulup ismi hem preprocessi bozuyor hem de cok farkli sayida sample'a sahip, bu yuzden bunlar da otomatik olarak unticked olacak
            country_xpath = '//*[@id="col_club_team"]'
            nationality_xpath = '//*[@id="col_nationality"]'

            stronger_foot_xpath = '//*[@id="col_foot"]'
            ball_control_xpath = '//*[@id="col_ball_control"]'
            dribbling_xpath = '//*[@id="col_dribbling"]'
            low_pass_xpath = '//*[@id="col_low_pass"]'
            lofted_pass_xpath = '//*[@id="col_lofted_pass"]'
            finishing_path = '//*[@id="col_finishing"]'
            speed_xpath = '//*[@id="col_speed"]'
            kicking_power_xpath = '//*[@id="col_kicking_power"]'
            stamina_xpath = '//*[@id="col_stamina"]'
            tackling_xpath = '//*[@id="col_tackling"]'
            aggression_xpath = '//*[@id="col_aggression"]'
            def_eng_xpath = '//*[@id="col_defensive_engagement"]'
            wf_acc_xpath = '//*[@id="col_weak_foot_accuracy"]'

            # xpathler listeye atilir
            checkbox_xpath_list = [country_xpath, nationality_xpath,stronger_foot_xpath,ball_control_xpath,dribbling_xpath,low_pass_xpath,lofted_pass_xpath,def_eng_xpath,
                                   finishing_path,speed_xpath,kicking_power_xpath,stamina_xpath,tackling_xpath,aggression_xpath,wf_acc_xpath]

            # bu liste icinde iterate edilerek tabloya yansitilacak attributelar otomatik olarak isaretlenir
            for cb_xpath in checkbox_xpath_list:
                check_box = browser.find_element_by_xpath(cb_xpath)
                browser.execute_script("arguments[0].click();", check_box)

            # secili attributelar yansitmak icin apply butonuna otomatik olarak basilir
            apply_button_xpath = '//*[@id="popup0"]/div[3]/button'
            apply_button = browser.find_element_by_xpath(apply_button_xpath)
            browser.execute_script("arguments[0].click();", apply_button)

            # scriptin her calistirilmasinda ilk sayfadan sonra tekrardan secili attributelari isaretlemek gerekmez
            # j variable'i ile bu durum saglanir
            j += 1
            time.sleep(3)

            # yeni attributelarla olusmus tablo ve veriler selenium icindeki function ile string olarak alinir ve txt dosyasina yazilir
            table = browser.find_element_by_xpath('//*[@id="content"]/div[2]/table').text
            w.write(table + "\n")
            print(table)

        # yukarida da aciklandigi uzere script calistirildiktan sonraki ilk sayfa disinda gelen tum tablolar direkt txt dosyasina kaydedilir
        else:
            table = browser.find_element_by_xpath('//*[@id="content"]/div[2]/table').text
            w.write(table+"\n")

"""
100 kusur iterasyondan sonra sitenin request limitine takildigim icin kacinci iterasyonda hata aldigimi anlamak uzere i variable'ini yazdirdim
txt dosyasini da a flagi ile acmistim, request limiti yaklasik 1.5-2 dk icinde sifirlanmakta, toplamda 10-15 dkda her seferinde nereden kaldigimi belirten 
i parametresi ile functionu cagirdim ve tum datayi alt alta ekledim
"""
# continue_after_req_limit(1)
# continue_after_req_limit(118)
# continue_after_req_limit(236)
# continue_after_req_limit(353)
# continue_after_req_limit(470)