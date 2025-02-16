import time
from Screen import *
from Structures.DrawArray import draw_array, draw_explanation, draw_text
def insertion_sort(array,error_message, user_input):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        clear_screen()
        draw_text( font, error_message, user_input)
        draw_array(array,highlight_indices=[i])
        draw_explanation(f"Checking number {key}, searching for correct position")
        time.sleep(1)

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            clear_screen()
            draw_text( font, error_message, user_input)
            draw_array(array, highlight_indices=[j + 1])
            draw_explanation(f"{array[j+1]} is greater than {key}, shifting it right")
            time.sleep(1)

        array[j + 1] = key
        clear_screen()
        draw_text(font, error_message, user_input)
        draw_array(array, insert_index=j + 1)
        draw_explanation(f"Inserting {key} at position {j + 1}")
        time.sleep(1)

    clear_screen()
    draw_text(font, error_message, user_input)
    draw_array(array)
    draw_explanation("Sorting completed! The array is now sorted ✅")
