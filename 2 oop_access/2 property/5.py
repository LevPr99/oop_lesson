class WindowDlg:
    
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.__flag = (self.width, self.height)
    
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
            self.__check_fl()
            
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width, max = (0, 10000)):
        if max[0] <= width <= max[1]:
            self.__width = width
            self.__check_fl()
            
    def __check_fl(self):
        if '_WindowDlg__flag' in self.__dict__:
            if self.__flag[0] != self.width or self.__flag[1] != self.height:
                self.show()
                self.__flag = (self.width, self.height)
            
    def show(self):
        print(f"{self.title}: {self.width}, {self.height}")

wdl = WindowDlg('Hello', 10, 11)
wdl.show()
