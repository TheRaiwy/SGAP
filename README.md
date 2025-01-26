# Steam Gift Auto-Purchaser 🤖🎮

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.0%2B-orange)](https://selenium-python.readthedocs.io/)

Автоматизированное оформление подарков в Steam с полной поддержкой всех платформ

## 🚀 Особенности
- Авторизация в Steam с 2FA поддержкой
- Автоматический поиск друга по профилю
- Оформление покупки в качестве подарка
- Поддержка Windows/macOS/Linux
- Пошаговая обработка корзины покупок

## 📦 Требования
- Python 3.10+
- Google Chrome последней версии
- ChromeDriver (инструкция ниже)

## ⚙️ Установка

### 1. Установите зависимости
```bash
pip install selenium webdriver-manager
```

### 2. Настройка ChromeDriver

#### Для всех ОС:
1. Проверьте версию Chrome:
   - Откройте `chrome://settings/help`
   - Запишите полную версию (например: `116.0.5845.141`)

2. Скачайте соответствующий ChromeDriver:
   - [Официальный сайт](https://chromedriver.chromium.org/downloads)
   - **Важно!** Версия должна точно совпадать с версией браузера

---

### 🪟 Windows
1. Скачайте `chromedriver_win32.zip`
2. Распакуйте в папку:
   ```powershell
   Expand-Archive -Path chromedriver_win32.zip -DestinationPath C:\chromedriver
   ```
3. Добавьте в PATH:
   - ПКМ по "Этот компьютер" → Свойства → Дополнительные параметры системы
   - Переменные среды → Path → Изменить → Новый
   - Добавьте: `C:\chromedriver`

---

### 🍎 macOS
```bash
# Установка через Homebrew
brew install --cask chromedriver

# Или ручная установка
curl -O https://chromedriver.storage.googleapis.com/116.0.5845.141/chromedriver_mac64.zip
unzip chromedriver_mac64.zip
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
```

---

### 🐧 Linux (Ubuntu/Debian)
```bash
# Установка зависимостей
sudo apt-get install -y unzip libnss3 libgconf-2-4

# Скачивание и установка
wget https://chromedriver.storage.googleapis.com/116.0.5845.141/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/
sudo chmod +x /usr/bin/chromedriver
```

## 🔧 Конфигурация
1. Откройте файл `main.py`
2. Замените значения:
```python
STEAM_LOGIN = "ВАШ_ЛОГИН"
STEAM_PASSWORD = "ВАШ_ПАРОЛЬ"
FRIEND_LINK = "ССЫЛКА_НА_ПРОФИЛЬ_ДРУГА"
GAME_URL = "ССЫЛКА_НА_ИГРУ"
```

## 🏃 Запуск
```bash
python app.py
```

## 🔍 Логирование процесса
- Все действия выводятся в консоль с эмодзи-индикаторами
- При ошибке создается скриншот `error_screenshot.png`

## ⚠️ Важные предупреждения
1. Steam может блокировать аккаунты за автоматизацию
2. Не используйте основной аккаунт Steam
3. Версии Chrome/ChromeDriver должны совпадать
4. XPath элементы могут меняться при обновлении Steam

## 🛠️ Устранение неполадок

| Ошибка                          | Решение                        |
|---------------------------------|--------------------------------|
| `NoSuchElementException`        | Обновите XPath элементы        |
| `SessionNotCreatedException`    | Проверьте версии Chrome/Driver |
| `TimeoutException`              | Увеличьте время ожидания       |

## 📜 Лицензия
MIT License. Использование на свой риск. Автор не несет ответственности за последствия.

## 📌 Примечания
- Для автоматического управления драйверами используйте:
```python
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
```
- Рекомендуется использовать виртуальное окружение Python
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
