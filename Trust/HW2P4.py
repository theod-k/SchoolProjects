import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Parameters
alpha = 10.5
beta_param = 7.5

# X values from 0 to 1
x = np.linspace(0, 1, 100)

# Beta distribution PDF
pdf = beta.pdf(x, alpha, beta_param)

# Plotting
plt.figure(figsize=(8, 4))
plt.plot(x, pdf, label=f'Beta({alpha}, {beta_param})')
plt.title('Beta Distribution PDF')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid()
plt.show()
