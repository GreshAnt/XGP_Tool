import pyperclip
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from random import randint
from time import sleep
import requests
from bs4 import BeautifulSoup
import warnings
from random import shuffle
import cryptography.fernet
import platform
import hashlib
import base64

warnings.filterwarnings('ignore')


def get_device_id():
    # 获取计算机的硬件设备号（UUID）
    device_uuid = platform.node()

    # 获取操作系统相关信息
    os_info = platform.system() + platform.release()

    # 组合设备标识信息
    combined_info = device_uuid + os_info

    # 使用MD5哈希算法生成设备识别码
    device_id = hashlib.md5(combined_info.encode()).hexdigest()

    return device_id


# 获取设备识别码
device_idx = get_device_id()


def decrypt_device_id(file_path, device_id_key):
    # 读取加密的设备识别码文件
    with open(file_path, "rb") as file:
        ciphertext = file.read()

    # 创建解密器对象
    cipher_suite = cryptography.fernet.Fernet(device_id_key)

    # 解密设备识别码
    plaintext = cipher_suite.decrypt(ciphertext)

    # 返回设备识别码的明文
    return plaintext.decode()


decrypted_device_id = None
decrypted_device_id2 = None
try:
    file_path = "C:\\Users\\Public\\" + 'device_id' + ".bin"
    device_id_key = base64.urlsafe_b64encode(hashlib.sha256(device_idx.encode()).digest())
    decrypted_device_id = decrypt_device_id(file_path, device_id_key)
except:
    pass

try:
    file_path2 = 'device_id.bin'
    device_id_key2 = base64.urlsafe_b64encode(hashlib.sha256(device_idx.encode()).digest())
    decrypted_device_id2 = decrypt_device_id(file_path2, device_id_key2)
except:
    pass

if decrypted_device_id is not None:
    print(f'Your hwid : {device_idx} , the session hwid : {decrypted_device_id}')
else:
    print(f'Your hwid : {device_idx} , the session hwid : {decrypted_device_id2}')

if (decrypted_device_id == device_idx) or (decrypted_device_id2 == device_idx):
    print('>设备识别码检测通过')
else:
    print('hwid错误!!')
    sleep(5)
    quit(0)


def retry(func):
    while True:
        try:
            func()
            break
        except:
            continue


class XGP:

    def __init__(self, email_raw, _password_, in_game_name):
        self.email_raw = email_raw
        self.password = _password_
        self.in_game_name = in_game_name

    def BuyXgp(self):
        while 1:
            qs = input('>请问这个账号有xbox名字吗？(y/n) \n>')
            if qs not in ['y', 'n']:
                print('>错误！')
            else:
                break
        out5 = '@hotmail.com'
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        options.use_chromium = True
        options.add_argument("--inprivate")  # 启用InPrivate模式
        driver_path = 'msedgedriver.exe'
        service = Service(driver_path)
        xbox2 = webdriver.Edge(service=service, options=options)
        xbox2.get('https://www.xbox.com/zh-HK/xbox-game-pass/pc-game-pass?xr=shellnav')
        print('>Open xbox website')
        # 检测登录
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#mectrl_headerPicture'))
        # 点击买XGP
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#topofpage > div > div > div.c-group.adjust.trailer > a').click())
        print('>Get XGP')
        # 输入邮箱
        retry(lambda: xbox2.find_element(By.ID, 'i0116').send_keys(self.email_raw + out5))
        print('>Type in email')
        sleep(0.6)
        # 下一步
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#idSIButton9').click())
        print('>Next')
        # 输入密码
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#i0118').send_keys(self.password))
        print('>Type in password')
        sleep(0.6)
        # 登录
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#idSIButton9').click())
        print('>Login')
        sleep(2)
        try:
            xbox2.find_element(By.CSS_SELECTOR, '#iShowSkip').click()
        except:
            pass
        # 不要保持登录
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#idBtn_Back').click())
        print('>Disagree')

        if qs == 'n':
            while 1:
                try:
                    xbox2.find_element(By.CSS_SELECTOR, '#create-account-gamertag-input').send_keys(self.in_game_name)
                    sleep(5)
                    xbox2.find_element(By.CSS_SELECTOR, '#inline-continue-control').click()
                    break
                except:
                    pass
        elif qs == 'y':
            pass
        print('>Set xbox in game name')
        # 他妈的下一步
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         'body > reach-portal > div:nth-child(3) > div > div > div > div > div > div '
                                         '> div'
                                         '> div > div > div > '
                                         'div.Container-module__container___YTczU.ContextualStoreProductDetailsPage'
                                         '-module__body___LV6g1 > '
                                         'div.ContextualStoreProductDetailsPage-module__upShiftContainers___1bo\+v'
                                         '.ContextualStoreProductDetailsPage-module__multipleButtonContainer___DN-ZY '
                                         '> div'
                                         '> div.Column-module__col6___keGm9.ContextualStoreProductDetailsPage'
                                         '-module__paddingLeft0___gaLHu.ContextualStoreProductDetailsPage'
                                         '-module__paddingRight0___gAqxV').click())
        print('>Next')
        # 开始 新增付款方式
        xbox2.switch_to.frame('purchase-sdk-hosted-iframe')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#store-cart-root > div > div > div.focusLapContainer--xSS0YN8I > div > '
                                         'div.buyNowDetailsFlex---gyRdxKV > '
                                         'div.selectedPaymentOptionContainer--Aljd0H0A >'
                                         'button > i').click())
        print('>Get new pay')
        # ewallet
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#displayId_ewallet').click())
        print('>Select to ewallet')
        # alipay
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#displayId_ewallet_alipay_billing_agreement').click())
        print('>Select to alipay')
        # Next
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#pidlddc-button-saveNextButton').click())
        print('>Next')
        print('>Please scan the QR code')

        # 输入地址
        while 1:
            try:
                xbox2.find_element(By.CSS_SELECTOR, '#city').send_keys('SB')
                xbox2.find_element(By.CSS_SELECTOR, '#address_line1').send_keys('SB')
                xbox2.find_element(By.CSS_SELECTOR, '#pidlddc-button-saveButton').click()
                break
            except:
                pass
        print('>Type in address')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#store-cart-root > div > div > div.focusLapContainer--xSS0YN8I > div > div.buyNowDetailsFlex---gyRdxKV > div.selectedPaymentOptionContainer--Aljd0H0A > button > div > div.paymentOptionLink--3xO8r326.undefined > span'))
        xbox2.find_element(By.CSS_SELECTOR,
                           '#store-cart-root > div > div > div.focusLapContainer--xSS0YN8I > div > div.buttonGroup--6c-lZSe3 > button.primary--DXmYtnzQ.base--kY64RzQE').click()
        print('>Pay')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         'body > reach-portal > div:nth-child(3) > div > div > div > div > div > div > div > div > div > div > div.ThankYouPage-module__actionContainer___YBSpg > a'))
        print(f"email: {self.email_raw + out5} , password: {self.password} , name : {self.in_game_name}")
        pyperclip.copy(f"email: {self.email_raw + out5} , password: {self.password} , name : {self.in_game_name}")
        print('>已经粘贴到剪贴板')
        xbox2.close()
        xbox2.quit()

    def IGN(self):
        out2 = '@hotmail.com'
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        options.use_chromium = True
        options.add_argument("--inprivate")  # 启用InPrivate模式
        driver_path = 'msedgedriver.exe'
        service = Service(driver_path)
        minecraft = webdriver.Edge(service=service, options=options)
        minecraft.get('https://www.minecraft.net/')
        print('>Open minecraft website')
        retry(lambda: minecraft.find_element(By.CSS_SELECTOR,
                                             '#mc-globalhead__primaryheader > div.mc-globalbanner > nav > ul > li.mc-globalhead__nav-login > a').click())
        retry(lambda: minecraft.find_element(By.CSS_SELECTOR,
                                             '#main-content > div.page-section.page-section--first.site-content--hide-footer.bg-img-height.bg-globe.d-flex.align-items-center > div > div > div > div.bg-white.py-4 > div:nth-child(1) > div.my-3 > a').click())
        print('>Login in')
        retry(lambda: minecraft.find_element(By.CSS_SELECTOR, '#i0116').send_keys(self.email_raw + out2))
        print('>Type in email')
        sleep(0.6)
        retry(lambda: minecraft.find_element(By.CSS_SELECTOR, '#idSIButton9').click())
        print('>Next')

        retry(lambda: minecraft.find_element(By.CSS_SELECTOR, '#i0118').send_keys(self.password))
        print('>Type in password')
        sleep(0.6)
        retry(lambda: minecraft.find_element(By.CSS_SELECTOR, '#idSIButton9').click())
        print('>Login')
        retry(lambda: minecraft.find_element(By.CSS_SELECTOR, '#idBtn_Back').click())

        retry(lambda: minecraft.find_element(By.CSS_SELECTOR,
                                             '#main-content > section > div > div.my-games-wrapper.mx-auto > div.my-games-container > div:nth-child(1) > div > div.games-card__text > div > div > a:nth-child(2) > div').click())
        print('>Go to change the profile')
        retry(lambda: minecraft.find_element(By.CSS_SELECTOR, '#profileNameLabel > input').send_keys(self.in_game_name))
        retry(lambda: minecraft.find_element(By.CSS_SELECTOR,
                                             '#main-content > section > div > div > section > div.card-view__container > form > div > div.redeem__button-align > button').click())
        print('>Profile changed, every thing is down')
        sleep(3)
        print(f"email: {self.email_raw + out2} , password: {self.password} , name : {self.in_game_name}")
        pyperclip.copy(f"email: {self.email_raw + out2} , password: {self.password} , name : {self.in_game_name}")
        print('>已经粘贴到剪贴板')
        minecraft.close()
        minecraft.quit()

    def refund(self):
        out3 = '@hotmail.com'
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        options.use_chromium = True
        options.add_argument("--inprivate")  # 启用InPrivate模式
        driver_path = 'msedgedriver.exe'
        service = Service(driver_path)
        refund = webdriver.Edge(service=service, options=options)
        refund.get('https://www.microsoft.com/zh-cn/')
        retry(lambda: refund.find_element(By.CSS_SELECTOR, '#mectrl_headerPicture').click())
        print('>Login in')
        retry(lambda: refund.find_element(By.CSS_SELECTOR, '#i0116').send_keys(self.email_raw + out3))
        print('>Type in email')
        sleep(0.6)
        retry(lambda: refund.find_element(By.CSS_SELECTOR, '#idSIButton9').click())
        print('>Next')

        retry(lambda: refund.find_element(By.CSS_SELECTOR, '#i0118').send_keys(self.password))
        print('>Type in password')
        sleep(0.6)
        retry(lambda: refund.find_element(By.CSS_SELECTOR, '#idSIButton9').click())
        print('>Login')
        try:
            refund.find_element(By.CSS_SELECTOR, '#iShowSkip').click()
        except:
            pass
        retry(lambda: refund.find_element(By.CSS_SELECTOR, '#idBtn_Back').click())
        print('>Disagree')

        refund.get('https://account.microsoft.com/services/pcgamepass/cancel?fref=billing-cancel')
        while 1:
            try:
                refund.find_element(By.CSS_SELECTOR, '#StickyFooter > button > span').click()
                print('>Continue')
                break
            except:
                pass
            retry(lambda: refund.find_element(By.CSS_SELECTOR, '#StickyFooter > button').click())
            print('>Continue')
        retry(lambda: refund.find_element(By.CSS_SELECTOR, '#benefit-cancel').click())

        idd = 0
        while True:
            try:
                wid = 'ChoiceGroup' + str(idd) + '-cancel-now'
                refund.find_element(By.ID, wid).click()
                break
            except:
                idd = idd + 1
                continue

        print('>Refund...')
        refund.find_element(By.CSS_SELECTOR, '#cancel-select-cancel').click()
        print('>Refund successful! Every thing is down')
        print(f"email: {self.email_raw + out3} , password: {self.password} , name : {self.in_game_name}")
        pyperclip.copy(f"email: {self.email_raw + out3} , password: {self.password} , name : {self.in_game_name}")
        print('>已经粘贴到剪贴板')
        sleep(1)
        refund.close()
        refund.quit()


class UniqueSkill(XGP):
    def __init__(self, email_raw, _password_, in_game_name):
        super().__init__(email_raw, _password_, in_game_name)

    @staticmethod
    def randomIGN():
        base_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        random_str = ''
        for i in range(3):
            random_str += base_str[randint(0, (len(base_str) - 1))]
        num = str(randint(0, 999))
        return 'Gre' + random_str + num


def randomIGN2():
    base_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    random_str = ''
    for i in range(5):
        random_str += base_str[randint(0, (len(base_str) - 1))]
    num = str(randint(0, 999))
    return 'Gre' + random_str + num


logo = '''   ______                          __      ___            __
  / ____/   _____  ___    _____   / /_    /   |   ____   / /_
 / / __    / ___/ / _ \  / ___/  / __ \  / /| |  / __ \ / __/
/ /_/ /   / /    /  __/ (__  )  / / / / / ___ | / / / // /_
\____/   /_/     \___/ /____/  /_/ /_/ /_/  |_|/_/ /_/ \__/
                                                             '''


def email():
    # 定义目标网页的 URL
    email_api = [
        'Your email api here',
        'Your email api here']
    shuffle(email_api)
    url = email_api[0]

    # 发送 HTTPS 请求并获取网页内容，禁用 SSL 证书验证
    response = requests.get(url, verify=False)
    html_content = response.text

    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取字符串
    string = soup.get_text()

    # 打印提取到的字符串
    string = string.split('----')

    return string


e = 'e'
p = 'p'
result = 'result'


def remove_suffix(string, suffixx):
    if string.endswith(suffixx):
        return string[:len(string) - len(suffixx)]
    else:
        return string


def c():
    global e
    global p
    global result
    eap = email()
    e = eap[0]
    p = eap[1]
    suffix = "@hotmail.com"
    result = remove_suffix(e, suffix)


open('account.txt', 'a')


def AccountSave(account):
    f = open('account.txt', 'a')
    f.write(account + '\n')
    f.close()


def whiletrue():
    alipayps = input('>你的支付宝支付密码:')
    out5 = '@hotmail.com'
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    options.use_chromium = True
    options.add_argument("--inprivate")  # 启用InPrivate模式
    driver_path = 'msedgedriver.exe'
    service = Service(driver_path)
    xbox2 = webdriver.Edge(service=service, options=options)

    xbox2.get('https://auth.alipay.com/login/index.htm?goto=https%3A%2F%2Fwww.alipay.com%2F')
    print('Please scan the QR code')
    retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                     'body > div > div.container > div.content > div > div.mid > div > a.merchant-login > span'))
    first = True
    while 1:
        c()
        name = randomIGN2()
        emailin = result
        passwordin = p
        print(f"email: {emailin + out5} , password: {passwordin} , name : {name}")
        AccountSave(f"email: {emailin + out5} , password: {passwordin} , name : {name}")
        print('>已经写入文件')
        xbox2.get('https://www.xbox.com/zh-HK/xbox-game-pass/pc-game-pass?xr=shellnav')
        print('>Open xbox website')
        # 检测登录
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#mectrl_headerPicture'))
        if not first:
            retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#mectrl_headerPicture').click())
            retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#mectrl_body_signOut').click())
            xbox2.get('https://www.xbox.com/zh-HK/xbox-game-pass/pc-game-pass?xr=shellnav')
        # 点击买XGP
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#topofpage > div > div > div.c-group.adjust.trailer > a').click())
        print('>Get XGP')
        # 输入邮箱
        retry(lambda: xbox2.find_element(By.ID, 'i0116').send_keys(emailin + out5))
        print('>Type in email')
        sleep(0.6)
        # 下一步
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#idSIButton9').click())
        print('>Next')
        # 输入密码
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#i0118').send_keys(passwordin))
        print('>Type in password')
        sleep(0.6)
        # 登录
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#idSIButton9').click())
        print('>Login')
        sleep(2)
        try:
            xbox2.find_element(By.CSS_SELECTOR, '#iShowSkip').click()
        except:
            pass
        # 不要保持登录
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#idBtn_Back').click())
        print('>Disagree')

        while 1:
            try:
                xbox2.find_element(By.CSS_SELECTOR, '#create-account-gamertag-input').send_keys(randomIGN2())
                sleep(5)
                xbox2.find_element(By.CSS_SELECTOR, '#inline-continue-control').click()
                break
            except:
                pass
        print('>Set xbox in game name')

        xbox2.get('https://www.xbox.com/zh-HK/xbox-game-pass/pc-game-pass?xr=shellnav')
        print('>Open xbox website')
        # 检测登录
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#mectrl_headerPicture'))
        sleep(5)
        # 点击买XGP
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#topofpage > div > div > div.c-group.adjust.trailer > a').click())
        print('>Get XGP')
        # 他妈的下一步
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         'body > reach-portal > div:nth-child(3) > div > div > div > div > div > div '
                                         '> div'
                                         '> div > div > div > '
                                         'div.Container-module__container___YTczU.ContextualStoreProductDetailsPage'
                                         '-module__body___LV6g1 > '
                                         'div.ContextualStoreProductDetailsPage-module__upShiftContainers___1bo\+v'
                                         '.ContextualStoreProductDetailsPage-module__multipleButtonContainer___DN-ZY '
                                         '> div'
                                         '> div.Column-module__col6___keGm9.ContextualStoreProductDetailsPage'
                                         '-module__paddingLeft0___gaLHu.ContextualStoreProductDetailsPage'
                                         '-module__paddingRight0___gAqxV').click())
        print('>Next')
        # 开始 新增付款方式
        xbox2.switch_to.frame('purchase-sdk-hosted-iframe')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#store-cart-root > div > div > div.focusLapContainer--xSS0YN8I > div > '
                                         'div.buyNowDetailsFlex---gyRdxKV > '
                                         'div.selectedPaymentOptionContainer--Aljd0H0A >'
                                         'button > i').click())
        print('>Get new pay')
        # ewallet
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#displayId_ewallet').click())
        print('>Select to ewallet')
        # alipay
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#displayId_ewallet_alipay_billing_agreement').click())
        print('>Select to alipay')
        # Next
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#pidlddc-button-saveNextButton').click())
        print('>Next')
        retry(lambda: xbox2.find_element(By.ID, 'pidlddc-hyperlink-alipayQrCodeChallengeRedirectionLink').click())
        for window_handle in xbox2.window_handles:
            xbox2.switch_to.window(window_handle)
            if '签约' in xbox2.title:
                break
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#payPassword_rsainput').send_keys(alipayps))
        sleep(0.6)
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#J_submit').click())
        sleep(5)
        for window_handle in xbox2.window_handles:
            xbox2.switch_to.window(window_handle)
            if 'Xbox' in xbox2.title:
                break
        sleep(5)
        xbox2.switch_to.frame('purchase-sdk-hosted-iframe')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#pidlddc-button-alipayContinueButton').click())
        # 输入地址
        while 1:
            try:
                xbox2.find_element(By.CSS_SELECTOR, '#city').send_keys('SB')
                xbox2.find_element(By.CSS_SELECTOR, '#address_line1').send_keys('SB')
                xbox2.find_element(By.CSS_SELECTOR, '#pidlddc-button-saveButton').click()
                break
            except:
                pass
        print('>Type in address')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#store-cart-root > div > div > div.focusLapContainer--xSS0YN8I > div > div.buyNowDetailsFlex---gyRdxKV > div.selectedPaymentOptionContainer--Aljd0H0A > button > div > div.paymentOptionLink--3xO8r326.undefined > span'))
        xbox2.find_element(By.CSS_SELECTOR,
                           '#store-cart-root > div > div > div.focusLapContainer--xSS0YN8I > div > div.buttonGroup--6c-lZSe3 > button.primary--DXmYtnzQ.base--kY64RzQE').click()
        print('>Pay')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         'body > reach-portal > div:nth-child(3) > div > div > div > div > div > div > div > div > div > div > div.ThankYouPage-module__actionContainer___YBSpg > a'))

        xbox2.get('https://www.minecraft.net/')
        print('>Open minecraft website')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#mc-globalhead__primaryheader > div.mc-globalbanner > nav > ul > li.mc-globalhead__nav-login > a').click())
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#main-content > div.page-section.page-section--first.site-content--hide-footer.bg-img-height.bg-globe.d-flex.align-items-center > div > div > div > div.bg-white.py-4 > div:nth-child(1) > div.my-3 > a').click())
        print('>Login in')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#main-content > section > div > div.my-games-wrapper.mx-auto > div.my-games-container > div:nth-child(1) > div > div.games-card__text > div > div > a:nth-child(2) > div').click())
        print('>Go to change the profile')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#profileNameLabel > input').send_keys(name))
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR,
                                         '#main-content > section > div > div > section > div.card-view__container > form > div > div.redeem__button-align > button').click())
        print('>Profile changed.')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#mc-globalhead__nav-login-button-1 > span').click())
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#mc-globalhead__nav-login-dropdown-1 > li:nth-child(2) > a').click())
        sleep(10)

        xbox2.get('https://www.microsoft.com/zh-cn/')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#mectrl_headerPicture').click())
        print('>Login in')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#i0116').send_keys(emailin + out5))
        print('>Type in email')
        sleep(0.6)
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#idSIButton9').click())
        print('>Next')

        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#i0118').send_keys(passwordin))
        print('>Type in password')
        sleep(0.6)
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#idSIButton9').click())
        print('>Login')
        try:
            xbox2.find_element(By.CSS_SELECTOR, '#iShowSkip').click()
        except:
            pass
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#idBtn_Back').click())
        print('>Disagree')
        xbox2.get('https://account.microsoft.com/services/pcgamepass/cancel?fref=billing-cancel')
        while 1:
            try:
                xbox2.find_element(By.CSS_SELECTOR, '#StickyFooter > button > span').click()
                print('>Continue')
                break
            except:
                pass
            retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#StickyFooter > button').click())
            print('>Continue')
        retry(lambda: xbox2.find_element(By.CSS_SELECTOR, '#benefit-cancel').click())

        idd = 0
        while True:
            try:
                wid = 'ChoiceGroup' + str(idd) + '-cancel-now'
                xbox2.find_element(By.ID, wid).click()
                break
            except:
                idd = idd + 1
                continue

        print('>refund..')
        xbox2.find_element(By.CSS_SELECTOR, '#cancel-select-cancel').click()
        sleep(5)
        print('>Refund successful! ')

        xbox2.get('https://www.microsoft.com/rpsauth/v1/account/SignOut?ru=https%3A%2F%2Fwww.microsoft.com%2Fzh-hk%2F')
        retry(lambda: xbox2.find_element(By.ID, 'shellmenu_0'))
        sleep(2)
        print(f"email: {emailin + out5} , password: {passwordin} , name : {name}")
        pyperclip.copy(f"email: {emailin + out5} , password: {passwordin} , name : {name}")
        print('>已经粘贴到剪贴板')
        sleep(1)

        stop = input('>要停止请输入stop或者q，其它都是继续:')
        if (stop == 'stop') or (stop == 'q'):
            break
        else:
            first = False


if __name__ == "__main__":
    print(logo)
    print('>本程序支持注册账号+购买XGP+设置名字+退款全套操作')
    print('>请先看“看我.txt”！')
    print('>本程序所有代码均由GreshAnt编写!!!')
    while 1:
        if 1 == 1:
            c()
            server = str(input(
                '>你想要什么服务？ 输入stop退出\n 1.购买+设置名字+退款\n 2.购买\n 3.设置名字\n 4.退款 \n 5.超级循环\n>'))
            if server == '1':
                server1 = UniqueSkill(None, None, None)
                xgpemail = result
                xgppassword = p
                xgpign = server1.randomIGN()
                print(f'email : {xgpemail}@hotmail.com ; password : {xgppassword} ; name : {xgpign}')
                server1 = UniqueSkill(xgpemail, xgppassword, xgpign)
                server1.BuyXgp()
                server1.IGN()
                server1.refund()
                break
            elif server == '2':
                xgpemail = input('输入你的邮箱前缀>')
                xgppassword = input('请输入你的密码>')
                server2 = UniqueSkill(None, None, None)
                xgpign = server2.randomIGN()
                server2 = UniqueSkill(xgpemail, xgppassword, xgpign)
                server2.BuyXgp()
                break
            elif server == '3':
                server3 = UniqueSkill(None, None, None)
                xgpemail = input('输入你的邮箱前缀>')
                xgppassword = input('请输入你的密码>')
                xgpign = server3.randomIGN()
                server3 = UniqueSkill(xgpemail, xgppassword, xgpign)
                server3.IGN()
                break
            elif server == '4':
                xgpemail = input('输入你的邮箱前缀>')
                xgppassword = input('请输入你的密码>')
                xgpign = None
                server4 = UniqueSkill(xgpemail, xgppassword, xgpign)
                server4.refund()
                break
            elif server == '5':
                whiletrue()
            elif server == 'stop':
                break
            else:
                print('>键入的字符错误！')
                continue
