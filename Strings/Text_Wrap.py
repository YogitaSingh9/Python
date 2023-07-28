import textwrap
def wrap(string, max):
    return textwrap.fill(string, max)
if __name__ == '__main__':
    string, max = input(), int(input())
    result = wrap(string, max)
    print(result)