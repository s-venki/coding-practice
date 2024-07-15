def main():
    dict = input().split(' ')
    sentence = input("enter a sentence:")
    print(replace(dict, sentence))


def replace(l: list[str], s: str) -> str:
    s = s.split(' ')
    l.sort(key=len)
    for i in range(len(s)):
        for root in l:
            if s[i].startswith(root):
                s[i] = root
                break

    return ' '.join(s)


if __name__ == '__main__':
    main()
