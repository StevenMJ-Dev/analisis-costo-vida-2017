import pandas as pd
import matplotlib.pyplot as plt


# ============================================
# EJERCICIO: EXAMEN FINAL
# Análisis del costo de vida mundial 2017
# ============================================


# ============================================
# 1. REVISIÓN INICIAL DEL DATASET
# ============================================

# Importar dataset CSV
datos = pd.read_csv("living.csv")


# --------------------------------------------
# Nro. de Filas y Nro. de Columnas
# --------------------------------------------

print("Número de filas:", datos.shape[0])
print("Número de columnas:", datos.shape[1])


# --------------------------------------------
# Costo de vida promedio
# --------------------------------------------

promedio = datos["Cost of living, 2017"].mean()

print("Costo de vida promedio:", round(promedio, 2))


# --------------------------------------------
# País con costo de vida más alto
# --------------------------------------------

mayor = datos.loc[datos["Cost of living, 2017"].idxmax()]

print("País con costo de vida más alto:", mayor["Countries"])
print("Costo de vida:", mayor["Cost of living, 2017"])



# --------------------------------------------
# País con costo de vida más bajo
# --------------------------------------------

menor = datos.loc[datos["Cost of living, 2017"].idxmin()]

print("País con costo de vida más bajo:", menor["Countries"])
print("Costo de vida:", menor["Cost of living, 2017"])



# --------------------------------------------
# Costo de Vida en Perú
# --------------------------------------------

peru = datos[datos["Countries"] == "Peru"]

print("Costo de vida en Perú:",
      peru["Cost of living, 2017"].values[0])



# --------------------------------------------
# Ranking de Perú
# --------------------------------------------

print("Ranking de Perú:",
      peru["Global rank"].values[0])




# ============================================
# 2. VISUALIZACIONES
# ============================================


# --------------------------------------------
# Los 10 países con el costo de vida más alto
# --------------------------------------------

top10 = datos.nlargest(10, "Cost of living, 2017")


plt.figure(figsize=(10,5))

plt.bar(
    top10["Countries"],
    top10["Cost of living, 2017"]
)

plt.title("Top 10 países con mayor costo de vida")
plt.xlabel("Países")
plt.ylabel("Costo de vida")

plt.xticks(rotation=45)

plt.show()



# --------------------------------------------
# Los 10 países con el costo de vida más bajo
# --------------------------------------------

bottom10 = datos.nsmallest(10, "Cost of living, 2017")


plt.figure(figsize=(10,5))

plt.bar(
    bottom10["Countries"],
    bottom10["Cost of living, 2017"]
)

plt.title("Top 10 países con menor costo de vida")
plt.xlabel("Países")
plt.ylabel("Costo de vida")

plt.xticks(rotation=45)

plt.show()



# --------------------------------------------
# Costo de vida de los países de América
# --------------------------------------------

america = datos[datos["Continent"] == "America"]


plt.figure(figsize=(12,6))

plt.bar(
    america["Countries"],
    america["Cost of living, 2017"]
)


plt.title("Costo de vida de los países de América")
plt.xlabel("Países")
plt.ylabel("Costo de vida")

plt.xticks(rotation=90)

plt.show()