import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
from controllers.novel_controller import NovelController
from controllers.chapter_controller import ChapterController

class MainWindow:
    """Ventana principal de la aplicación Novel Downloader."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Novel Downloader")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")

        # Configurar el tema moderno
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Lista de URLs base disponibles
        self.urls_base_list = [
            "https://www.novelhall.com",
            "https://www.webnovel.com",
            "https://www.skynovels.net",
            "https://panchotranslations.com",
            "https://wuxiaworld.site",
            "https://www.wuxiaworld.com",
            "https://novelasligeras.net"
        ]

        # Variables de control
        self.url_novela = tk.StringVar()
        self.url_base = tk.StringVar(value=self.urls_base_list[0])  # Establecer valor predeterminado
        self.idioma_destino = tk.StringVar(value="es")
        self.modo_descarga = tk.StringVar(value="todos")
        self.capitulo_inicio = tk.StringVar(value="1")
        self.capitulo_fin = tk.StringVar(value="200")
        self.capitulo_especifico = tk.StringVar(value="1")

        # Inicializar controladores
        self.novel_controller = NovelController(self.url_base.get())
        self.chapter_controller = ChapterController(self.url_base.get())

        # Crear la interfaz gráfica
        self.create_widgets()
        self.modo_descarga.trace_add("write", self.actualizar_interfaz)
    
    def create_widgets(self):
        """Crea los widgets de la interfaz gráfica."""
        # Agregar una barra de progreso
        self.progress = ttk.Progressbar(self.root, mode='determinate')
        self.progress.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        
        # Agregar un label para mostrar el estado
        self.status_label = ttk.Label(self.root, text="")
        self.status_label.grid(row=3, column=0, padx=10, pady=5)

        # Frame para la búsqueda de novelas
        frame_busqueda = ttk.LabelFrame(self.root, text="Buscar Novela", padding=10)
        frame_busqueda.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(frame_busqueda, text="Término de Búsqueda:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_busqueda = ttk.Entry(frame_busqueda, width=50)
        self.entry_busqueda.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(frame_busqueda, text="Buscar", command=self.buscar_novela_interfaz).grid(row=0, column=2, padx=5, pady=5)

        # Área de texto para mostrar resultados con un Treeview
        columns = ("nombre", "ultimo_capitulo")
        self.tree = ttk.Treeview(frame_busqueda, columns=columns, show='headings', height=10)
        
        # Configurar las columnas
        self.tree.heading('nombre', text='Nombre de la Novela')
        self.tree.heading('ultimo_capitulo', text='Último Capítulo')
        
        # Configurar el ancho de las columnas
        self.tree.column('nombre', width=400)
        self.tree.column('ultimo_capitulo', width=200)
        
        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(frame_busqueda, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Posicionar el Treeview y el scrollbar
        self.tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        scrollbar.grid(row=1, column=2, pady=5, sticky="ns")
        
        # Vincular el evento de selección
        self.tree.bind('<<TreeviewSelect>>', self.on_select_novela)

        # Frame para la descarga de capítulos
        frame_descarga = ttk.LabelFrame(self.root, text="Descargar Capítulos", padding=10)
        frame_descarga.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(frame_descarga, text="URL de la Novela:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_url_novela = ttk.Entry(frame_descarga, textvariable=self.url_novela, width=50)
        self.entry_url_novela.grid(row=0, column=1, padx=10, pady=10)

        # Tooltip para la URL de la novela
        self.tooltip_url_novela = ttk.Label(frame_descarga, text="Pega aquí la URL de la novela", foreground="gray")
        self.tooltip_url_novela.grid(row=0, column=2, padx=5, pady=10, sticky="w")
        self.entry_url_novela.bind("<FocusIn>", lambda e: self.tooltip_url_novela.config(text=""))
        self.entry_url_novela.bind("<FocusOut>", lambda e: self.tooltip_url_novela.config(text="Pega aquí la URL de la novela"))

        ttk.Label(frame_descarga, text="URL Base:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.combo_url_base = ttk.Combobox(
            frame_descarga,
            textvariable=self.url_base,
            values=self.urls_base_list,  # Usar la lista de URLs
            width=47,
            state="readonly"
        )
        self.combo_url_base.grid(row=1, column=1, padx=10, pady=10)
        # Opcional: Agregar un evento cuando se cambia la selección
        self.combo_url_base.bind('<<ComboboxSelected>>', self.on_url_base_change)
        
        ttk.Label(frame_descarga, text="Idioma de Destino:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        ttk.Combobox(frame_descarga, textvariable=self.idioma_destino, values=["es", "en", "fr", "de", "zh-cn", "ja"]).grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(frame_descarga, text="Modo de Descarga:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        ttk.Combobox(frame_descarga, textvariable=self.modo_descarga, values=["todos", "rango", "especifico"]).grid(row=3, column=1, padx=10, pady=10)

        # Frame para opciones de rango
        self.frame_rango = ttk.Frame(frame_descarga)
        self.frame_rango.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        ttk.Label(self.frame_rango, text="Capítulo Inicio:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_inicio = ttk.Entry(self.frame_rango, textvariable=self.capitulo_inicio)
        self.entry_inicio.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.frame_rango, text="Capítulo Fin:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_fin = ttk.Entry(self.frame_rango, textvariable=self.capitulo_fin)
        self.entry_fin.grid(row=1, column=1, padx=10, pady=10)

        # Frame para opción específica
        self.frame_especifico = ttk.Frame(frame_descarga)
        self.frame_especifico.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        ttk.Label(self.frame_especifico, text="Capítulo Específico:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_especifico = ttk.Entry(self.frame_especifico, textvariable=self.capitulo_especifico)
        self.entry_especifico.grid(row=0, column=1, padx=10, pady=10)

        ttk.Button(frame_descarga, text="Descargar", command=self.iniciar_descarga).grid(row=6, column=0, columnspan=2, pady=20)

        # Inicializar visibilidad de los frames
        self.actualizar_interfaz()

        # Hacer la interfaz autoescalable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def on_select_novela(self, event):
        """Método para manejar la selección de una novela."""
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item[0])
            # Obtener la URL de la novela del diccionario almacenado
            novela_data = self.tree.item(selected_item[0])['values']
            if hasattr(self, 'novelas_dict') and novela_data[0] in self.novelas_dict:
                url_novela = self.novelas_dict[novela_data[0]]['url_novela']
                self.url_novela.set(url_novela)
                self.status_label.config(text=f"Novela seleccionada: {novela_data[0]}")

    def on_url_base_change(self, event):
        """Método para manejar el cambio de URL base."""
        selected_url = self.url_base.get()
        print(f"URL base seleccionada: {selected_url}")
        # Actualizar la interfaz según la URL seleccionada
        self.status_label.config(text=f"URL base cambiada a: {selected_url}")

    def actualizar_interfaz(self, *args):
        """Actualiza la visibilidad de los frames según el modo de descarga."""
        modo = self.modo_descarga.get()
        if modo == "todos":
            self.frame_rango.grid_remove()
            self.frame_especifico.grid_remove()
        elif modo == "rango":
            self.frame_rango.grid()
            self.frame_especifico.grid_remove()
        elif modo == "especifico":
            self.frame_rango.grid_remove()
            self.frame_especifico.grid()

    def buscar_novela_interfaz(self):
        """Maneja la búsqueda de novelas desde la interfaz gráfica."""
        termino_busqueda = self.entry_busqueda.get()
        if not termino_busqueda:
            messagebox.showerror("Error", "Por favor, ingresa un término de búsqueda.")
            return

        resultados = self.novel_controller.buscar_novela(termino_busqueda)
        if resultados:
            # Limpiar resultados anteriores
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Crear diccionario para almacenar la información completa de las novelas
            self.novelas_dict = {}
            
            # Insertar nuevos resultados
            for novela in resultados:
                self.tree.insert('', 'end', values=(
                    novela['nombre'],
                    novela['ultimo_capitulo']
                ))
                # Almacenar la información completa de la novela
                self.novelas_dict[novela['nombre']] = novela
        else:
            messagebox.showinfo("Información", "No se encontraron resultados.")

    def iniciar_descarga(self):
        """Inicia la descarga de la novela utilizando el controlador."""
        try:
            url_novela = self.url_novela.get()
            url_base = self.url_base.get()
            idioma_destino = self.idioma_destino.get()
            modo_descarga = self.modo_descarga.get()
            
            # Convertir strings a integers
            capitulo_inicio = int(self.capitulo_inicio.get())
            capitulo_fin = int(self.capitulo_fin.get())
            capitulo_especifico = int(self.capitulo_especifico.get())
            
            # Actualizar estado inicial
            self.status_label.config(text="Obteniendo URLs de capítulos...")
            self.progress['value'] = 0
            self.root.update_idletasks()
            
            # Llamar al método descargar_novela del controlador
            self.chapter_controller.descargar_novela(
            url_novela=url_novela,
            url_base=url_base,  # Pasar la URL base
            idioma_destino=idioma_destino,
            modo_descarga=modo_descarga,
            capitulo_inicio=capitulo_inicio,
            capitulo_fin=capitulo_fin,
            capitulo_especifico=capitulo_especifico)
            
            # Mensaje de finalización
            self.progress['value'] = 100
            self.status_label.config(text="¡Descarga completada!")
            messagebox.showinfo("Éxito", "La descarga se ha completado exitosamente.")
                
        except ValueError:
            self.status_label.config(text="Error: Números inválidos")
            messagebox.showerror("Error", "Por favor, ingrese números válidos para los capítulos")
            return
        except Exception as e:
            self.status_label.config(text="Error en la descarga")
            messagebox.showerror("Error", f"Error al descargar: {str(e)}")
            return


if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # Usar un tema moderno
    app = MainWindow(root)
    root.mainloop()
