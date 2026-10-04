# KM CEO · Equipación

Presentación web de la propuesta de equipación del club KM CEO (km-ceo.com): mockups de producto e imágenes inspiracionales de tritrajes, tirantes de running, camiseta de algodón y calcetines, fabricados por GSport Custom.

**Ver la presentación:** https://ricardovilardi.github.io/kmceo-equipacion/

## Navegación

| Acción | Teclado | Ratón / táctil |
|---|---|---|
| Siguiente / anterior | `→` `←`, `Espacio`, `RePág` `AvPág` | Botones de la barra, clic en la mitad derecha/izquierda, deslizar |
| Primera / última | `Inicio` `Fin` | — |
| Miniaturas | `G` | Botón de cuadrícula |
| Saltar a una sección | — | Botón «Secciones» |
| Pantalla completa | `F` | Botón de pantalla completa |
| Enlace a una diapositiva | — | `…/#12` abre la diapositiva 12 |

## Estructura

- `index.html`: la presentación generada (no editar a mano).
- `slides-src/`: una diapositiva por archivo (1920×1080, estilos inline), `deck.json` con orden y secciones, y `blobmap.json` con el mapeo de imágenes.
- `template.html`: navegación y estilos de la web.
- `assets/img/`: mockups e imágenes (JPG, 2000 px).

Para regenerar tras editar una diapositiva o la plantilla:

```bash
python3 build.py
```

Los mockups son imágenes generadas con IA a partir del logo oficial y de las fotos de producto de GSport. Son orientativos: el fabricante debe entregar su diseño técnico para aprobar antes de producir.
