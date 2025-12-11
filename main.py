from task_manager import TaskManager

# Créer le gestionnaire
manager = TaskManager()

# Ajouter des tâches
manager.add_task("Apprendre Git", 
                 "Suivre le cours")
manager.add_task("Faire l'exercice")
manager.add_task("Réviser pour l'exam")

# Compléter une tâche
manager.complete_task(0)

# Afficher
print("=== Mes tâches ===")
manager.display_all()