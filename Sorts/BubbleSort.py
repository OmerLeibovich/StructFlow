import time
from Screen import *
from Structures.DrawArray import draw_array, draw_explanation, draw_text

def bubble_sort(array,error_message,user_input):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            clear_screen()
            draw_text( font,error_message,user_input)
            draw_array(array, highlight_indices=[j, j + 1])
            update_screen()
            time.sleep(1)

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                clear_screen()
                draw_text(array, font,error_message,user_input)
                draw_array(array, highlight_indices=[j, j + 1])
                draw_explanation(f"{array[j]} is lower than {array[j + 1]}, replace them")
                update_screen()
                time.sleep(1)

    clear_screen()
    draw_text(array, font,error_message,user_input)
    draw_array(array)
    update_screen()
