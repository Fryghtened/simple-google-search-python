from googlesearch import search
query = "What is air?"
count = 0
f = open("links.txt" , "w")
for i in search(query, tld="com", num=10, stop=10, pause=2):
    f.write(i + "\n")
    count += 1
    print(f"Wrote to file {count} times")
    
f.close()
