from contacts.model import Contact

class Service:
    def __init__(self):
        pass

    @staticmethod
    def set_contact(name, phone, email, addr):
        return Contact(name, phone, email, addr)

    @staticmethod
    def get_contacts(params):
        contacts = [] #리스트
        for i in params: #for loop
            contacts.append(i.to_string())
        return ' '.join(contacts)

    @staticmethod
    def del_contact(params, name):
        for i, t in enumerate(params): #이넘. 인덱스값과 객체 하나를 끌어낸다.
            if t.name == name:
                del params[i] #i번째 있는 것을 지워버려라.
