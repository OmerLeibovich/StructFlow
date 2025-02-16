import time
from Screen import *
from Structures.DrawArray import draw_array, draw_explanation, draw_text


def quick_sort(array, error_message, user_input, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = improved_partition(array, low, high, error_message, user_input)
        quick_sort(array, error_message, user_input, low, pivot_index - 1)
        quick_sort(array, error_message, user_input, pivot_index + 1, high)


def median_of_three(array, low, high):
    """ בוחר את הפיווט בצורה חכמה יותר: מדיאן משלושה """
    mid = (low + high) // 2
    pivot_candidates = [array[low], array[mid], array[high]]
    pivot_candidates.sort()
    return pivot_candidates[1]  # הערך האמצעי מבין השלושה


def improved_partition(array, low, high, error_message, user_input):
    pivot = median_of_three(array, low, high)  # בחירת פיווט חכמה יותר
    pivot_index = array.index(pivot)

    # העברת הפיווט לסוף (כדי להשתמש באותו אלגוריתם)
    array[pivot_index], array[high] = array[high], array[pivot_index]

    i = low - 1
    for j in range(low, high):
        clear_screen()
        draw_text(array, font, error_message, user_input)
        draw_array(array, highlight_indices=[j, high])
        time.sleep(2)

        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    clear_screen()
    draw_text(array, font, error_message, user_input)
    draw_array(array, highlight_indices=[i + 1])
    time.sleep(2)

    return i + 1  # מחזיר את האינדקס החדש של הפיווט
