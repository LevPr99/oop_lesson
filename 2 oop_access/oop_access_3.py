class Clock:
    
    def __init__(self, time=0) -> None:
        self.__time = time
    
    @staticmethod
    def __check_time(tm):
        return isinstance(tm, int) and tm >= 0 and tm < 100000
    
    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm
            
    def get_time(self):
        return self.__time

        
clock = Clock(4530)