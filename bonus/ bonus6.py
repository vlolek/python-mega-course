contents = ["all carrots  are t obe sliced longitudinally", 
            "the carrots are sliced longitudinally", "the carrots are sliced longitudinally", 
            "all carrots are to be sliced longitudinally"]
filenames = ["doc.txt", "report.txt", "pressentation.txt "]
for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
