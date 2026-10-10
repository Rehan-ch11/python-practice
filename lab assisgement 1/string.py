
def analyze(s):
    w = s.split()
    u = set(w)
    v = sum(c.lower() in "aeiou" for c in s)

    print("Words:", len(w))
    print("Characters:", len(s))

    if len(w) > 0:
        print("Longest:", max(w, key=len))
        print("Shortest:", min(w, key=len))
    else:
        print("Longest: None")
        print("Shortest: None")

    print("Vowels:", v)
    print("Unique words:", u)
    print("Alphabetical:", sorted(w))

    with open("word-analysis.txt", "w") as f:
        if len(w) > 0:
            result = (len(w), len(s), max(w, key=len),
                      min(w, key=len), v, u, sorted(w))
        else:
            result = (len(w), len(s), None, None, v, u, sorted(w))

        f.write(str(result))


s = input("Enter sentence: ")
analyze(s)
