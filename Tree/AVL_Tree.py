from tkinter import Tk, messagebox
from collections import deque
from Tree import DFS_Search
from Tree import BFS_Search
import pygame
import sys
import random
from Screen import *


Title = initialize_screen("AVL Tree Visualization")



# AVL Tree class
class TreeNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.parent = parent
class AVLTree:
    def __init__(self):
        self.root = None
        self.visited = set()


    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key, parent=None):
        if node is None:
            return TreeNode(key, parent)
        if key < node.key:
            node.left = self._insert(node.left, key, node)
        else:
            node.right = self._insert(node.right, key, node)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node


    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp


            temp = self.get_min_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))


        balance = self._get_balance(node)


        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Right Heavy
        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node


    def get_min_node(self, node):
        return node if not node or not node.left else self.get_min_node(node.left)

    def _rotate_left(self, z):
        if z is None or z.right is None:
            return z
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, y):
        if y is None or y.left is None:
            return y
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def draw(self, x, y, node, level):
        if node:
            node_color = (255, 0, 0) if node.key in self.visited else BLACK
            pygame.draw.circle(screen, node_color, (x, y), NODE_RADIUS)
            font = pygame.font.Font(None, 36)
            text = font.render(str(node.key), True, WHITE)
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)

            line_offset = NODE_RADIUS

            if node.left:
                x_left = x - (SCREEN_WIDTH // (2 ** (level + 2)))
                y_left = y + 100
                pygame.draw.line(screen, BLACK, (x, y + line_offset), (x_left, y_left), 2)
                self.draw(x_left, y_left, node.left, level + 1)

            if node.right:
                x_right = x + (SCREEN_WIDTH // (2 ** (level + 2)))
                y_right = y + 100
                pygame.draw.line(screen, BLACK, (x, y + line_offset), (x_right, y_right), 2)
                self.draw(x_right, y_right, node.right, level + 1)

    def BFS(self, highest, BFS_order):

        return BFS_Search.BFS_Search(self, highest, BFS_order)

    def DFS(self, Stack, DFS_order):
        return DFS_Search.DFS_Search(self, Stack, DFS_order)


        pygame.display.update()

    def update_array(self, node, array, index=0):
        if node is not None:

            if index >= len(array):
                array.extend([None] * (index - len(array) + 1))


            array[index] = node.key


            self.update_array(node.left, array, 2 * index + 1)
            self.update_array(node.right, array, 2 * index + 2)
        else:

            if index < len(array):
                array[index] = None

def draw_array(screen, array, highlighted_numbers, targets, visited_nodes,algoritam):
    font = pygame.font.Font(None, 36)
    y_position = SCREEN_HEIGHT

    current_x = (SCREEN_WIDTH // 2) - (font.size("[" + ",".join(str(num) for num in array) + "]")[0] // 2)
    arrayTXT = font.render("Leafs:", True, BLACK)
    screen.blit(arrayTXT, (current_x - 100, y_position))
    screen.blit(font.render("[", True, BLACK), (current_x, y_position))
    current_x += font.size("[")[0]


    for i, num in enumerate(array):
        color = (255, 0, 0) if num in highlighted_numbers else BLACK
        num_text = font.render(str(num), True, color)
        screen.blit(num_text, (current_x, y_position))
        current_x += num_text.get_width()

        if i < len(array) - 1:
            comma_text = font.render(",", True, BLACK)
            screen.blit(comma_text, (current_x, y_position))
            current_x += comma_text.get_width()

    screen.blit(font.render("]", True, BLACK), (current_x, y_position))


    if visited_nodes:
        y_position += 50
        current_x = (SCREEN_WIDTH // 2) - (font.size("[" + ",".join(str(num) for num in visited_nodes) + "]")[0] // 2)
        array_text = font.render(algoritam + " List:", True, BLACK)
        screen.blit(array_text, (current_x - 120, y_position))
        screen.blit(font.render("[", True, BLACK), (current_x, y_position))
        current_x += font.size("[")[0]


        for i, num in enumerate(visited_nodes):
            num_text = font.render(str(num), True, BLACK)
            screen.blit(num_text, (current_x, y_position))
            current_x += num_text.get_width()

            if i < len(visited_nodes) - 1:
                comma_text = font.render(",", True, BLACK)
                screen.blit(comma_text, (current_x, y_position))
                current_x += comma_text.get_width()

        screen.blit(font.render("]", True, BLACK), (current_x, y_position))




def AVL_Tree():
    Tk().wm_withdraw()
    messagebox.showinfo("Tutorial\n",
                        "Up Button : add Number to AVL Tree\nDown Button : remove Number from AVL Tree\n\n\n"
                        "after you finish build the Tree:\n\nLeft Button: press few times to see the order of BFS\n"
                        "Right Button: press few times to see the order of DFS\n\n\nAfter press Left OR Right Button you can press Space to clear")
    avl_tree = AVLTree()
    input_number = ""
    TreeNumbers = []
    BFS_order = []
    Highest = 0
    DFS_order = []
    stack = []
    highlighted_numbers = []
    targets = []
    visited_nodes = []
    BFS_activate = False
    DFS_activate = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP :
                    if BFS_activate != False or DFS_activate != False:
                        Tk().wm_withdraw()
                        messagebox.showinfo("Error\n", "you cant add when you start DFS OR BFS!")
                        input_number = ""
                        break
                    try:
                        num = int(input_number)
                        if not num in TreeNumbers:
                            avl_tree.insert(num)
                            TreeNumbers.append(num)
                            avl_tree.update_array(avl_tree.root, TreeNumbers)
                        else:
                            Tk().wm_withdraw()
                            messagebox.showinfo("Error\n","This Number already exists!")
                    except ValueError:
                        pass
                    input_number = ""
                elif event.key == pygame.K_DOWN :
                    if BFS_activate != False or DFS_activate != False:
                        Tk().wm_withdraw()
                        messagebox.showinfo("Error\n", "you cant delete when you start DFS OR BFS!")
                        input_number = ""
                        break
                    try:
                        num = int(input_number)
                        if num in TreeNumbers:
                            TreeNumbers.remove(num)
                            avl_tree.delete(num)
                            avl_tree.update_array(avl_tree.root, TreeNumbers)
                        else:
                            Tk().wm_withdraw()
                            messagebox.showinfo("Error\n","This Number not exists!")
                    except ValueError:
                        pass
                    input_number = ""
                elif event.key == pygame.K_LEFT and DFS_activate == False:
                    Highest, BFS_order, targets = avl_tree.BFS(Highest, BFS_order)
                    for target in targets:
                        if target.key not in visited_nodes:
                            visited_nodes.append(target.key)
                        if target.key not in highlighted_numbers:
                            highlighted_numbers.append(target.key)
                    BFS_activate = True

                elif event.key == pygame.K_RIGHT and BFS_activate == False:
                    stack, DFS_order, target = avl_tree.DFS(stack, DFS_order)
                    if target is not None and target not in visited_nodes:
                        visited_nodes.append(target)
                    if target is not None and target not in highlighted_numbers:
                        highlighted_numbers.append(target)
                    DFS_activate = True

                elif event.key == pygame.K_SPACE:
                    avl_tree.visited = set()
                    DFS_order = []
                    stack = []
                    BFS_order = []
                    Highest = 0
                    targets = []
                    BFS_activate = False
                    DFS_activate = False
                    highlighted_numbers = []
                    visited_nodes = []

                elif event.key == pygame.K_BACKSPACE:
                    input_number = input_number[:-1]
                else:
                    input_number += event.unicode

        pygame.display.update()



        screen.fill(WHITE)
        if avl_tree.root:
            avl_tree.draw(SCREEN_WIDTH // 2, 50, avl_tree.root, 0)
            avl_tree.update_array(avl_tree.root,TreeNumbers)
            TreeNumbers = [x for x in TreeNumbers if x is not None]

        font = pygame.font.Font(None, 36)
        input_text = font.render("Enter a number: " + input_number, True, BLACK)
        input_rect = input_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        screen.blit(input_text, input_rect)

        if DFS_activate:
            draw_array(screen, TreeNumbers, highlighted_numbers, targets, visited_nodes,"DFS")
        elif BFS_activate:
            draw_array(screen, TreeNumbers, highlighted_numbers, targets, visited_nodes, "BFS")
        else:
            draw_array(screen, TreeNumbers, [], targets, [],"")

        pygame.display.flip()

    pygame.quit()
    sys.exit()
