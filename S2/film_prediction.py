import numpy as np

# Données d'exemple
ratings = np.array([[5, 3, 0, 1],
                    [4, 0, 0, 1],
                    [1, 1, 0, 5],
                    [1, 0, 0, 4],
                    [0, 1, 5, 4]])

# Décomposition SVD
U, s, V = np.linalg.svd(ratings)

# Nombre de dimensions à utiliser
k = 2

# Reconstruction de la matrice originale avec les k premières dimensions
reconstructed_ratings = np.dot(U[:, :k], np.dot(np.diag(s[:k]), V[:k, :]))

# Prédiction de l'évaluation pour l'utilisateur 0 et le film 2 (indices 0-based)
user_id = 0
movie_id = 2
predicted_rating = reconstructed_ratings[user_id, movie_id]

print("Matrice de notation originale :\n", ratings)
print("\nMatrice reconstruite :\n", reconstructed_ratings)
print("\nPrédiction de l'évaluation pour l'utilisateur", user_id, "et le film", movie_id, ":", predicted_rating)

import numpy as np

# Define a full matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Use a lambda function to create a binary matrix based on a condition
binary_matrix = np.array(list(map(lambda x: [1 if val > 5 else 0 for val in x], matrix)))

print("Original Matrix:")
print(matrix)
print("\nBinary Matrix (based on values > 5):")
print(binary_matrix)
