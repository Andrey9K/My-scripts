import os
import openpyxl

def convert_to_xlsx(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".xlsx"):
            file_path = os.path.join(input_folder, filename)
            wb = openpyxl.load_workbook(file_path)
            output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.xlsx")
            wb.save(output_file)
            wb.close()

# Путь к папке с исходными файлами XLSX
input_folder = "/home/akozlov/Загрузки/Исходные Excel/"
# Путь к папке, в которую будут сохранены переконвертированные файлы XLSX
output_folder = "/home/akozlov/Загрузки/Форматированные Excel/"

# Вызов функции пересохранения файлов
convert_to_xlsx(input_folder, output_folder)