def reverse_words(str):
    tmp = str.split()
    tmp.reverse()
    ret = ""
    for word in tmp:
        ret += word + " "
    ret = ret[:-1]
    return ret

def main():
    s1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    s2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    print("STRING 1")
    print(reverse_words(s1))
    print("STRING 2")
    print(reverse_words(s2))
if __name__ =="__main__":
    main()