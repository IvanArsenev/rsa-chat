import socket
import threading

def euler(n):
    f = n
    if n%2 == 0:
        while n%2 == 0:
            n = n // 2
        f = f // 2
    i = 3
    while i*i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n // i
            f = f // i
            f = f * (i-1)
        i = i + 2
    if n > 1:
        f = f // n
        f = f * (n-1)
    return f

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def decode(string, e, n):
    for i in range(1, n):
        if (i*e)%euler(n) == 1:
            d = i
            break
    code = [int(x) for x in string]
    s = (get_key(alphabet, (code[0]**d)%n))
    for i in range(1,len(code)):
        if ((code[i]**d)%n-code[i-1]) < 0:
            s += (get_key(alphabet, (code[i]**d)%n-code[i-1]+n))
        else:
            s += (get_key(alphabet, (code[i]**d)%n-code[i-1]))
    return s

def encode(string, e, n):
    coded_s, s = 0, ''
    for i in range(len(string)):
        s += str(((alphabet[string[i]]+coded_s)**e)%n) + ' '
        coded_s = ((alphabet[string[i]]+coded_s)**e)%n
    return s

alphabet = {' ':0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52, 'а':53, 'б':54, 'в':55, 'г':56, 'д':57, 'е':58, 'ж':59, 'з':60, 'и':61, 'й':62, 'к':63, 'л':64, 'м':65, 'н':66, 'о':67, 'п':68, 'р':69, 'с':70, 'т':71, 'у':72, 'ф':73, 'х':74, 'ц':75, 'ч':76, 'ш':77, 'щ':78, 'ъ':79, 'ы':80, 
'ь':81, 'э':82, 'ю':83, 'я':84, 'А':85, 'Б':86, 'В':87, 'Г':88, 'Д':89, 'Е':90, 'Ж':91, 'З':92, 'И':93, 'Й':94, 'К':95, 'Л':96, 'М':97, 'Н':98, 'О':99, 'П':100, 'Р':101, 'С':102, 'Т':103, 'У':104, 'Ф':105, 'Х':106, 'Ц':107, 'Ч':108, 'Ш':109, 'Щ':110, 'Ъ':111, 'Ы':112, 'Ь':113, 'Э':114, 'Ю':115, 'Я':116, '!':117, '"':118, '#':119, '$':120, '%':121, '&':122, "'":123, '(':124, ')':125, '*':126, '+':127, ',':128, '-':129, '.':130, '/':131, '0':132, '1':133, '2':134, '3':135, '4':136, '5':137, '6':138, '7':139, '8':140, '9':141, ':':142, ';':143, '<':144, '=':145, '>':146, '?':147, '@':148, '"':149, '^':150}

e, n = 5, 3451

def read_sok():
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8').split()[0], decode(data.decode('utf-8').split()[1:], e, n))
server = '90.188.89.254', 5050

alias = input("Ваш псевдоним: ")

sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.sendto(('['+alias+'] '+ '0000000000').encode('utf-8'), server)
potok = threading.Thread(target= read_sok)
potok.start()
while True:
    sor.sendto(('['+alias+'] '+ encode(input(), e, n)).encode('utf-8'), server)