def count_occurences(file_name, word):
    count = 0
    try:
        text = open(file_name)
        line = text.read()
        line = line.replace('.','').replace(',','').replace(':','').replace('?','').split()
        for w in line:
            if w.lower() == word.lower():
                count += 1
        text.close()
    except Exception as e:
        print(e)
        
    return count

