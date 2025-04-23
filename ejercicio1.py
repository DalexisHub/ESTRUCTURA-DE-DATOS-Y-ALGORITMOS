from collections import deque

def sliding_window_maximum(nums, k):
    if not nums or k == 0:
        return []

    dq = deque()
    result = []

    for i in range(len(nums)):
        # Eliminar índices que están fuera del rango de la ventana
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Eliminar elementos menores al actual desde el final de la cola
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Agregar el máximo a la lista de resultados
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
# Output: [3, 3, 5, 5, 6, 7]

print(sliding_window_maximum([1, 3, 1, 2, 0, 5], 3))  # [3, 3, 2, 5]
print(sliding_window_maximum([9, 8, 7, 6, 5], 2))     # [9, 8, 7, 6]
print(sliding_window_maximum([1, 1, 1, 1, 1], 3))     # [1, 1, 1]

