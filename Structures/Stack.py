import pygame
from Screen import *
import DrawArray
import time

pygame.display.set_caption("Stack Visualizer")
class StackVisualizer:
    def __init__(self):
        self.stack = []

    def push(self, value, color = YELLOW):
        max_items = (SCREEN_HEIGHT - 220) // (RECT_HEIGHT + 10)

        if len(self.stack) < max_items:
            self.stack = [(v, WHITE) for v, _ in self.stack]
            self.stack.append((value, color))
            self.draw_explanation(f"{value} inserted to the stack")
            pygame.display.update()
            pygame.time.wait(2000)
            self.draw_stack()

    def pop(self):
        if self.stack:
            self.stack = [(v, WHITE) for v, _ in self.stack]
            if self.stack:
                self.stack[-1] = (self.stack[-1][0],RED)
                value = self.stack[-1][0]
                self.draw_stack()
                DrawArray.draw_text(font, error_message, user_input)
                pygame.display.update()
                pygame.time.wait(3000)
            self.stack.pop()
            self.draw_stack()
            self.draw_explanation(f"{value} removed from the top of stack")
            DrawArray.draw_text(font, error_message, user_input)
            pygame.display.update()
            pygame.time.wait(2000)

    def peek(self):
        if self.stack:
            return self.stack[-1][0]
        return None

    def draw_stack(self):
        clear_screen()

        for i, (value, color) in enumerate(reversed(self.stack)):
            x = SCREEN_WIDTH // 2 - RECT_WIDTH // 2
            y = 220 + (i * (RECT_HEIGHT + 10))

            if y + RECT_HEIGHT > SCREEN_HEIGHT:
                break

            pygame.draw.rect(screen, color, (x, y, RECT_WIDTH, RECT_HEIGHT))
            pygame.draw.rect(screen, BLACK, (x, y, RECT_WIDTH, RECT_HEIGHT), 2)

            text = font.render(str(value), True, BLACK)
            text_rect = text.get_rect(center=(x + RECT_WIDTH // 2, y + RECT_HEIGHT // 2))
            screen.blit(text, text_rect)

    def draw_explanation(self, message):
        DrawArray.draw_explanation(message)


running = True
user_input = ""
error_message = ""
message_time = None
stack = StackVisualizer()

while running:
    clear_screen()

    stack.draw_stack()

    if message_time and time.time() - message_time > 3:
        error_message = ""
        message_time = None

    DrawArray.draw_text(font, error_message, user_input)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                max_items = (SCREEN_HEIGHT - 220) // (RECT_HEIGHT + 10)

                if user_input:
                    if len(stack.stack) < max_items:
                        stack.push(int(user_input))
                        user_input = ""
                    else:
                        error_message = "Stack is full!"
                        user_input = ""
                        message_time = time.time()
                else:
                    error_message = "Please enter a number first."
                    message_time = time.time()


            elif event.key == pygame.K_DOWN:
                    stack.pop()

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            elif event.unicode.isdigit():
                user_input += event.unicode
