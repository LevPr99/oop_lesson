class Museum:
    
    def __init__(self, name):
        self.name = name
        self.exhibits = list()
    
    def add_exhibit(self, obj):
        self.exhibits.append(obj)
        
    def remove_exhibit(self, obj):
        if obj in self.exhibits:
            self.exhibits.remove(obj)
            
    def get_info_exhibit(self, indx):
        return 'Описание экспоната {name}: {descr}'.format(descr=self.exhibits[indx].descr, name=self.exhibits[indx].name)


class Picture:
    
    def __init__(self, name, author, descr):
        self.name = name
        self.descr = descr
        self.author = author
# 

class Mummies:
    
    def __init__(self, name, location, descr):
        self.name = name
        self.descr = descr
        self.location = location


class Papyri:
    
    def __init__(self, name, date, descr):
        self.name = name
        self.descr = descr
        self.date = date

mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in range(len(mus.exhibits)):
    print(mus.get_info_exhibit(x))