def split_and_join(line):
    words = line.split(" ")
    joined = "-".join(words)
    return joined

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
