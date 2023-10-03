class Data:
    
    def __init__(self, data, dest_ip):
        self.ip = dest_ip
        self.data = data


class Router:
    
    buffer = list()
    
    def __init__(self) -> None:
        self.servers_lst = list()
    
    def link(self, server):
        self.servers_lst.append(server)
    
    def unlink(self, server):
        self.servers_lst.remove(server)
    
    def send_data(self):
        # self.servers_lst.setdefault(0, '')
        for i in self.servers_lst:
            for j in self.buffer:
                if i.ip == j.ip:
                    i.data = j.data
        self.buffer.clear()

class Server:
    
    IP = 0
    
    def __new__(cls, *args, **kwargs):
        cls.IP += 1
        return super().__new__(cls)
    
    def __init__(self) -> None:
        self.ip = self.IP
        self.buffer = list()
    
    @staticmethod
    def send_data(data : Data):
        Router.buffer.append(data)
    
    def get_data(self):
        data = self.buffer.copy()
        self.buffer.clear()
        return data
    
    def get_ip(self):
        return self.ip
    
    
    
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
print(msg_lst_from)
msg_lst_to = sv_to.get_data()
print(msg_lst_to)
