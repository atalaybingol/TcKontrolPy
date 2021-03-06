from pywebio.input import input, FLOAT
from pywebio.output import put_text


class TCK():

    def __init__(self, tck):
        self.tck = tck

    def check(self):

        tck = str(self.tck)

        if(len(tck) != 11):
            return tck+" nope"

        lst = [int(x) for x in str(tck)]

        a = int(lst[0])+int(lst[2])+int(lst[4])+int(lst[6])+int(lst[8])

        b = int(lst[1])+int(lst[3])+int(lst[5])+int(lst[7])

        x = ((a*7)-b) % 10
        y = (a+b+x) % 10

        if lst[0] != 0 and x == lst[9] and y == lst[10]:
            return tck+" Doğru"
        else:
            return tck+" nope"


def main():

    tc = input("TC Kimlik Numarası：", type=FLOAT)

    a = TCK(tc)

    save(a.check())
    put_text(a.check())


def save(i):
    file = open("history.txt", "a")
    file.write(i)
    file.close()


while(True):
    if __name__ == '__main__':
        main()
