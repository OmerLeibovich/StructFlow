import sys

import time
from Screen import *
from Structures import DrawArray
from Sorts import BubbleSort,CountingSort,HeapSort,InsertionSort,MargeSort,QuickSort,SelectionSort


Title = initialize_screen("Sort Visualizer")



# Main program
array = []
running = True
user_input = ""
error_message = ""
message_time = None

while running:
    clear_screen()

    if message_time and time.time() - message_time > 3:
        error_message = ""
        message_time = None

    DrawArray.draw_text(font, error_message, user_input)
    DrawArray.draw_array(array)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                try:
                    if len(array) < MAX_ARRAY_SIZE:
                        if user_input.isdigit():
                            number = int(user_input)
                            if number <= 999:
                                array.append(number)
                                user_input = ""
                                error_message = ""
                            else:
                                error_message = "The input must be less than 1000"
                                message_time = time.time()
                        else:
                            error_message = "Please enter a valid number."
                            message_time = time.time()
                    else:
                        error_message = "Array size limit reached (14)."
                        message_time = time.time()
                except ValueError:
                    error_message = "Please enter a valid number."
                    message_time = time.time()

            elif event.key == pygame.K_DOWN:
                try:
                    if user_input.isdigit():
                        number = int(user_input)
                        if number <= 999 and number in array:
                            array.remove(number)
                            user_input = ""
                            error_message = ""
                        else:
                            error_message = f"Number {number} not found in array."
                            message_time = time.time()
                    else:
                        error_message = "Please enter a valid number to remove."
                        message_time = time.time()
                except ValueError:
                    error_message = "Please enter a valid number to remove."
                    message_time = time.time()

            elif event.key == pygame.K_SPACE:
                array = []
                user_input = ""

            elif event.key == pygame.K_s:
                BubbleSort.bubble_sort(array,error_message,user_input)

            elif event.key == pygame.K_i:
                InsertionSort.insertion_sort(array,error_message,user_input)

            elif event.key == pygame.K_a:
                SelectionSort.selection_sort(array,error_message,user_input)

            elif event.key == pygame.K_m:
                MargeSort.merge_sort(array,error_message,user_input)

            elif event.key == pygame.K_q:
                QuickSort.quick_sort(array,error_message,user_input)

            elif event.key == pygame.K_c:
                array = CountingSort.counting_sort(array,error_message,user_input)

            elif event.key == pygame.K_h:
                HeapSort.heap_sort(array,error_message,user_input)

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            elif event.unicode.isdigit():
                user_input += event.unicode

pygame.quit()
sys.exit()