from random import Random

class Cell:
    '''С помощью класса Cell предполагается создавать отдельные клетки'''
    
    def __init__(self) -> None:
        self.around_mines = 0
        '''число мин вокруг клетки (начальное значение 0)'''
        self.mine : False
        self.fl_open = False
        self.__M_count = 0
        
class GamePole:
    '''С помощью класса GamePole должна быть возможность создавать
        квадратное игровое поле с числом клеток N x N'''
    
    def __init__(self, N, M) -> None:
        self.N = N
        '''размер поля'''
        self.M = M
        '''общее число мин на поле'''
    
    def init(self):
        '''инициализация поля с новой расстановкой M мин'''
        field = list()
        for i in range(self.N):
            for j in range(self.N):
                rnd_m = self.cell_random()
                if rnd_m is not None:
                    field.append(rnd_m)
    
    def show(self):
        '''отображение поля в консоли в виде таблицы чисел открытых клеток'''
        pass
    
    def cell_random(self):
        cl = Cell()
        rnd = Random.randint(0,1)
        cl.mine = rnd
        self.__M_count += rnd
        return 0 if self.__M_count >= self.M else cl