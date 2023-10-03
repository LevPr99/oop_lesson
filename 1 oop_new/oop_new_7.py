class Viber:
    
    msg_list = list()
    
    @classmethod
    def add_message(cls, msg):
        cls.msg_list.append(msg)
    
    @classmethod
    def remove_message(cls, msg):
        cls.msg_list.remove(msg)
        
    @staticmethod   
    def set_like(msg):
        msg.fl_like = True if msg.fl_like == False else False
    
    @classmethod
    def show_last_message(cls, var):
        return cls.msg_list[var:]
    
    @classmethod    
    def total_messages(cls):
        return len(cls.msg_list)
    
    
class Message:
    
    def __init__(self, text, fl_like = False):
        self.text = text
        self.fl_like = fl_like