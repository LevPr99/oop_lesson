class WindowDlg:
    
    def __init__(self, title, width, height):
        self.__check = {width, height}
        self.title = title
        self.width = width
        self.height = height
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title : str):
        if isinstance(title, str):
            self.__title = title
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height, max = (0, 10000)):
        if max[0] <= height <= max[1]:
            self.__height = height
            
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width, max = (0, 10000)):
        if max[0] <= width <= max[1]:
            self.__width = width
    
    def __check_fl(self):
        if self.width not in self.__check or self.height not in self.__check:
            self.show()
            
    def show(self):
        print(f"{self.title}: {self.width}, {self.height}")

wdl = WindowDlg('Hello', 10, 11)
# wdl.show()
wdl.height = 123
wdl.width = 222
wdl.show()
