import glob 

myfiles = glob.glob("txt_files/*.txt")

for filepath in myfiles:
    with open(filepath, "r") as file:
        print(file.read().upper())
