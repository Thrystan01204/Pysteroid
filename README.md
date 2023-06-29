# Pysteroid

3 modules :

- client
- server
- game

## Gameplay :

Doit ressembler à [ce jeu](https://store.steampowered.com/app/1700890/Asteroids_Recharged/?l=french)

Gameplay en 2d, le joueur peut se déplacer vers le haut, la gauche, le bas et la droite.
Les diagonales doivent être aussi disponibles.

Contrôle :

- Z : devant
- Q : gauche
- S : bas
- D : droite
- espace : piou piou

Bonus :

- Avec temps :

  - tir rapide (10 s)
  - rayon plein (2 s)
  - clones (5 s)
  - grosse explosion à l'impact (10 s)
  - trou noir (au niveau de la récup du buff, 5 s)

- Permanent :
  - triple tir
  - tourelle automatique
  - invulnérabilité temporaire (2 s toutes les 10 s)

## Style

Style originale, écran noir avec des étoiles, astéroïdes en blanc, les joueurs ont des couleurs.

## Modules python à installer :

```shell
pip install pyglet pymunk
```
