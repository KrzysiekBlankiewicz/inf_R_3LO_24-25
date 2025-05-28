class ListItem:
    def __init__(s, value):
        s.value = value
        s.next = None
        s.before = None

class List:
    def __init__(s, start_value = None):
        if start_value != None:
            s.first = ListItem(start_value)
            s.last = s.first
            s.size = 1
        else:
            s.first = None
            s.last = None
            s.size = 0
        
    def print(s):
        if s.size == 0:
            return
        item = s.first
        while item != s.last:
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
    def addon(s, value):
        item = ListItem(value)
        if s.size == 0:
            s.first = item
            s.last = item
        else: 
            s.last.next = item
            item.before = s.last
            s.last = item
    def find(s,look):
        looki = ListItem(look)
        badana = s.first
        if s.size == 0:
            return False
        while badana.value != looki.value: 
            if badana.next == looki.value
                return True
            else:
                badana = badana.next
        return False
