from tkinter import ttk

class CustomProgressBar(ttk.Progressbar):
    """Barra de progreso personalizada con funcionalidades adicionales."""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(mode='determinate')
    
    def update_progress(self, value):
        """Actualiza el valor de la barra de progreso."""
        self['value'] = value
        self.update_idletasks()