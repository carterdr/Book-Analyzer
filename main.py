def main():
    path = "books/frankestein.txt"
    text = openFile(path)
    print(getNumWords(text))
    print(get_chars_dict(text))
        
def getNumWords(text):
    return len(text.split())
def openFile(path):
    with open(path) as f:
        return f.read()
def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.lower() not in chars:
            chars[(c.lower())] = 1
        else:    
            chars[(c.lower())] += 1    
    return chars
main()