with open('lines.txt', 'r') as f: 
    lines = len(list(filter(lambda x: x.strip(), f)))
