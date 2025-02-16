import time
from Screen import *
from Structures.DrawArray import draw_array, draw_explanation, draw_text
def selection_sort(array, error_message, user_input):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            clear_screen()
            draw_text( font, error_message, user_input)
            draw_array(array, highlight_indices=[j], move_index=min_index)
            draw_explanation(f"Current minimum: {array[min_index]}")
            time.sleep(1)

            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
        time.sleep(1)

        clear_screen()
        draw_text( font, error_message, user_input)
        draw_array(array, highlight_indices=[i])
        time.sleep(1)

    clear_screen()
    draw_text( font, error_message, user_input)
    draw_array(array)
    draw_explanation("Sorting completed! ✅")