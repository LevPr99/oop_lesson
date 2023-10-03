class Cell:
    '''С помощью класса Cell предполагается создавать отдельные клетки'''
    
    def __init__(self) -> None:
        self.around_mines
        self.mine
        self.fl_open
        
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
                field.append(self.mine_random())
    
    def show(self):
        '''отображение поля в консоли в виде таблицы чисел открытых клеток'''
        pass
    
    @classmethod
    def mine_random(cls):
        pass
        return Cell()