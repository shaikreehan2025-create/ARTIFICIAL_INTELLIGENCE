import math

def minimax(depth, node_index, is_max, scores, height):
    # Base condition: leaf node reached
    if depth == height:
        return scores[node_index]

    if is_max:
        val1 = minimax(depth + 1, node_index * 2, False, scores, height)
        val2 = minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        return max(val1, val2)
    else:
        val1 = minimax(depth + 1, node_index * 2, True, scores, height)
        val2 = minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        return min(val1, val2)

# Terminal game utility leaf scores
leaf_scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_height = int(math.log2(len(leaf_scores)))

print("Minimax Algorithm for Adversarial Game Tree:\n")
print(f"Terminal Leaf Node Scores: {leaf_scores}")
print(f"Game Tree Depth: {tree_height}")

optimal_value = minimax(depth=0, node_index=0, is_max=True, scores=leaf_scores, height=tree_height)
print(f"\nOptimal Utility Value for Maximizing Player: {optimal_value}")