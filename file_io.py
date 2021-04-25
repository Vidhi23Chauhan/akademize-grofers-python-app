f_names = open("sample_lines.txt", "r")
file_content_names = f_names.read()
print(file_content_names.split("\n"))

f_words = open("sample_words.txt", "r")
file_content_words = f_words.read()
print(file_content_words.split(" "))


f_numbers = open("sample_numbers.csv", "r")
file_content_numbers = f_numbers.read()
print(file_content_numbers.split(","))

"""

['Vidhi', 'Shobha', 'Manu', 'Yatharth', 'Ankush', 'Aditya']
['Vidhi', 'Shobha', 'Manu', 'Yatharth', 'Ankush', 'Aditya']
['one', 'two three', 'four five six']

"""