# words are from: http://www.talkenglish.com/vocabulary/top-1500-nouns.aspx

f = open("list-1500-nouns.txt", "r+")
new_file = ""
while(True):
    line = f.readline()
    print(line)

    if line == "":
        print("done")
        break

    words_in_line = line.split()

    new_file += words_in_line[0] + "\n"
print(new_file)
f.close()
f = open("list-1500-nouns.txt", "w")
f.write(new_file)
f.close()
