import math

def alpha_beta_search(depth, node_index, is_max, scores, alpha, beta, height, visited):
    if depth == height:
        visited.append(scores[node_index])
        return scores[node_index]

    if is_max:
        best_val = -math.inf
        for i in range(2):
            val = alpha_beta_search(depth + 1, node_index * 2 + i, False, scores, alpha, beta, height, visited)
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break # Beta cutoff
        return best_val
    else:
        best_val = math.inf
        for i in range(2):
            val = alpha_beta_search(depth + 1, node_index * 2 + i, True, scores, alpha, beta, height, visited)
            best_val = min(best_val, val)
            beta = min(beta, best_val)
            if beta <= alpha:
                break # Alpha cutoff
        return best_val

leaf_scores = [3, 5, 6, 9, 1, 2, 0, -1]
tree_height = int(math.log2(len(leaf_scores)))
evaluated_nodes = []

print("Alpha-Beta Pruning Algorithm for Gaming:\n")
print(f"Leaf Utility Scores: {leaf_scores}")
print(f"Tree Height: {tree_height}")

optimal_val = alpha_beta_search(depth=0, node_index=0, is_max=True, scores=leaf_scores, alpha=-math.inf, beta=math.inf, height=tree_height, visited=evaluated_nodes)

print(f"\nEvaluated Leaf Nodes: {evaluated_nodes}")
print(f"Pruned Leaves Count: {len(leaf_scores) - len(evaluated_nodes)}")
print(f"Optimal Value with Alpha-Beta Pruning: {optimal_val}")