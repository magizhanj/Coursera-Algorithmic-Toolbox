def add_two(f,s):
    return f+s


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(add_two(a, b))
