import re

def validar_contraseña(contraseña):
    criterios = {
        "longitud": len(contraseña) >= 8,
        "mayúscula": re.search(r"[A-Z]", contraseña) is not None,
        "minúscula": re.search(r"[a-z]", contraseña) is not None,
        "número": re.search(r"[0-9]", contraseña) is not None,
        "símbolo": re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña) is not None,
    }

    print("\nResultado de validación:")
    for criterio, cumplido in criterios.items():
        print(f"✔ {criterio.capitalize()}: {'Sí' if cumplido else 'No'}")

    if all(criterios.values()):
        print("\n✅ Contraseña segura.")
    else:
        print("\n❌ Contraseña insegura. Revisa los criterios anteriores.")

# Uso
if __name__ == "__main__":
    contraseña = input("Ingresa tu contraseña para validar: ")
    validar_contraseña(contraseña)
