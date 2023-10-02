class Point:
    
    class __Meta:
        pass
    
    def __init__(self, x=0, y=0, z=0) -> None:
        self._x = x # protected (доступно внутри класса и в дочерних классах) (на самом деле нет, но)
        self.__y = y #  private (доступно только внутри класса)
        self.z = z  #   public
        
    def __set_coord(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
        
    
    
pt = Point(1, 2)
# print(pt._x, pt.__y)
pt.__set_coord(1, 2, 3)