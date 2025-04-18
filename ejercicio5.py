class VentanaDeslizanteMaxima:
    
    def __init__(self, nums, k):
        if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
            raise TypeError("La lista debe contener solo enteros.")
        if not isinstance(k, int) or k <= 0:
            raise ValueError("El tamaño de la ventana debe ser un entero positivo.")
        if k > len(nums):
            raise ValueError("El tamaño de la ventana no puede ser mayor que la longitud de la lista.")
        self.nums = nums
        self.k = k

    def resolver(self):
        resultado = []
        ventana = []

        for i in range(len(self.nums)):
            while ventana and ventana[0] <= i - self.k:
                ventana.pop(0)
            while ventana and self.nums[ventana[-1]] < self.nums[i]:
                ventana.pop()
            ventana.append(i)
            if i >= self.k - 1:
                resultado.append(self.nums[ventana[0]])

        return resultado

#PRUEBAAAAA
def pruebas():
    assert VentanaDeslizanteMaxima([1,3,-1,-3,5,3,6,7], 3).resolver() == [3,3,5,5,6,7]
    assert VentanaDeslizanteMaxima([9, 11], 2).resolver() == [11]
    assert VentanaDeslizanteMaxima([4, 2, 12, 3, 8, 7], 1).resolver() == [4, 2, 12, 3, 8, 7]
    assert VentanaDeslizanteMaxima([1, 3, 1, 2, 0, 5], 3).resolver() == [3, 3, 2, 5]

    try:
        VentanaDeslizanteMaxima([], 3).resolver()
    except ValueError as e:
        print(f"Error esperado: {e}")

    try:
        VentanaDeslizanteMaxima([1, 2, 3], 0).resolver()
    except ValueError as e:
        print(f"Error esperado: {e}")

    try:
        VentanaDeslizanteMaxima([1, 2, 3], "dos").resolver()
    except ValueError as e:
        print(f"Error esperado: {e}")

    print("Todas las pruebas pasaron.")
pruebas()