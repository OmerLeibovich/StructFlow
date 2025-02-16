def BFS_Search(self, highest, BFS_order):
    targets = []
    if self.root is None:
        return highest, BFS_order, targets

    if not BFS_order:
        BFS_order.append(self.root)
        self.visited.add(self.root.key)
        targets.append(self.root)
        return highest, BFS_order, targets

    for node in BFS_order[highest:]:
        if node.left:
            BFS_order.append(node.left)
            self.visited.add(node.left.key)
            targets.append(node.left)
        if node.right:
            BFS_order.append(node.right)
            self.visited.add(node.right.key)
            targets.append(node.right)
        highest += 1

    return highest, BFS_order, targets