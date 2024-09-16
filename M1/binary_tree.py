def in_order(tree):

    if tree is None:

        return

    yield from in_order(tree.left)

    yield tree.value

    yield from in_order(tree.right)

    