import pygame
import time
from Screen import *
import DrawArray

pygame.display.set_caption("Queue Visualizer")

class QueueVisualizer:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        max_items = (SCREEN_HEIGHT - 200) // (RECT_HEIGHT + SPACING)

        if len(self.queue) < max_items:
            self.queue = [(val, WHITE) for val, _ in self.queue]
            self.queue.append((value, YELLOW))

            self.draw_explanation(f"{value} inserted to the queue")
            pygame.display.update()
            pygame.time.wait(1000)
            self.draw_queue()
        else:
            self.draw_explanation("Queue is full!")
            pygame.display.update()
            pygame.time.wait(1000)

    def dequeue(self):

        if self.queue:
            if self.queue:
                self.queue = [(val, WHITE) for val, _ in self.queue[:-1]] + [(self.queue[-1][0], WHITE)]
            else:
                self.queue = []
            self.queue[0] = (self.queue[0][0], RED)
            self.draw_queue()
            DrawArray.draw_text(font, error_message, user_input)
            pygame.display.update()
            pygame.time.wait(1000)
            value = self.queue.pop(0)[0]
            self.draw_queue()
            self.draw_explanation(f"{value} removed from the queue")
            DrawArray.draw_text(font, error_message, user_input)
            pygame.display.update()
            pygame.time.wait(1000)
        else:
            self.draw_explanation("Queue is empty!")
            pygame.display.update()
            pygame.time.wait(1000)


    def peek(self):
        return self.queue[0][0] if self.queue else None

    def draw_queue(self):
        clear_screen()
        for i, (value, color) in enumerate(self.queue):
            x = QUEUE_START_X
            y = 220 + (i * (RECT_HEIGHT + 10))
            pygame.draw.rect(screen, color, (x, y, RECT_WIDTH, RECT_HEIGHT))
            pygame.draw.rect(screen, BLACK, (x, y, RECT_WIDTH, RECT_HEIGHT), 2)
            text = font.render(str(value), True, BLACK)
            text_rect = text.get_rect(center=(x + RECT_WIDTH // 2, y + RECT_HEIGHT // 2))
            screen.blit(text, text_rect)

    def draw_explanation(self, message):
        DrawArray.draw_explanation(message)




running = True
queue = QueueVisualizer()
user_input = ""
error_message = ""
message_time = None
while running:
    clear_screen()
    queue.draw_queue()
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
                    if len(queue.queue) < max_items:
                        queue.enqueue(int(user_input))
                        user_input = ""
                    else:
                        error_message = "Stack is full!"
                        user_input = ""
                        message_time = time.time()
                else:
                    error_message = "Please enter a number first."
                    message_time = time.time()
            elif event.key == pygame.K_DOWN:
                queue.dequeue()
                user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.unicode.isdigit():
                user_input += event.unicode

