class ListItem:
    def __init__(s, value):
        s.value = value
        s.next = None
        s.before = None

class List:
    def __init__(s, start_value):
        s.first = ListItem(start_value)
        s.last = s.first
        s.size = 1
        
    def print(s):
        item = s.first
        while item.next != s.last:
            print(item.value)
            item = item.next
        print(s.last.value)

    def pop(s, id_remove):
        if id_remove < 0 or id_remove >= s.size:
            return
        
        s.size -= 1
        if id_remove == 0:
            s.first = s.first.next
            s.first.before = None
            return
        if  id_remove == s.size - 1:
            s.last = s.last.before
            s.last.next = None
            return
        
        item = s.first
        id = 0
        while item.next != s.last:
            if id == id_remove:
                item.before.next = item.next
                item.next.before = item.before
            item = item.next
            id += 1
