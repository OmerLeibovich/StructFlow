import time
from Screen import *
from Structures.DrawArray import draw_array, draw_explanation, draw_text
def heap_sort(array,error_message, user_input):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        clear_screen()
        draw_text(font, error_message, user_input)
        draw_array(array, highlight_indices=[i])
        time.sleep(2)
        heapify(array, i, 0)

def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

