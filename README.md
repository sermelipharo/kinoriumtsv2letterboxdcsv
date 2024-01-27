# Kinorium Export to Letterboxd Import Converter

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md) [![ru](https://img.shields.io/badge/lang-ru-red.svg)](README.ru.md)

## Description
The `kinoriumtsv2letterboxdcsv` script is designed to process and convert movie data from the Kinorium backup format to a CSV format compatible for import into Letterboxd. It combines data from two TSV files (a file with ratings and a file with comments), filters them (leaving only movies and animated films), and then exports the results in CSV format, divided into 1900 lines (Letterboxd's limit).

## Functionality
- Combining data from two TSV files
- Filtering data to exclude series/episodes/animated series
- Exporting processed data to CSV files compatible with Letterboxd

## Installation
The script requires Python 3, Pandas, and Tkinter. Since Tkinter usually comes with Python, it may not require separate installation. However, if it's not available in your system, here are the commands for installing it in different operating systems:

### Debian/Ubuntu:
```bash
sudo apt-get install python3-tk
```

### Fedora:
```bash
sudo dnf install python3-tkinter
```

### MacOS (using Homebrew):
```bash
brew install python-tk
```

### Arch Linux:
```bash
sudo pacman -Syu tk --noconfirm
```

### RHEL/CentOS 6/7:
```bash
sudo yum install -y python3-tkinter
```

### OpenSUSE:
```bash
sudo zypper in -y python-tk
```
To install the required libraries, use the following command:

```bash
pip install Pandas
```

## Usage
To use this script, follow these steps:

1. Obtain the necessary export files from your Kinorium account. To do this, go to the [Kinorium Settings page](https://kinorium.com/user/settings/) and perform a data export/backup.
2. Run the script.
```bash
python3 merger-g.py
```

3. When the first dialog box appears, select the file with ratings (usually with the suffix `votes`).
4. In the second dialog box, select the file with comments (with the suffix `comments`).
5. Specify the folder where the results will be saved.
6. After processing the data, the script will save the results in the selected folder.

The resulting files can then be imported into Letterboxd. To do this:
- Go to the [Letterboxd Import page](https://letterboxd.com/import/).
- Upload the processed files.
- It is recommended to check the "Hide successful matches" box to more easily correct unrecognized movies.

Make sure to select the correct files in the appropriate dialog boxes to ensure proper data processing.
```
