# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
# -написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# -розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
# -написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def print_list(head):
    """Функція для виведення списку на екран."""
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def reverse_list(head):
    """Функція для реверсування однозв'язного списку."""
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def insertion_sort_list(head):
    """Функція для сортування однозв'язного списку за допомогою сортування вставками."""
    sorted_head = None
    current = head

    while current:
        next_node = current.next
        if not sorted_head or sorted_head.value >= current.value:
            current.next = sorted_head
            sorted_head = current
        else:
            sorted_curr = sorted_head
            while sorted_curr.next and sorted_curr.next.value < current.value:
                sorted_curr = sorted_curr.next
            current.next = sorted_curr.next
            sorted_curr.next = current
        current = next_node

    return sorted_head

def merge_sort_list(head):
    """Функція для сортування однозв'язного списку за допомогою сортування злиттям."""
    if not head or not head.next:
        return head

    def split_list(node):
        """Допоміжна функція для розділення списку на дві половини."""
        slow = fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        return node, second_half

    def merge_list(list1, list2):
        """Допоміжна функція для злиття двох відсортованих списків."""
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next

    first_half, second_half = split_list(head)
    sorted_first = merge_sort_list(first_half)
    sorted_second = merge_sort_list(second_half)
    return merge_list(sorted_first, sorted_second)

def merge_sorted_lists(l1, l2):
    """Функція для об'єднання двох відсортованих однозв'язних списків."""
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

# Приклади використання
if __name__ == "__main__":
    # Створення однозв'язних списків
    list1 = ListNode(1, ListNode(3, ListNode(5)))
    list2 = ListNode(2, ListNode(4, ListNode(6)))

    print("Original list1:")
    print_list(list1)
    print("Original list2:")
    print_list(list2)

    # Реверсування списку
    reversed_list1 = reverse_list(list1)
    print("\nReversed list1:")
    print_list(reversed_list1)

    # Сортування списку
    sorted_list1 = merge_sort_list(reversed_list1)
    print("\nSorted list1:")
    print_list(sorted_list1)

    # Об'єднання двох відсортованих списків
    merged_list = merge_sorted_lists(sorted_list1, list2)
    print("\nMerged list:")
    print_list(merged_list)

