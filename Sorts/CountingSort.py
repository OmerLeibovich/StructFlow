import time
from Screen import *
from Structures.DrawArray import draw_array, draw_explanation, draw_text
def counting_sort(array,error_message,user_input):
    max_val = max(array)
    min_val = min(array)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    sorted_array = [0] * len(array)

    for num in array:
        count[num - min_val] += 1

        clear_screen()
        draw_text(array, font, error_message, user_input)
        draw_array(array, y_position="top")
        draw_array(count, y_position="bottom", highlight_indices=[num - min_val])
        draw_explanation(f"Counting: Number {num} appears {count[num - min_val]} times")
        time.sleep(1)

    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    clear_screen()
    draw_text(array, font, error_message, user_input)
    draw_array(count, y_position="bottom", highlight_indices=range(len(count)))
    draw_explanation("Cumulative count array ready")
    time.sleep(2)

    for i in range(len(array) - 1, -1, -1):
        num = array[i]
        sorted_index = count[num - min_val] - 1
        sorted_array[sorted_index] = num
        count[num - min_val] -= 1

        clear_screen()
        draw_text(array, font, error_message, user_input)
        draw_array(count, y_position="bottom", highlight_indices=[num - min_val])
        draw_array(sorted_array, highlight_indices=[sorted_index], y_position="top")
        draw_explanation(f"Placing {num} at position {sorted_index} in sorted array")
        time.sleep(2)

    clear_screen()
    draw_text(array, font, error_message, user_input)
    draw_array(array, y_position="bottom")
    draw_array(sorted_array, y_position="top")
    draw_explanation("Sorting completed!")
    update_screen()

    time.sleep(3)

    return sorted_array
