+# Code pour gestion des différences
+
+from typing import List
+import os
+
+class DiffEngine:
+    @staticmethod
+    def calculate_diff( fichier Original, fichier Nouveau ) : 
+        # fonction d'implémentation pour la génération de diff
+        diff = os.popen('diff -q ' + original  + '	' + nouveau).read().strip()
+        return diff)
+
fichier = os.path.abspath( Original fichier )
m nouveau = os.path. abolte( Nouveau fichier)
+nous devrions implémenter une fonction pour la gestion de la modification des fichiers
+
+def main() :
+    print("Bienvenue dans le différencier!