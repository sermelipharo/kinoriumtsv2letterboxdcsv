# Конвертер Экспорта Кинориума в Импорт Letterboxd

![Static Badge](https://img.shields.io/badge/letterboxd-2C3440?logo=letterboxd) ![Static Badge](https://img.shields.io/badge/python3-grey?style=flat&logo=python&logoColor=white) [![en](https://img.shields.io/badge/lang-en-FF8002.svg)](README.md) [![ru](https://img.shields.io/badge/lang-ru-00E153.svg)](README.ru.md) [![ua](https://img.shields.io/badge/lang-ua-41BDF3.svg)](README.uk.md)
Перенос оценок и отзывов с платформы Кинориум на платформу Letterboxd.

## Описание
Скрипт kinoriumtsv2letterboxdcsv  предназначен для обработки и преобразования данных о фильмах из формата бекапа в Kinorium'е в формат CSV для импорта совместимый с Letterboxd. Он объединяет данные из двух TSV файлов (файл с оценками и файл с комментариями), фильтрует их (оставляя только фильмы и мультфильмы), и затем экспортирует результаты в формате CSV, поделенные на 1900 строк (лимит Letterboxd'a).

## Функциональность
- Объединение данных из двух TSV файлов
- Фильтрация данных для исключения сериалов/эпизодов/мультсериалов
- Экспорт обработанных данных в CSV файлы, совместимые с Letterboxd

## Установка
Для работы скрипта необходим Python 3 и библиотеки Pandas и Tkinter. Поскольку Tkinter обычно идет в комплекте с Python, он может не требовать отдельной установки. Однако, если в вашей системе его нет, вот команды для его установки в различных операционных системах:
### Tkinter
#### Debian/Ubuntu:
```bash
sudo apt-get install python3-tk
```

#### Fedora:
```bash
sudo dnf install python3-tkinter
```

#### MacOS (с использованием Homebrew):
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
Чтобы установить необходимые библиотеки, используйте следующую команду:

```bash
pip install Pandas
```

## Использование
Чтобы использовать этот скрипт, выполните следующие шаги:

1. Получите нужные файлы экспорта с вашего аккаунта Kinorium. Для этого перейдите на страницу [Настройки Kinorium](https://kinorium.com/user/settings/) и выполните экспорт/бэкап данных.
2. Запустите скрипт.
```bash
python3 merger-g.py
```
3. При появлении первого диалогового окна выберите файл с оценками (обычно с суффиксом `votes`).
4. Во втором диалоговом окне выберите файл с комментариями (с суффиксом `comments`).
5. Укажите папку, куда будут сохранены результаты.
6. После обработки данных скрипт сохранит результаты в выбранную папку.

Полученные файлы можно затем импортировать в Letterboxd. Для этого:
- Перейдите на страницу [Импорт Letterboxd](https://letterboxd.com/import/).
- Загрузите обработанные файлы.
- Рекомендуется установить галочку "Hide successful matches", чтобы легче было исправить нераспознанные фильмы.

Убедитесь, что выбираете правильные файлы в соответствующие диалоговые окна, чтобы обеспечить корректную обработку данных.
