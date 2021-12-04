if __name__ == "__main__":
    list_empl_name = ["Ivanov", "Petrov", "Egorov"]
    list_empl_positions = ["Manager", "Translator", "Engineer"]

    file_for_HR_empl_name = "list_empl.txt"
    file_for_HR_empl_position = "list_empl_positions.txt"
    file_for_HR_empl_name_plus_position = "list_mpl_name_plus_position.txt"

    with open(file_for_HR_empl_name, "w", encoding="utf-8") as f:
        for employee in list_empl_name:
            f.write(employee + "\n")

    with open(file_for_HR_empl_position, "w", encoding="utf-8") as f:
        for employee in list_empl_positions:
            f.write(employee + "\n")

    with open(file_for_HR_empl_name, "r") as input_file_1, open(file_for_HR_empl_position, "r") as input_file_2, open(
            file_for_HR_empl_name_plus_position, "w") as output_file:
        print(file_for_HR_empl_name_plus_position)
    pass



# 1 Написать декоратор, сохраняющий результат в файл output.txt помимо возвращения. Результаты должны накапливаться в файле.
#
#  2    Написать генератор, возвращающий по 3 символа из текстового файла, при этом не загружая в память весь файл.
#
# 3 Написать генератор, возвращающий по одному слову текстового файла, при этом не загружая в память весь файл. В качестве разделителя слов использовать символ пробела.
#
# 4 Написать генератор, возвращающий по одной строке из текстового файла. Символом окончания строки является символ “\n”. Встроенной реализацией пользоваться нельзя.
# with open(filename) as f:
# for line in f:	...
# 5 Написать генератор, возвращающий  последние n строк из текстового файла, при этом не загружая в память весь файл.