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
            
    def add(s, value):
        new_item = ListItem(value)
        if s.size == 0:
            s.first = new_item
            s.last = new_item
        else:
            s.last.next = new_item
            new_item.before = s.last
            s.last = new_item
        s.size += 1

    def find(s, value_find):
        item = s.first
        index = 0
        while item is not None:
            if item.value == value_find:
                return index
            item = item.next
            index += 1
        return -1

    def erase(s):
        s.first = None
        s.last = None
        s.size = 0

l = List(7)
l.add(9)
l.add(9)
l.add(9)
l.add(9)
l.add(9)
l.print()

g = List()
