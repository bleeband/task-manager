from task import Task

class TaskManager:
    """Gestionnaire de tâches."""
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, description=""):
        """Ajoute une nouvelle tâche."""
        task = Task(title, description)
        self.tasks.append(task)
        return task
    
    def get_pending_tasks(self):
        """Retourne les tâches non complétées."""
        return [t for t in self.tasks 
                if not t.completed]
    
    def get_completed_tasks(self):
        """Retourne les tâches complétées."""
        return [t for t in self.tasks 
                if t.completed]
    
    def complete_task(self, index):
        """Marque une tâche comme complétée."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
            return True
        return False
    
    def display_all(self):
        """Affiche toutes les tâches."""
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")