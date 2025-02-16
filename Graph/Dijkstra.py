import sys
from tkinter import messagebox,Tk


import pygame
import random

from Graph.UnionFind import UnionFind
from Screen import *

Title = initialize_screen("The Shortest Path")

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connections = []

def find_nearest_node(pos, nodes, threshold=20):
    for node in nodes:
        distance = ((node.x - pos[0]) ** 2 + (node.y - pos[1]) ** 2) ** 0.5
        if distance <= threshold:
            return node
    return None

def connect_nodes(node1, node2, edges):
    if node2 not in node1.connections:
        node1.connections.append(node2)
        node2.connections.append(node1)
        random_number = random.randint(1, 100)
        edges.append((node1, node2, random_number))


def find_mst_progressive(nodes, edges, mst_edges, union_find):
    edges = sorted(edges, key=lambda edge: edge[2])
    for edge in edges:
        node1, node2, weight = edge
        if union_find.union(node1, node2):
            mst_edges.append(edge)
            return edge
    return None


def Graph():
    Tk().wm_withdraw()
    messagebox.showinfo("Tutorial\n",
                        "Left Clicker : Choose where you want to put the graph points\nRight Clicker : press and Drag to connect between graph points\n\n\n"
                        "After you finish building the Graph:\n\nDown Button: Press to give random numbers to the arcs \n"
                        "Up Button: Press a few times to see how to find the shortest path\n\n\nCan press Space to clear")
    nodes = []
    edges = []

    connecting_nodes = False
    lines = False
    shortest_path_edges = set()
    shortest_path_progress = []
    show_numbers = False
    distances_array = []

    right_click_held = False
    start_node = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not lines:
                    x, y = pygame.mouse.get_pos()
                    if y < 650:
                        node = Node(x, y)
                        nodes.append(node)
                elif event.button == 3:
                    right_click_held = True
                    pos = pygame.mouse.get_pos()
                    start_node = find_nearest_node(pos, nodes)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    right_click_held = False
                    start_node = None

            elif event.type == pygame.MOUSEMOTION and right_click_held:
                if start_node:
                    pos = pygame.mouse.get_pos()
                    end_node = find_nearest_node(pos, nodes)
                    if end_node and end_node != start_node:
                        connect_nodes(start_node, end_node, edges)
                        start_node = end_node

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and show_numbers:
                    if not shortest_path_edges:
                        union_find = UnionFind(nodes)
                        shortest_path_edges = []
                        mst_edges = []


                    next_edge = find_mst_progressive(nodes, edges, shortest_path_edges, union_find)
                    if next_edge:
                        shortest_path_progress.append(next_edge)

                elif event.key == pygame.K_DOWN:
                    for i in range(len(edges)):
                        edges[i] = (edges[i][0], edges[i][1], random.randint(1, 100))
                    show_numbers = True
                    shortest_path_edges = set()
                    shortest_path_progress = []
                    distances_array = [edge[2] for edge in edges]

                elif event.key == pygame.K_SPACE:
                    nodes.clear()
                    edges.clear()
                    shortest_path_edges.clear()
                    shortest_path_progress.clear()
                    show_numbers = False
                    connecting_nodes = False
                    lines = False
                    distances_array = []

        screen.fill((255, 255, 255))

        pygame.draw.line(screen, (0, 0, 0), (0, 650), (SCREEN_WIDTH, 650), 3)


        for node in nodes:
            pygame.draw.circle(screen, (0, 0, 255), (node.x, node.y), 22)


        for edge in edges:
            x1, y1, x2, y2, random_number = edge[0].x, edge[0].y, edge[1].x, edge[1].y, edge[2]
            if edge in shortest_path_progress or (edge[1], edge[0], edge[2]) in shortest_path_progress:
                edge_color = (255, 0, 0)
            else:
                edge_color = (0, 0, 0)

            pygame.draw.line(screen, edge_color, (x1, y1), (x2, y2), 6)

            if show_numbers:
                font = pygame.font.Font(None, 36)
                text_x, text_y = (x1 + x2) / 1.98, (y1 + y2) / 1.98
                text = font.render(str(random_number), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (text_x, text_y)
                pygame.draw.rect(screen, (255, 255, 0), text_rect.inflate(10, 10))
                screen.blit(text, text_rect)

        if distances_array:
            font = pygame.font.Font(None, 36)
            distances_text = "distances: " + " " * 3 + str(distances_array)
            distances_surface = font.render(distances_text, True, (0, 0, 0))
            screen.blit(distances_surface, (10, 670))

        if shortest_path_progress:
            shortest_distances = [edge[2] for edge in shortest_path_progress]
            font = pygame.font.Font(None, 36)
            shortest_distances_text = "Shortest Path: " + " " * 3 + str(shortest_distances)
            shortest_distances_surface = font.render(shortest_distances_text, True, (0, 0, 0))
            screen.blit(shortest_distances_surface, (10, 730))

        pygame.display.update()

if __name__ == '__main__':
    Graph()
