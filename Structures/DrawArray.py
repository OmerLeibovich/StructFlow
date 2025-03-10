
from Screen import *

def draw_array(array, highlight_indices=None, move_index=None, insert_index=None, y_position="center", show_indices=False):

    if highlight_indices is None:
        highlight_indices = []

    if y_position == "top":
        y_offset = -50
    elif y_position == "bottom":
        y_offset = 50
    else:
        y_offset = 0

    for i, value in enumerate(array):
        x = i * RECT_WIDTH + SPACING if i != 0 else SPACING
        y = SCREEN_HEIGHT // 2 - RECT_HEIGHT // 2 + y_offset

        if i in highlight_indices:
            color = (255, 255, 0)
        elif move_index is not None and i == move_index:
            color = RED
        elif insert_index is not None and i == insert_index:
            color = (0, 255, 0)
        else:
            color = WHITE

        pygame.draw.rect(screen, color, (x, y, RECT_WIDTH, RECT_HEIGHT))
        pygame.draw.rect(screen, BLACK, (x, y, RECT_WIDTH, RECT_HEIGHT), 2)

        text = font.render(str(value), True, BLACK)
        text_rect = text.get_rect(center=(x + RECT_WIDTH // 2, y + RECT_HEIGHT // 2))
        screen.blit(text, text_rect)

        if show_indices:
            index_text = font.render(str(i), True, (100, 100, 100))
            index_rect = index_text.get_rect(center=(x + RECT_WIDTH // 2, y + RECT_HEIGHT // 2 + 20))
            screen.blit(index_text, index_rect)

    update_screen()

def draw_explanation(text):
    font = pygame.font.Font(None, 40)
    explanation_text = font.render(text, True, BLACK)

    text_rect = explanation_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
    screen.blit(explanation_text, text_rect)
    update_screen()



def draw_text(font_Input,error_message,user_input):
    font_Message = pygame.font.Font(None, 50)
    input_text = font_Input.render(f"Enter a Number: {user_input}", True, BLACK)
    screen.blit(input_text, (300, 10))

    if error_message:
        error_text = font_Message.render(error_message, True, RED)
        text_rect = error_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        screen.blit(error_text, text_rect)
