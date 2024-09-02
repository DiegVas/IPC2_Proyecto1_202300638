class NodeRow:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.value_next = None  # Para enlazar múltiples valores


class CustomDict:
    def __init__(self):
        self.head = None

    def add(self, key, value):
        if not self.head:
            self.head = NodeRow(key, value)
        else:
            current = self.head
            while current.next:
                if current.key == key:
                    self._add_value(current, value)
                    return
                current = current.next
            if current.key == key:
                self._add_value(current, value)
            else:
                current.next = NodeRow(key, value)

    def _add_value(self, node, value):
        current_value = node
        while current_value.value_next:
            current_value = current_value.value_next
        current_value.value_next = NodeRow(node.key, value)

    def get(self, key):
        current = self.head
        while current:
            if current.key == key:
                return self._get_values(current)
            current = current.next
        return None

    def _get_values(self, node):
        values = []
        current_value = node
        while current_value:
            values.append(current_value.value)
            current_value = current_value.value_next
        return values

    def values(self):
        current = self.head
        while current:
            yield self._get_values(current)
            current = current.next
