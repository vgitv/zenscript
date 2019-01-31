# .opt/bin

Ce dossier contient les exécutables. Ajouter dans le `.bashrc` :

```bash
export PATH=$HOME/.opt/bin:$PATH
```

Dans le cas où les sources ne tiennent pas sur un seul fichier, les mettre dans le dossier `.opt/src/nom_programme/` puis créer un script bash du même nom dans le `bin` qui appelle le programme. On évite ainsi les liens symboliques. Par exemple, si le programme 'truc' comporte plusieurs fichier sources, on organise l'arborescence ainsi :

```
.opt/
|   bin/
|   |   truc # script bash comportant la ligne "~/.opt/src/truc/main.py"
|   src/
|   |   truc/
|   |   |   main.py
|   |   |   module1.py
|   |   |   module2.py
```
