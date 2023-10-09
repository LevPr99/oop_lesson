class TreeObj:
    """Описание вершин и листьев решающего дерева."""
    def __init__(self, indx: bool, value: str=None):
        self.indx = indx
        self.value = value
        self.left = None
        self.right = None

    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, left_obj):
        self.__left = left_obj
        
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, right_obj):
        self.__right = right_obj

    
class DecisionTree:
    """Работа с решающим деревом в целом."""
    
    @classmethod
    def predict(cls, root, x):
        """Построение прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root."""
        if x[0]:
            root = root.left
        else:
            root = root.right
        if x[root.indx] == 1:
            root = root.left
        else:
            root = root.right
        return root.value
    
    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """Добавление вершин в решающее дерево (метод должен возвращать добавленную вершину - объект класса TreeObj)."""
        if node is not None:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj
    
    
assert type(TreeObj.left) == property and type(TreeObj.right) == property, "в классе TreeObj должны быть объекты-свойства left и right"

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

assert DecisionTree.predict(root, [1, 1, 0]) == 'программист', "неверный вывод решающего дерева" #?
assert DecisionTree.predict(root, [0, 1, 0]) == 'нет', "неверный вывод решающего дерева" #?
assert DecisionTree.predict(root, [0, 1, 1]) == 'посмотрим', "неверный вывод решающего дерева" #?