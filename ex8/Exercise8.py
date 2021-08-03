import os


def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir()

    with open(file) as f:
        filelist = f.read().split("\n")
    print(filelist)

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file,f"{i}{format}")
            i += 1
    print(files)
soldier(r"C:\Users\piyush thakur\PycharmProjects\ex8",
        r"C:\Users\piyush thakur\PycharmProjects\ex8\exercise8.py",
        r".PNG")