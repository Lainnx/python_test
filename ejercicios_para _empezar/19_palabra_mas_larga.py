
texto = input("Introduce una texto: ").strip().split(" ")

palabra_ml = ""

for palabra in texto:
    if len(palabra) > len(palabra_ml):
        palabra_ml = palabra
print(f"La palabra más larga del texto es: {palabra_ml}")