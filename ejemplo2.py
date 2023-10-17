import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Generamos algunos datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creamos un gráfico
plt.plot(x, y)

# Mostramos el gráfico en la aplicación web
st.pyplot(plt)
