# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

# convert csv <-> ttv <-> txt
import tkinter.filedialog

print('enter path to file: ')
path = tkinter.filedialog.askopenfilename(title="SUPPORTED FILE TYPES: .csv, .txt, .ttv")

print('enter format to convert to, i.e. [csv]: ')
to = input()

end_lines = []
with open(path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    if (len(lines) == 1): 
        for line in lines:
            splitted = line.split("**")
            for v in splitted:
                end_lines.append(v)

    else: 
        for line in lines:
            end_lines.append(line)


path_to_new_file = path[:-3] + to
with open(path_to_new_file, 'a') as the_file:
    for x in end_lines:
        if to != "ttv":
            the_file.write(x + "\n")
        else:
            the_file.write(x.replace("* *", "*\t*") + "\n")
