data = "This is the data I want to save into the file."
file_path = "example.txt"

file = open(file_path, "w")
file.write(data)
file.close()
