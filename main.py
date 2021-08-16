import os
import codecs


def delete_file():
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with codecs.open(file_path, 'r', 'utf-8') as f:
                search_word = "delete_this_file"
                content = f.read()
                if search_word in content:
                    print('word found')
                    print(file_path)
                    f.close()
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")


def delete_line():
    search_word = "delete_this_line"
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            delete_list = []
            with codecs.open(file_path, "r", 'utf-8') as f:
                lines = f.readlines()
                for num, line in enumerate(lines, 1):
                    if search_word in line:
                        search_line = num
                        delete_list.append(search_line)

            with codecs.open(file_path, "w", 'utf-8') as f:
                for line in lines:
                    if search_word not in line:
                        line.strip("\n")
                        f.write(line)
            if delete_list:
                with open("changes.txt", "a") as dc:
                    dc.write(f"Deleted line: {delete_list} in {file_path}\n")
                print(f"Deleted lines: {delete_list} in {file_path}")


def delete_block():

    lookup_from = 'delete_from'
    lookup_to = 'delete_to'

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            delete_list = []
            counter = 1
            with codecs.open(file_path, "r", 'utf-8') as f:
                lines = f.readlines()
                for num, line in enumerate(lines, 1):
                    if lookup_from in line:
                        del_from = num
                    elif lookup_to in line:
                        del_to = num
                        for i in range(del_from, del_to + 1):
                            delete_list.append(i)

            with codecs.open(file_path, "w", 'utf-8') as f:
                for line in lines:
                    if counter not in delete_list:
                        f.write(line)
                    counter += 1
                f.close()
            if delete_list:
                with open("changes.txt", "a") as dc:
                    dc.write(f"Deleted Block of lines: {delete_list} in {file_path}\n")
                print(f"Deleted Block of code: {delete_list} in {file_path}")


while input('Type "y" to continue ').lower() == "y":
    directory = input("Enter the directory to make changes (case sensitive): ")
    if os.path.isdir(directory):
        confirmation = input("Are you sure you want to proceed? (Y or N):")
        if confirmation.lower() == "y":
            delete_line()
            delete_file()
            delete_block()
        else:
            print("Process terminated.")






