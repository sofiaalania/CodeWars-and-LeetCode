# Pre-order traversal
def pre_order_generator(node):
    if node is None:
        return

    yield node.data
    for c in [node.left, node.right]:
        yield from pre_order_generator(c)
def pre_order(node):
    return list(pre_order_generator(node))
# In-order traversal
def in_order_gen(node):
    if node is None:
        return

    for c in [node.left]:
        yield from in_order_gen(c)
    yield node.data
    for c in [node.right]:
        yield from in_order_gen(c)
    
def in_order(node):
    return list(in_order_gen(node))

# Post-order traversal
def post_order_gen(node):
    if node is None:
        return

    for c in [node.left, node.right]:
        yield from post_order_gen(c)
    yield node.data

def post_order(node):
    return list(post_order_gen(node))
