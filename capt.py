# Сделать рандомную правильную кнопку  --> Вроде есть
# Сделать пары смайлов, которые нельзя использовать вместе  --> Вроде есть
import config
import random
#pic = 4

# class rands:
















pic = random.randint(0, 78)# Рандомное животное для картинки
picL = config.animals[pic]
picNumb = random.randint(1, 5)  # Рандомный номер картинки с животным определенным выше

picEm = random.randint(1, 5)
p1 = random.randint(0, 78)
p2 = random.randint(0, 78)
p3 = random.randint(0, 78)
p4 = random.randint(0, 78)
p5 = random.randint(0, 78)

if picEm == 1: p1 = pic  # Присвоение правильного ответа рандомной кнопке
if picEm == 2: p2 = pic
if picEm == 3: p3 = pic
if picEm == 4: p4 = pic
if picEm == 5: p5 = pic


ps = [p1, p2, p3, p4, p5]


def double(self):
    if p1 == pic:  # Если первая кнопка правильная
        if p1 == p2:
            self.p2 = random.randint(0, 79)
        elif p1 == p3:
            self.p3 = random.randint(0, 79)
        elif p1 == p4:
            self.p4 = random.randint(0, 79)
        elif p1 == p5:
            self.p5 = random.randint(0, 79)
    elif (p1 != pic) and (p2 != pic):
        self.p2 = random.randint(0, 79)
    elif (p1 != pic) and (p3 != pic):
        self.p3 = random.randint(0, 79)
    elif (p1 != pic) and (p4 != pic):
        self.p4 = random.randint(0, 79)
    elif (p1 != pic) and (p5 != pic):
        self.p5 = random.randint(0, 79)
    if p2 == pic:  # Если вторая кнопка правильная
        if p2 == p1:
            self.p1 = random.randint(0, 79)
        elif p2 == p3:
            self.p3 = random.randint(0, 79)
        elif p2 == p4:
            self.p4 = random.randint(0, 79)
        elif p2 == p5:
            self.p5 = random.randint(0, 79)
    elif (p2 != pic) and (p1 != pic):
        self.p1 = random.randint(0, 79)
    elif (p2 != pic) and (p3 != pic):
        self.p3 = random.randint(0, 79)
    elif (p2 != pic) and (p4 != pic):
        self.p4 = random.randint(0, 79)
    elif (p2 != pic) and (p5 != pic):
        self.p5 = random.randint(0, 79)
    if p3 == pic:  # Если третья кнопка правильная
        if p3 == p1:
            self.p1 = random.randint(0, 79)
        elif p3 == p2:
            self.p2 = random.randint(0, 79)
        elif p3 == p4:
            self.p4 = random.randint(0, 79)
        elif p3 == p5:
            self.p5 = random.randint(0, 79)
    elif (p3 != pic) and (p1 != pic):
        self.p1 = random.randint(0, 79)
    elif (p3 != pic) and (p2 != pic):
        self.p2 = random.randint(0, 79)
    elif (p3 != pic) and (p4 != pic):
        self.p4 = random.randint(0, 79)
    elif (p3 != pic) and (p5 != pic):
        self.p5 = random.randint(0, 79)
    if p4 == pic:  # Если четвертая кнопка правильная
        if p4 == p1:
            self.p1 = random.randint(0, 79)
        elif p4 == p2:
            self.p2 = random.randint(0, 79)
        elif p4 == p3:
            self.p3 = random.randint(0, 79)
        elif p4 == p5:
            self.p5 = random.randint(0, 79)
    elif (p4 != pic) and (p1 != pic):
        self.p1 = random.randint(0, 79)
    elif (p4 != pic) and (p2 != pic):
        self.p2 = random.randint(0, 79)
    elif (p4 != pic) and (p3 != pic):
        self.p3 = random.randint(0, 79)
    elif (p4 != pic) and (p5 != pic):
        self.p5 = random.randint(0, 79)
    if p5 == pic:  # Если пятая кнопка правильная
        if p5 == p1:
            self.p1 = random.randint(0, 79)
        elif p5 == p2:
            self.p2 = random.randint(0, 79)
        elif p5 == p3:
            self.p3 = random.randint(0, 79)
        elif p5 == p4:
            self.p4 = random.randint(0, 79)
    elif (p5 != pic) and (p1 != pic):
        self.p1 = random.randint(0, 79)
    elif (p5 != pic) and (p2 != pic):
        self.p2 = random.randint(0, 79)
    elif (p5 != pic) and (p3 != pic):
        self.p3 = random.randint(0, 79)
    elif (p5 != pic) and (p4 != pic):
        self.p4 = random.randint(0, 79)


def exception(self):
    if ((p1 == 55) and ((p2 == 56) or (p3 == 56) or (p4 == 56) or (p5 == 56))) or \
            ((p2 == 55) and ((p1 == 56) or (p3 == 56) or (p4 == 56) or (p5 == 56))) or \
            ((p3 == 55) and ((p2 == 56) or (p1 == 56) or (p4 == 56) or (p5 == 56))) or \
            ((p4 == 55) and ((p2 == 56) or (p3 == 56) or (p1 == 56) or (p5 == 56))) or \
            ((p5 == 55) and ((p2 == 56) or (p3 == 56) or (p4 == 56) or (p1 == 56))):  # Слон и мамонт
        if (55 in ps) and (pic == 55):
            if 56 == p1:
                self.p1 = random.randint(0, 79)
            elif 56 == p2:
                self.p2 = random.randint(0, 79)
            elif 56 == p3:
                self.p3 = random.randint(0, 79)
            elif 56 == p4:
                self.p4 = random.randint(0, 79)
            elif 56 == p4:
                self.p4 = random.randint(0, 79)
        elif (56 in ps) and (pic == 56):
            if 55 == p1:
                self.p1 = random.randint(0, 79)
            elif 55 == p2:
                self.p2 = random.randint(0, 79)
            elif 55 == p3:
                self.p3 = random.randint(0, 79)
            elif 55 == p4:
                self.p4 = random.randint(0, 79)
            elif 55 == p4:
                self.p4 = random.randint(0, 79)
    elif ((p1 == 23) and ((p2 == 12) or (p3 == 12) or (p4 == 12) or (p5 == 12))) or \
            ((p2 == 23) and ((p1 == 12) or (p3 == 12) or (p4 == 12) or (p5 == 12))) or \
            ((p3 == 23) and ((p2 == 12) or (p1 == 12) or (p4 == 12) or (p5 == 12))) or \
            ((p4 == 23) and ((p2 == 12) or (p3 == 12) or (p1 == 12) or (p5 == 12))) or \
            ((p5 == 23) and ((p2 == 12) or (p3 == 12) or (p4 == 12) or (p1 == 12))):  # Свин и кабан
        if (23 in ps) and (pic == 23):
            if 12 == p1:
                self.p1 = random.randint(0, 79)
            elif 12 == p2:
                self.p2 = random.randint(0, 79)
            elif 12 == p3:
                self.p3 = random.randint(0, 79)
            elif 12 == p4:
                self.p4 = random.randint(0, 79)
            elif 12 == p4:
                self.p4 = random.randint(0, 79)
        elif (12 in ps) and (pic == 12):
            if 23 == p1:
                self.p1 = random.randint(0, 79)
            elif 23 == p2:
                self.p2 = random.randint(0, 79)
            elif 23 == p3:
                self.p3 = random.randint(0, 79)
            elif 23 == p4:
                self.p4 = random.randint(0, 79)
            elif 23 == p4:
                self.p4 = random.randint(0, 79)
    elif ((p1 == 48) and ((p2 == 49) or (p3 == 49) or (p4 == 49) or (p5 == 49))) or \
            ((p2 == 48) and ((p1 == 49) or (p3 == 49) or (p4 == 49) or (p5 == 49))) or \
            ((p3 == 48) and ((p2 == 49) or (p1 == 49) or (p4 == 49) or (p5 == 49))) or \
            ((p4 == 48) and ((p2 == 49) or (p3 == 49) or (p1 == 49) or (p5 == 49))) or \
            ((p5 == 48) and ((p2 == 49) or (p3 == 49) or (p4 == 49) or (p1 == 49))):  # Кит и акула
        if (48 in ps) and (pic == 48):
            if 49 == p1:
                self.p1 = random.randint(0, 79)
            elif 49 == p2:
                self.p2 = random.randint(0, 79)
            elif 49 == p3:
                self.p3 = random.randint(0, 79)
            elif 49 == p4:
                self.p4 = random.randint(0, 79)
            elif 49 == p4:
                self.p4 = random.randint(0, 79)
        elif (49 in ps) and (pic == 49):
            if 48 == p1:
                self.p1 = random.randint(0, 79)
            elif 48 == p2:
                self.p2 = random.randint(0, 79)
            elif 48 == p3:
                self.p3 = random.randint(0, 79)
            elif 48 == p4:
                self.p4 = random.randint(0, 79)
            elif 48 == p4:
                self.p4 = random.randint(0, 79)
    elif ((p1 == 54) and ((p2 == 14) or (p3 == 14) or (p4 == 14) or (p5 == 14))) or \
            ((p2 == 54) and ((p1 == 14) or (p3 == 14) or (p4 == 14) or (p5 == 14))) or \
            ((p3 == 54) and ((p2 == 14) or (p1 == 14) or (p4 == 14) or (p5 == 14))) or \
            ((p4 == 54) and ((p2 == 14) or (p3 == 14) or (p1 == 14) or (p5 == 14))) or \
            ((p5 == 54) and ((p2 == 14) or (p3 == 14) or (p4 == 14) or (p1 == 14))):  # Горилла и обезьяна
        if (54 in ps) and (pic == 54):
            if 14 == p1:
                self.p1 = random.randint(0, 79)
            elif 14 == p2:
                self.p2 = random.randint(0, 79)
            elif 14 == p3:
                self.p3 = random.randint(0, 79)
            elif 14 == p4:
                self.p4 = random.randint(0, 79)
            elif 14 == p4:
                self.p4 = random.randint(0, 79)
        elif (14 in ps) and (pic == 14):
            if 54 == p1:
                self.p1 = random.randint(0, 79)
            elif 54 == p2:
                self.p2 = random.randint(0, 79)
            elif 54 == p3:
                self.p3 = random.randint(0, 79)
            elif 54 == p4:
                self.p4 = random.randint(0, 79)
            elif 54 == p4:
                self.p4 = random.randint(0, 79)
