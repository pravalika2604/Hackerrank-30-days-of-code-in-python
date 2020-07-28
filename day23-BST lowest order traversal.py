

    def levelOrder(self,root):
        queue = [root]
        for node in filter(None, queue):
            print(node.data, end=' ')
            queue += [node.left, node.right]
