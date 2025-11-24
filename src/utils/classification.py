# src/utils/classification.py

import re
from src.utils.rules import RULES, EXACT

def clasificar_producto(nombre):                                                        
    texto = nombre.lower()

    # 1) Coincidencia exacta
    if texto in EXACT:
        return EXACT[texto]

    # 2) Coincidencia por regex
    # Recorrer categorías y keywords
    for categoria, patrones in RULES.items():
        for patron in patrones:
            if re.search(patron, texto):
                return categoria

    # Fallback final
    return "Alimentos secos"
                                                                                                                                  