uniqueTitles = set()
with open("title1.txt") as f:
    for line in f:
        uniqueTitles.add(line)

outputFile = "deduped_title1.txt"
output = open(outputFile, "a")
for title in uniqueTitles:
    output.write(title)
output.close()
