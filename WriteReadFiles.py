fw = open("sample.txt", "w")
fw.write("Writing in text file\n")
fw.write("More words in text file\n")
fw.close()

fr = open("sample.txt", "r")
text = fr.read()
print(text)
fr.close()