import random
number = set([])
str = set([])
def random_num(number):
    for i in range(1000):
        number.add(random.random()*100)

def random_str(str):
    for i in range(0,1000):
        m_str = "".join(random.choices("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm", k=random.randint(0,100)))
        str.add(m_str)

def select():
    for i in number:
        if i>=20 and i<=50:
                print(i)
    for i in str:
        if i.find("at")>=0:
            print(i)
        # if "at" in i:
        #     print(i)

def main():
    random_num(number)
    random_str(str)
    select()

main()