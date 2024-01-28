from typing import List


class Tree:
    def __init__(self, id: int, children: List['Tree']):
        self.id = id
        self.children = children

# Вывести все ID элементов дерева


# Depth-first search
def recursive_dfs(tree: Tree):
    result = [tree.id]
    # не выполнится, если children пустой
    for x in tree.children:
        result += recursive_dfs(x)
    return result


def dfs(tree: Tree):
    result = []
    stack = [tree]

    # [12, 2] -> True
    # [] -> False

    while stack:
        current = stack.pop()
        result.append(current.id)
        for child in current.children:
            stack.append(child)

    return result


tree = Tree(
    1,
    [
        Tree(2, []),
        Tree(3, [
            Tree(4, []),
            Tree(5, [])
        ])
    ]
)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(' '.join([str(x) for x in recursive_dfs(tree)]))

