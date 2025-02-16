from tkinter import *
from PIL import ImageTk, Image

from Structures.Doubly_LinkedList import Run_DoublyLinkedList
from Structures.LinkedList import Run_LinkedList
from Graph.path_finder import path_finder
from Tree.AVL_Tree import AVL_Tree
from Graph.Dijkstra import Graph



active_path_finder = False
active_AVL_TREE = False
active_Graph = False
active_LinkedList = False
active_DoublyLinkedList = False

def activate_path_finder():
    global active_path_finder
    active_path_finder = True
    root.destroy()

def activate_AVL_tree():
    global active_AVL_TREE
    active_AVL_TREE = True
    root.destroy()

def activate_graph():
    global active_Graph
    active_Graph = True
    root.destroy()

def activate_linked_list():
    global active_LinkedList
    active_LinkedList = True
    root.destroy()

def activate_doubly_linked_list():
    global active_DoublyLinkedList
    active_DoublyLinkedList = True
    root.destroy()

root = Tk()
myimg = ImageTk.PhotoImage(Image.open("algorithm-formulation.jpg"))
my_imageLabel = Label(image=myimg)
my_imageLabel.pack()
root.attributes('-fullscreen', True)
PathFinderButton = Button(root, text="path_finder", padx=30, pady=30, fg="green", command=activate_path_finder, font=('Bold', '20'))
AVL_TreeButton = Button(root, text="AVL_Tree", padx=30, pady=30, fg="Black", command=activate_AVL_tree, font=('Bold', '20'))
GraphButton = Button(root, text="Graph", padx=30, pady=30, fg="Black", command=activate_graph, font=('Bold', '20'))
LinkedListButton = Button(root, text="LinkedList", padx=30, pady=30, fg="Black", command=activate_linked_list, font=('Bold', '20'))
DoublyLinkedListButton = Button(root, text="DoublyLinkedList", padx=30, pady=30, fg="Black", command=activate_doubly_linked_list, font=('Bold', '20'))
exitButton = Button(root, text="Exit", padx=50, pady=30, fg="red",command = root.destroy,font=('Bold', '20'))
PathFinderButton.pack()
PathFinderButton.place(x=1080, y=100)
AVL_TreeButton.pack()
AVL_TreeButton.place(x=1080,y=250)
GraphButton.pack()
GraphButton.place(x=1080,y=400)
LinkedListButton.pack()
LinkedListButton.place(x=1080,y=550)
DoublyLinkedListButton.pack()
DoublyLinkedListButton.place(x=600,y=100)
exitButton.pack()
exitButton.place(x=680, y=700)
root.mainloop()


if active_path_finder:
    path_finder()
elif active_AVL_TREE:
    AVL_Tree()
elif active_Graph:
    Graph()
elif active_LinkedList:
    Run_LinkedList()
elif active_DoublyLinkedList:
    Run_DoublyLinkedList()
