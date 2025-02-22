from tkinter import ttk

def apply_styles(root):
    """Aplica estilos personalizados a la interfaz gráfica."""
    style = ttk.Style(root)
    style.theme_use("clam")
    
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12), padding=5)
    style.configure("TEntry", font=("Arial", 12), padding=5)
    style.configure("Treeview", font=("Arial", 11), rowheight=25)