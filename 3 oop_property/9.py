class TreeObj:
    """Описание вершин и листьев решающего дерева."""
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.left = None
        self.__right = None

    @property
    def left(self):
        return self.__left
    
    @left.getter
    def left(self, left_obj):
        self.left = left_obj
        
    @property
    def right(self):
        return self.__right
    
    @right.getter
    def right(self, right_obj):
        self.right = right_obj

class DecisionTree:
    """Работа с решающим деревом в целом."""
    
    @classmethod
    def predict(cls, root, x):
        """Построение прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root."""
        pass
    
    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """Добавление вершин в решающее дерево (метод должен возвращать добавленную вершину - объект класса TreeObj)."""
        pass
    
    