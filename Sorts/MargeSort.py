import time
from Screen import *
from Structures.DrawArray import draw_array, draw_explanation, draw_text
def merge_sort(array, error_message, user_input, left=0, right=None):
    if right is None:
        right = len(array) - 1

    if left < right:
        mid = (left + right) // 2


        clear_screen()
        draw_text(font, error_message, user_input)
        draw_array(array, highlight_indices=list(range(left, mid + 1)), move_index=mid)
        draw_explanation(f"Splitting: {array[left:mid+1]} | {array[mid+1:right+1]}")
        time.sleep(1)

        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right, error_message, user_input)


def merge(array, left, mid, right, error_message, user_input):
    left_part = array[left:mid + 1]
    right_part = array[mid + 1:right + 1]

    i = j = 0
    k = left


    clear_screen()
    draw_text(font, error_message, user_input)
    draw_array(left_part, highlight_indices=[], move_index=None, insert_index=None, y_offset=-100)  # חלק שמאלי למעלה
    draw_array(right_part, highlight_indices=[], move_index=None, insert_index=None, y_offset=100)   # חלק ימני למטה
    time.sleep(1)

    while i < len(left_part) and j < len(right_part):
        clear_screen()
        draw_text( font, error_message, user_input)

        # ציור שני המערכים
        draw_array(left_part, highlight_indices=[i], y_offset=-100)
        draw_array(right_part, highlight_indices=[j], y_offset=100)
        draw_array(array, highlight_indices=[k])
        time.sleep(1)

        if left_part[i] < right_part[j]:
            draw_explanation(f"{left_part[i]} lower then {right_part[j]}, Therefore the next member that insert to array is {left_part[i]}")
            time.sleep(3)
            array[k] = left_part[i]
            i += 1
        else:
            draw_explanation(f"{right_part[j]} lower then {left_part[i]}, Therefore the next member that insert to array is {right_part[j]}")
            time.sleep(3)
            array[k] = right_part[j]
            j += 1
        k += 1


    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1


    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1


    clear_screen()
    draw_text(font, error_message, user_input)
    draw_array(array, highlight_indices=list(range(left, right + 1)))
    time.sleep(1)
