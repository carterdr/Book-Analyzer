def main():
    path = "books/frankestein.txt"
    text = openFile(path)
    printReport(text, path)
def getNumWords(text):
    return len(text.split())
def openFile(path):
    with open(path) as f:
        return f.read()
def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            if c.lower() not in chars:
                chars[(c.lower())] = 1
            else:    
                chars[(c.lower())] += 1    
    return chars
def printReport(text, path):
    print(f"--- Begin report of {path} ---")
    print(f"{getNumWords(text)} found in the document")
    lis = []
    for key, value in get_chars_dict(text).items():
        lis.append((key, value))
    lis.sort(key = lambda x: x[1], reverse = True)
    for item in lis:
        print(f"The {item[0]} character was found {item[1]} times")
    print("--- End report ---")
main()