import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Конфигурационные данные (ЗАПОЛНИТЕ СВОИ ДАННЫЕ!)
STEAM_LOGIN = "ВАШ_ЛОГИН"
STEAM_PASSWORD = "ВАШ_ПАРОЛЬ"
FRIEND_LINK = "ССЫЛКА_НА_ПРОФИЛЬ_ДРУГА (s.team)"
GAME_URL = "ССЫЛКА_НА_ИГРУ"

# Оригинальные XPath элементы
LOGIN_INPUT_XPATH = '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[1]/input'
PASSWORD_INPUT_XPATH = '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input'
FRIEND_NAME_XPATH = '//*[@id="responsive_page_template_content"]/div[2]/div[2]/div/div/div/div[1]/div[1]/span[1]'
ADD_TO_CART_XPATH = '//*[@id="btn_add_to_cart_827941"]'
CHECKOUT_STEPS = [
    '/html/body/div[3]/dialog/div/div[2]/div/div[3]/div/div[2]/div/div/div/div[2]/div[5]/div[1]/div/button',
    '/html/body/div[3]/dialog/div[3]/div/button[3]',
    '/html/body/div[3]/dialog/div/div[2]/div/div[3]/div/div[3]/button[2]',
    '//*[@id="page_root"]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/button',
    '//*[@id="page_root"]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div/div/div[2]/div/button'
]
FRIEND_INPUT_XPATH = '/html/body/div[3]/dialog/div/div[2]/div/div[3]/div/div/div[2]/input'
FRIEND_CONFIRM_XPATH = '/html/body/div[3]/dialog/div/div[2]/div/div[3]/div/div/div[3]'
FINAL_BUTTON_XPATH = '//*[@id="page_root"]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/button'
SSA_CHECKBOX_XPATH = '//*[@id="accept_ssa"]'
PURCHASE_BUTTON_XPATH = '//*[@id="purchase_button_bottom"]'

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        print("🔐 Начало авторизации...")
        driver.get("https://store.steampowered.com/login/")
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, LOGIN_INPUT_XPATH))
        ).send_keys(STEAM_LOGIN)
        
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, PASSWORD_INPUT_XPATH))
        )
        password_field.send_keys(STEAM_PASSWORD)
        password_field.send_keys(Keys.RETURN)
        
        print("⏳ Ожидание 5 секунд для ручного ввода 2FA... (если имеентся)")
        time.sleep(5)

        print("👥 Переход к профилю друга...")
        driver.get(FRIEND_LINK)
        
        friend_name = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, FRIEND_NAME_XPATH))
        ).text
        print(f"✅ Найдено имя друга: {friend_name}")

        print("🎮 Переход на страницу игры...")
        driver.get(GAME_URL)
        
        WebDriverWait(driver, 30).until(
            lambda d: d.current_url == GAME_URL
        )
        print("✔️ Страница игры успешно загружена")

        print("🛒 Добавление игры в корзину...")
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, ADD_TO_CART_XPATH))
        ).click()

        print("🚀 Начало оформления заказа...")
        for index, step in enumerate(CHECKOUT_STEPS):
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, step))
            ).click()
            print(f"✅ Шаг {index+1}/5 оформления пройден")
            time.sleep(1)

        print("🎁 Выбор друга для подарка...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, FRIEND_INPUT_XPATH))
        ).send_keys(friend_name)
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, FRIEND_CONFIRM_XPATH))
        ).click()
        time.sleep(1)

        print("🔥 Финальные шаги...")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, FINAL_BUTTON_XPATH))
        ).click()
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, SSA_CHECKBOX_XPATH))
        ).click()
                
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, PURCHASE_BUTTON_XPATH))
        ).click()

        print("🎉 Покупка успешно завершена!")

    except Exception as e:
        print(f"❌ Критическая ошибка: {str(e)}")
        driver.save_screenshot("error_screenshot.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()