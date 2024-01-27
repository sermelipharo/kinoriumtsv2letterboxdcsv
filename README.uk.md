# Конвертер Експорту Кіноріуму в Імпорт Letterboxd

![Static Badge](https://img.shields.io/badge/letterboxd-gray?logo=letterboxd) ![Static Badge](https://img.shields.io/badge/python3-FF8002?style=flat&logo=python&logoColor=white) [![en](https://img.shields.io/badge/lang-en-00E153.svg)](README.md) [![ru](https://img.shields.io/badge/lang-ru-41BDF3.svg)](README.ru.md)

## Опис
Скрипт kinoriumtsv2letterboxdcsv призначений для обробки та перетворення даних про фільми з формату бекапу в Кіноріумі в формат CSV для імпорту сумісного з Letterboxd. Він об'єднує дані з двох TSV файлів, фільтруючи їх так, щоб залишились лише фільми та мультфільми, та експортує результати у форматі CSV, поділ на 1900 рядків (ліміт Letterboxd'a).

## Функціональність
- Об'єднання даних з двох TSV файлів.
- Фільтрація даних для виключення серіалів/епізодів/мультсеріалів.
- Експорт оброблених даних у CSV файли, сумісні з Letterboxd.

## Встановлення
Скрипт потребує Python 3, а також бібліотек Pandas та Tkinter. Зазвичай, Tkinter входить в стандартний комплект Python, але якщо у вашій системі його немає, ось команди для його встановлення в різних операційних системах:
### Tkinter
#### Debian/Ubuntu:
```bash
sudo apt-get install python3-tk
```

#### Fedora:
```bash
sudo dnf install python3-tkinter
```

#### MacOS (з використанням Homebrew):
```bash
brew install python-tk
```

#### Arch Linux:
```bash
sudo pacman -Syu tk --noconfirm
```

#### RHEL/CentOS 6/7:
```bash
sudo yum install -y python3-tkinter
```

#### OpenSUSE:
```bash
sudo zypper in -y python-tk
```
### Pandas
Щоб встановити необхідні бібліотеки, використовуйте наступну команду:

```bash
pip install Pandas
```

## Використання
Щоб скористатися цим скриптом, виконайте наступні кроки:

1. Отримайте потрібні файли експорту з вашого акаунту Кіноріум. Для цього перейдіть на сторінку [Налаштування Кіноріум](https://kinorium.com/user/settings/) та виконайте експорт/бекап даних.
2. Запустіть скрипт за допомогою команди:
```bash
python3 merger-g.py
```
3. При появі першого діалогового вікна виберіть файл з оцінками (зазвичай з суфіксом `votes`).
4. У другому діалоговому вікні виберіть файл з коментарями (з суфіксом `comments`).
5. Вкажіть папку, куди будуть збережені результати.
6. Після обробки даних скрипт збереже результати у вибрану папку.

Отримані файли потім можна імпортувати в Letterboxd. Для цього:
- Перейдіть на сторінку [Імпорт Letterboxd](https://letterboxd.com/import/).
- Завантажте оброблені файли.
- Рекомендується встановити галочку "Hide successful matches", щоб легше було виправити невпізнані фільми.

Переконайтеся, що вибираєте правильні файли у відповідні діалогові вікна, щоб забезпечити коректну обробку даних.
