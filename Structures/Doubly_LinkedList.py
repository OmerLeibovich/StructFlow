import sys
import pygame
import random
import time
from tkinter import messagebox, Tk
from Screen import *


Title = initialize_screen("Doubly LinkedList")


# Node class
class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.next = None
        self.prev = None

# DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.highlighted_node = None
        self.mode = "head"  # Default mode is "head"

    def add(self, value):
        new_node = Node(value, NODE_SPACING, ROW_SPACING)
        if self.mode == "head":
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif self.mode == "tail":
            if not self.tail:
                self.head = self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node

        self.update_positions()

    def remove_last(self):
        if not self.head:
            return

        if self.mode == "head":
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif self.mode == "tail":
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

        self.update_positions()

    def update_positions(self):
        current = self.head
        x = NODE_SPACING
        y = ROW_SPACING
        while current:
            current.x = x
            current.y = y

            if x + NODE_SPACING * 2 > SCREEN_WIDTH:
                x = NODE_SPACING
                y += ROW_SPACING
            else:
                x += NODE_SPACING

            current = current.next

            if y + ROW_SPACING > SCREEN_HEIGHT:
                print("Error: Linked list exceeds screen height!")
                break

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        current = self.head
        previous = None
        while current:
            color = (255, 0, 0) if current == self.highlighted_node else BLUE
            pygame.draw.circle(screen, color, (current.x, current.y), NODE_RADIUS)
            text_surface = font.render(str(current.value), True, WHITE)
            text_rect = text_surface.get_rect(center=(current.x, current.y))
            screen.blit(text_surface, text_rect)

            if previous and current.y > previous.y:
                pygame.draw.line(screen, BLACK, (25, current.y),
                                 (current.x - NODE_RADIUS, current.y), 3)
                arrow_head = [(current.x - NODE_RADIUS - 5, current.y - 5),
                              (current.x - NODE_RADIUS - 5, current.y + 5),
                              (current.x - NODE_RADIUS, current.y)]
                pygame.draw.polygon(screen, BLACK, arrow_head)

            if current.next and current.y == current.next.y:
                pygame.draw.line(screen, BLACK, (current.x + NODE_RADIUS, current.y),
                                 (current.next.x - NODE_RADIUS, current.next.y), 3)
                arrow_head = [(current.next.x - NODE_RADIUS - 5, current.next.y - 5),
                              (current.next.x - NODE_RADIUS - 5, current.next.y + 5),
                              (current.next.x - NODE_RADIUS, current.next.y)]
                pygame.draw.polygon(screen, BLACK, arrow_head)

            previous = current
            current = current.next

    def search_value(self, value):
        current = self.head if self.mode == "head" else self.tail
        last_checked_node = None  # משתנה כדי לזכור את האיבר האחרון שנבדק
        while current:
            # Highlight the node being checked
            self.highlighted_node = current
            last_checked_node = current  # שמור את האיבר הנוכחי
            self.draw(screen)
            pygame.display.update()
            pygame.time.delay(500)

            if current.value == value:
                return f"Value {value} found."

            current = current.next if self.mode == "head" else current.prev

        # אם לא נמצא, הגדר את האיבר האחרון חזרה לכחול
        if last_checked_node:
            self.highlighted_node = None  # נקה את ההדגשה
            self.draw(screen)
            pygame.display.update()
            pygame.time.delay(500)

        return f"Value {value} not found."

    def reset_highlight(self):
        self.highlighted_node = None
        self.draw(screen)
        pygame.display.update()

# Draw buttons
def draw_buttons(screen, font, mode):
    head_button_rect = pygame.Rect(50, SCREEN_HEIGHT - 592, BUTTON_WIDTH, BUTTON_HEIGHT)
    tail_button_rect = pygame.Rect(SCREEN_WIDTH - 150, SCREEN_HEIGHT - 592, BUTTON_WIDTH, BUTTON_HEIGHT)

    # Shadow
    shadow_offset = 5
    pygame.draw.rect(screen, (180, 180, 180), head_button_rect.move(shadow_offset, shadow_offset))
    pygame.draw.rect(screen, (180, 180, 180), tail_button_rect.move(shadow_offset, shadow_offset))

    # Button rectangles with border
    pygame.draw.rect(screen, BLACK if mode == "head" else WHITE, head_button_rect)
    pygame.draw.rect(screen, BLACK if mode == "tail" else WHITE, tail_button_rect)
    pygame.draw.rect(screen, BLACK, head_button_rect, 2)  # Border
    pygame.draw.rect(screen, BLACK, tail_button_rect, 2)  # Border

    # Text
    head_text = font.render("Head", True, WHITE if mode == "head" else BLACK)
    tail_text = font.render("Tail", True, WHITE if mode == "tail" else BLACK)

    screen.blit(head_text, (head_button_rect.x + 20, head_button_rect.y + 10))
    screen.blit(tail_text, (tail_button_rect.x + 28, tail_button_rect.y + 10))

    return head_button_rect, tail_button_rect


# Main function
def Run_DoublyLinkedList():
    Tk().wm_withdraw()
    messagebox.showinfo("Tutorial",
                        "Arrow Keys:\n"
                        "UP: Add node\n"
                        "DOWN: Remove node\n"
                        "SPACE: Clear list\n"
                        "S: Search for a value\n"
                        "Use the buttons to switch between Head and Tail modes")

    dll = DoublyLinkedList()
    running = True
    user_input = ""
    search_result = ""
    search_start_time = None
    error_message = ""  # משתנה לשמירת הודעת שגיאה
    error_message_start_time = None  # זמן תחילת הודעת השגיאה
    font = pygame.font.Font(None, 36)

    while running:
        screen.fill(WHITE)
        dll.update_positions()
        dll.draw(screen)

        # Draw buttons
        head_button_rect, tail_button_rect = draw_buttons(screen, font, dll.mode)

        # Display current input
        input_text = font.render(f"Enter a Number: {user_input}", True, BLACK)
        screen.blit(input_text, (300, 10))

        # Display search result
        if search_result and search_start_time:
            if time.time() - search_start_time < 3:
                search_text = font.render(search_result, True, BLACK)
                search_rect = search_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(search_text, search_rect)
            else:
                search_result = ""

        # Display error message
        if error_message and error_message_start_time:
            if time.time() - error_message_start_time < 3:
                error_text = font.render(error_message, True, (255, 0, 0))
                error_rect = error_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
                screen.blit(error_text, error_rect)
            else:
                error_message = ""

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:  # Add node
                    if user_input.isdigit() and 0 <= int(user_input) <= 100:
                        dll.reset_highlight()
                        dll.add(int(user_input))
                    else:
                        error_message = "Error: The number must be between 0 and 100"
                        error_message_start_time = time.time()
                    user_input = ""
                elif event.key == pygame.K_DOWN:  # Remove node
                    dll.remove_last()
                elif event.key == pygame.K_SPACE:  # Clear list
                    dll = DoublyLinkedList()
                    search_result = ""
                elif event.key == pygame.K_s:  # Search value
                    if user_input.isdigit() and 0 <= int(user_input) <= 100:
                        search_result = dll.search_value(int(user_input))
                        search_start_time = time.time()
                    else:
                        error_message = "Error: The number must be between 0 and 100"
                        error_message_start_time = time.time()
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.unicode.isdigit():
                    user_input += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if head_button_rect.collidepoint(event.pos):
                        dll.mode = "head"
                    elif tail_button_rect.collidepoint(event.pos):
                        dll.mode = "tail"

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    Run_DoublyLinkedList()
