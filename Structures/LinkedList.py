import sys
import pygame
import random
import time
from tkinter import messagebox,Tk
from Screen import *


Title = initialize_screen("Linked List Visualization")



# Node class
class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.highlighted_node = None

    def add(self, value):
        if not self.head:
            self.head = Node(value, NODE_SPACING, ROW_SPACING)
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
            # Determine new node position
            new_x = current.x + NODE_SPACING
            new_y = current.y
            if new_x + NODE_RADIUS * 2 > SCREEN_WIDTH:  # Move to next row
                new_x = NODE_SPACING
                new_y += ROW_SPACING
            current.next = Node(value, new_x, new_y)

    def remove_last(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            self.update_positions()
            return


        current = self.head
        while current.next and current.next.next:
            current = current.next


        current.next = None
        self.update_positions()

    def update_positions(self):
        current = self.head
        x = NODE_SPACING
        y = ROW_SPACING
        while current:
            current.x = x
            current.y = y

            # Check if the next node will fit within the current row
            if x + NODE_SPACING * 2 > SCREEN_WIDTH:  # Move to the next row if needed
                x = NODE_SPACING  # Reset x position
                y += ROW_SPACING  # Move to the next row
            else:
                x += NODE_SPACING  # Move to the next position in the row

            current = current.next

            # If the new row exceeds the screen height, break to avoid "sticking"
            if y + ROW_SPACING > SCREEN_HEIGHT:
                print("Error: Linked list exceeds screen height!")
                break

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        current = self.head
        previous = None  # To keep track of the previous node
        while current:
            # קובע צבע בהתאם למצב התא
            if current == self.highlighted_node:
                color = (255, 0, 0)  # צובע באדום את התא התואם
            else:
                color = BLUE  # הצבע הרגיל של התאים

            # Draw the node
            pygame.draw.circle(screen, color, (current.x, current.y), NODE_RADIUS)
            text_surface = font.render(str(current.value), True, WHITE)
            text_rect = text_surface.get_rect(center=(current.x, current.y))
            screen.blit(text_surface, text_rect)

            # If it's the first node in a new row, draw an arrow from the previous row
            if previous and current.y > previous.y:
                # Draw a line from the start of the screen to the first node in the new row
                pygame.draw.line(screen, BLACK, (25, current.y),
                                 (current.x - NODE_RADIUS, current.y), 3)
                # Draw arrow head
                arrow_head = [(current.x - NODE_RADIUS - 5, current.y - 5),
                              (current.x - NODE_RADIUS - 5, current.y + 5),
                              (current.x - NODE_RADIUS, current.y)]
                pygame.draw.polygon(screen, BLACK, arrow_head)

            # Draw the arrow to the next node if they are on the same row
            if current.next and current.y == current.next.y:
                pygame.draw.line(screen, BLACK, (current.x + NODE_RADIUS, current.y),
                                 (current.next.x - NODE_RADIUS, current.next.y), 3)
                arrow_head = [(current.next.x - NODE_RADIUS - 5, current.next.y - 5),
                              (current.next.x - NODE_RADIUS - 5, current.next.y + 5),
                              (current.next.x - NODE_RADIUS, current.next.y)]
                pygame.draw.polygon(screen, BLACK, arrow_head)

            # Move to the next node
            previous = current
            current = current.next

    def Search_Value(self, screen, value):
        font = pygame.font.Font(None, 36)
        count = 0
        if not self.head:  # אם הרשימה ריקה
            return "The list is empty"

        current = self.head
        while current:
            # צובע את התא הנוכחי באדום (מסמן אותו כנבדק)
            pygame.draw.circle(screen, (255, 0, 0), (current.x, current.y), NODE_RADIUS)
            text_surface = font.render(str(current.value), True, WHITE)
            text_rect = text_surface.get_rect(center=(current.x, current.y))
            screen.blit(text_surface, text_rect)

            # עדכון המסך
            pygame.display.update()

            # בדיקה אם הערך תואם
            if current.value == value:
                self.highlighted_node = current  # מסמן את הצומת התואם
                pygame.display.update()  # מעדכן את המסך כדי להציג את הצביעה
                return f"Value {value} found at node in LinkedList [{count}]"

            # המתנה קצרה כדי להדגיש את החיפוש
            pygame.time.delay(500)

            # אם אין התאמה, מסיר את הצבע האדום (מחזיר לצבע המקורי)
            pygame.draw.circle(screen, BLUE, (current.x, current.y), NODE_RADIUS)
            text_surface = font.render(str(current.value), True, WHITE)
            text_rect = text_surface.get_rect(center=(current.x, current.y))
            screen.blit(text_surface, text_rect)

            # עדכון המסך שוב
            pygame.display.update()

            # מעבר לתא הבא
            current = current.next
            count +=1

        # אם הערך לא נמצא
        return f"Value {value} not found in the Linkedlist"

    def reset_highlight(self):
        """איפוס הצומת המסומן"""
        self.highlighted_node = None
        self.draw(screen)
        pygame.display.update()


def Run_LinkedList():
    Tk().wm_withdraw()
    messagebox.showinfo("Tutorial\n",
                        "Left Clicker : Choose where you want to put the graph points\nRight Clicker : press and Drag to connect between graph points\n\n\n"
                        "After you finish building the Graph:\n\nDown Button: Press to give random numbers to the arcs \n"
                        "Up Button: Press a few times to see how to find the shortest path\n\n\nCan press Space to clear")
    # Main program
    linked_list = LinkedList()
    running = True
    user_input = ""
    search_result = ""
    message_start_time = None




    def display_message(screen, text, font, color, y_offset=0):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        screen.blit(text_surface, text_rect)

    # משתנים עבור הודעות
    error_message = ""
    error_message_start_time = None
    font = pygame.font.Font(None, 36)

    while running:
        screen.fill(WHITE)
        linked_list.update_positions()
        linked_list.draw(screen)

        # Display current input
        input_text = font.render(f"Enter a Number: {user_input}", True, BLACK)
        screen.blit(input_text, (300, 10))

        # Display error message
        if error_message and error_message_start_time:
            if time.time() - error_message_start_time < 3:
                display_message(screen, error_message, font, BLACK)
            else:
                error_message = ""
                error_message_start_time = None

        # Display search result
        if search_result and message_start_time:
            if time.time() - message_start_time < 3:
                display_message(screen, search_result, font, BLACK)
            else:
                search_result = ""
                message_start_time = None

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:  # Add number
                    if user_input.isdigit() and 0 <= int(user_input) <= 100:
                        linked_list.reset_highlight()
                        linked_list.add(int(user_input))
                    else:
                        error_message = "The number needs to be between 0 and 100"
                        error_message_start_time = time.time()
                    user_input = ""
                elif event.key == pygame.K_DOWN:  # Remove number
                    linked_list.remove_last()
                elif event.key == pygame.K_RIGHT:  # Search value
                    if user_input.isdigit() and 0 <= int(user_input) <= 100:
                        linked_list.reset_highlight()
                        search_result = linked_list.Search_Value(screen, int(user_input))
                        message_start_time = time.time()
                    else:
                        error_message = "The number needs to be between 0 and 100"
                        error_message_start_time = time.time()
                    user_input = ""
                elif event.key == pygame.K_SPACE:
                    linked_list = LinkedList()
                    search_result = ""
                    error_message = ""
                    message_start_time = None
                    error_message_start_time = None
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.unicode.isdigit():
                    user_input += event.unicode

    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    Run_LinkedList()