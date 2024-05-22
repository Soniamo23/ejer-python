import os
import shutil

# Directorio raíz a buscar (cambia esto según sea necesario)
ROOT_DIR = "/ruta/del/directorio"
# Directorio de backup
BACKUP_DIR = "/ruta/del/backup"

# Extensiones de archivos sensibles a buscar
SENSITIVE_EXTENSIONS = [".db", ".sql", ".key", ".pem"]
# Extensiones de archivos importantes a buscar para el backup
IMPORTANT_EXTENSIONS = [".log"]

def listar_archivos_sensibles(root_dir, extensions):
    print("Listando archivos sensibles...")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if any(file.endswith(ext) for ext in extensions):
                print(os.path.join(dirpath, file))

def crear_backup_archivos_importantes(root_dir, backup_dir, extensions):
    print("Creando backup de archivos importantes...")
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(dirpath, file)
                shutil.copy2(file_path, backup_dir)
    
    print(f"Backup completado. Los archivos importantes se han copiado a {backup_dir}")

if __name__ == "__main__":
    listar_archivos_sensibles(ROOT_DIR, SENSITIVE_EXTENSIONS)
    crear_backup_archivos_importantes(ROOT_DIR, BACKUP_DIR, IMPORTANT_EXTENSIONS)
