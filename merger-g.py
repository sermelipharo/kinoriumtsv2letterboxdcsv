import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import locale

# Установка локали и определение текущей локали пользователя
locale.setlocale(locale.LC_CTYPE, '')
current_locale, _ = locale.getlocale()

# Установка текстов интерфейса в зависимости от локали
if current_locale.startswith(('hy', 'ru', 'be', 'uk')):
    # Русский язык
    votes_file_title = "Выберите файл с оценками"
    comments_file_title = "Выберите файл с комментариями"
    folder_chooser_title = "Выберите папку для сохранения результатов"
    success_message = "Файлы успешно обработаны и сохранены!"
    warning_message = "Не выбраны все необходимые файлы или папка."
else:
    # Английский язык
    votes_file_title = "Select the ratings file"
    comments_file_title = "Select the comments file"
    folder_chooser_title = "Select a folder to save the results"
    success_message = "Files have been successfully processed and saved!"
    warning_message = "Not all necessary files or folder have been selected."

def select_file(title):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title=title)
    return file_path

def select_output_folder(title):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=title)
    return folder_path

def process_files(votes_file, comments_file, output_path):
    # Чтение файлов с правильной кодировкой
    df_votes = pd.read_csv(votes_file, sep='\t', encoding='utf-16le')
    df_comments = pd.read_csv(comments_file, sep='\t', encoding='utf-16le')

    # Фильтрация, чтобы оставить только фильмы и мультфильмы
    film_types = ['Фильм', 'Мультфильм', 'Movie', 'Animation Movie', 'Фільм', 'Мультфільм']
    df_votes = df_votes[df_votes['Type'].isin(film_types)]

    # Обработка в зависимости от наличия столбца 'Original Title'
    if 'Original Title' in df_votes.columns:
        # Если есть столбец 'Original Title'
        merged_df = pd.merge(df_votes, df_comments, on=['Date', 'Original Title', 'Year', 'My rating'], how='left', suffixes=('', '_comment'))
        merged_df['Title'] = merged_df['Original Title'].fillna(merged_df['Title'])
    else:
        # Если столбца 'Original Title' нет
        merged_df = pd.merge(df_votes, df_comments, on=['Date', 'Title', 'Year', 'My rating'], how='left', suffixes=('', '_comment'))

    # Обработка датафрейма
    processed_df = merged_df[['Title', 'Year', 'My rating', 'Date', 'Comment']].copy()
    processed_df.drop(columns=['Original Title'], errors='ignore', inplace=True)
    processed_df.rename(columns={'My rating': 'Rating10', 'Date': 'WatchedDate', 'Comment': 'Review'}, inplace=True)
    processed_df['Rating10'] = processed_df['Rating10'].fillna(0).astype(int)
    processed_df['WatchedDate'] = pd.to_datetime(processed_df['WatchedDate']).dt.strftime('%Y-%m-%d')

    # Разделение на части и сохранение каждой части в отдельный файл
    chunk_size = 1900
    for i, chunk in enumerate(range(0, len(processed_df), chunk_size)):
        chunk_df = processed_df.iloc[chunk:chunk + chunk_size]
        chunk_df.to_csv(f"{output_path}{i+1}.csv", index=False, encoding='utf-8-sig')

# Выбор файлов и папки для сохранения
votes_file = select_file(votes_file_title)
comments_file = select_file(comments_file_title)
output_folder = select_output_folder(folder_chooser_title)

if votes_file and comments_file and output_folder:
    output_path = output_folder + '/export_'
    process_files(votes_file, comments_file, output_path)
    messagebox.showinfo("Done", success_message)
else:
    messagebox.showwarning("Warning", warning_message)
