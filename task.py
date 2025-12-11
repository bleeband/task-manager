from datetime import datetime

class Task:
    """Représente une tâche individuelle."""
    
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
    
    def complete(self):
        """Marque la tâche comme complétée."""
        self.completed = True
    
    def __str__(self):
        status = "✅" if self.completed else "⏳"
        return f"{status} {self.title}"