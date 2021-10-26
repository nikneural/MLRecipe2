from sklearn.datasets import make_regression
from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Сгенерировать матрицу признаков, вектор целей и истинные коэффициенты
features, target, coefficients = make_regression(n_samples=100,
                                                 n_features=3,
                                                 n_informative=3,
                                                 n_targets=1,
                                                 noise=0.0,
                                                 coef=True,
                                                 random_state=1)

print("Матрица признаков:\n {}".format(features[:3]))
print("Вектор целей:\n {}".format(target[:3]))

# для классификации
features, target = make_classification(n_samples=100,
                                       n_features=3,
                                       n_informative=3,
                                       n_redundant=0,
                                       n_classes=2,
                                       weights=[.25, .75],
                                       random_state = 1)

print("Матрица признаков:\n {}".format(features[:3]))
print("Вектор целей:\n {}".format(target[:3]))

# для кластеризации

features, target, make_blobs(n_samples=100,
                             n_features=2,
                             centers=3,
                             cluster_std=0.5,
                             shuffle=True,
                             random_state=1)

print("Матрица признаков:\n {}".format(features[:3]))
print("Вектор целей:\n {}".format(target[:3]))

plt.scatter(features[:, 0], features[:, 1], c=target)
plt.show()