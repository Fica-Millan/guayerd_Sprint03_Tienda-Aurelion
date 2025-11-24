# src/utils/validation.py

from src.utils.rules import RULES

def verificar_fallbacks(df):
    """
    Devuelve productos que quedaron en 'Alimentos secos' pero no
    coinciden con ninguna keyword real de esta categoría.
    """

    alimentos_keywords = RULES["Alimentos secos"]

    alimentos_reales = df[df["categoria_corregida"] == "Alimentos secos"]

    fallas = alimentos_reales[
        ~alimentos_reales["nombre_producto"]
        .str.lower()
        .apply(lambda x: any(kw in x for kw in alimentos_keywords))
    ]

    return alimentos_reales, fallas
