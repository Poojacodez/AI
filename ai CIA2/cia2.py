def minimax(depth, index, isMax, values, alpha, beta):
    if depth == 3:  
        return values[index]  
    
    if isMax:
        best = -float('inf')
        for i in range(2):  
            best = max(best, minimax(depth + 1, index * 2 + i, False, values, alpha, beta))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):  
            best = min(best, minimax(depth + 1, index * 2 + i, True, values, alpha, beta))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Driver code
if __name__ == "__main__":
    values = [1, 4, 7, 2, 3, 0, 6, 5]  
    print("Optimal value:", minimax(0, 0, True, values, -float('inf'), float('inf')))
