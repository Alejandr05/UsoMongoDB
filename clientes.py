import tkinter as tk 
from tkinter import messagebox 
from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient('mongo', 27017)
db = client.clientes
collection = db.informacion_cliente

def agregar_cliente():
    id = entry_id.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()

    cliente = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }
    collection.insert_one(cliente)
    messagebox.showinfo("Cliente Agregado", "Cliente agregado exitosamente")

def buscar_cliente():
    cliente_id = entry_id.get()
    cliente = collection.find_one({"id": cliente_id})
    
    if cliente:
        messagebox.showinfo("Cliente Encontrado", f"Nombre: {cliente['nombre']} \nTelefono: {cliente['telefono']}")
    else:
        messagebox.showinfo("Error", "Cliente no encontrado")

def actualizar_cliente():
    cliente_id = entry_id.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()

    cliente_actualizado = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }

    resultado = collection.update_one({"id": cliente_id}, {"$set": cliente_actualizado})

    if resultado.modified_count > 0:
        messagebox.showinfo("Cliente Actualizado", "Cliente actualizado exitosamente")
    else:
        messagebox.showerror("Error", "No se pudo actualizar la información del cliente")

def eliminar_cliente():
    cliente_id = entry_id.get()
    resultado = collection.delete_one({"id": cliente_id})

    if resultado.deleted_count > 0:
        messagebox.showinfo("Cliente Eliminado", "Cliente eliminado exitosamente")
    else:
        messagebox.showerror("Error", "No se puede eliminar el cliente")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Clientes")

# Etiquetas
tk.Label(root, text="ID:").grid(row=0, column=0)
tk.Label(root, text="Nombre:").grid(row=1, column=0)
tk.Label(root, text="Apellido:").grid(row=2, column=0)
tk.Label(root, text="Teléfono:").grid(row=3, column=0)

# Campos de entrada
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)
entry_apellido = tk.Entry(root)
entry_apellido.grid(row=2, column=1)
entry_telefono = tk.Entry(root)
entry_telefono.grid(row=3, column=1)

# Botones
tk.Button(root, text="Agregar Cliente", command=agregar_cliente).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Buscar Cliente", command=buscar_cliente).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(root, text="Actualizar Cliente", command=actualizar_cliente).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(root, text="Eliminar Cliente", command=eliminar_cliente).grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
