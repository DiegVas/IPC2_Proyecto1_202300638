from modules import Extract_file, Generate_graph, Process_file, Show_data, Upload_file


def mostrar_menu():
    print("\n-------------- Menú principal ---------------\n")
    print("[1]. Cargar archivo")
    print("[2]. Procesar archivo")
    print("[3]. Escribir archivo salida")
    print("[4]. Mostrar datos del estudiante")
    print("[5]. Generar gráfica")
    print("[6]. Salida")
    print("")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        print("\n-----------------------------\n")
        
        if opcion == '1':
    
            # Lógica para cargar archivo
            Upload_file()
                    
        elif opcion == '2':
            
            # Lógica para procesar archivo
            Process_file()
            
        elif opcion == '3':
           
            # Lógica para escribir archivo de salida
            Extract_file()
            
        elif opcion == '4':
            
            # Lógica para mostrar datos del estudiante
            Show_data()
            
        elif opcion == '5':
            
            
            # Lógica para generar gráfica
            Generate_graph()
            
        elif opcion == '6':
            print("\n---- ¡Saliendo! ----\n")
            break
        
        else:
            print("\n---- ¡Opción no válida, por favor intente de nuevo.! ----\n")

if __name__ == "__main__":
    main()