import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

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
    df_votes = df_votes[df_votes['Type'].isin(['Фильм', 'Мультфильм'])]

    # Объединение данных без изменения даты
    merged_df = pd.merge(df_votes, df_comments, on=['Date', 'Original Title', 'Year', 'My rating'], how='left', suffixes=('', '_comment'))

    # Создание копии датафрейма для обработки
    processed_df = merged_df[['Original Title', 'Title', 'Year', 'My rating', 'Date', 'Comment']].copy()

    # Заполнение 'Original Title' значениями из 'Title', если 'Original Title' пуст
    processed_df['Title'] = processed_df['Original Title'].fillna(processed_df['Title'])

    # Удаление лишнего столбца 'Original Title'
    processed_df.drop(columns=['Original Title'], inplace=True)

    # Переименование столбцов и преобразование типов данных
    processed_df.rename(columns={'My rating': 'Rating10', 'Date': 'WatchedDate', 'Comment': 'Review'}, inplace=True)
    processed_df['Rating10'] = processed_df['Rating10'].fillna(0).astype(int)

    # Преобразование формата даты
    processed_df['WatchedDate'] = pd.to_datetime(processed_df['WatchedDate']).dt.strftime('%Y-%m-%d')

    # Разделение на части и сохранение каждой части в отдельный файл
    chunk_size = 1900
    for i, chunk in enumerate(range(0, len(processed_df), chunk_size)):
        chunk_df = processed_df.iloc[chunk:chunk + chunk_size]
        chunk_df.to_csv(f"{output_path}{i+1}.csv", index=False, encoding='utf-8-sig')

# Выбор файлов и папки для сохранения
votes_file = select_file("Выберите файл с оценками")
comments_file = select_file("Выберите файл с комментариями")
output_folder = select_output_folder("Выберите папку для сохранения результатов")

if votes_file and comments_file and output_folder:
    output_path = output_folder + '/export_'
    process_files(votes_file, comments_file, output_path)
    messagebox.showinfo("Готово", "Файлы успешно обработаны и сохранены!")
else:
    messagebox.showwarning("Внимание", "Не выбраны все необходимые файлы или папка.")
