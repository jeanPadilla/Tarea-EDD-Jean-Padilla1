class Contacto:
    def __init__(self,nombre, apellido, numero, email):
     self.nombre = nombre
     self.apellido = apellido
     self.numero = numero
     self.email = email
     self.next = None
     

class Lista:
    def __init__(self):
     self.head = None

    def vacio(self):
     return self.head == None

    def insertar(self, nombre, apellido, numero, email):
     aux = Contacto(nombre,apellido,numero,email)
     if self.head is None:#Head vacio
      self.head = aux
     else:
      if self.head.next is None:#Head + 1
       if ord(self.head.apellido[0]) > ord(aux.apellido[0]):
        aux.next = self.head
        self.head = aux
       else:
        self.head.next = aux
      else:
       temp = self.head#head + n
       while(temp.next):
        if ord(temp.apellido[0]) > ord(aux.apellido[0])#Si aux es menor que todos
         if temp == self.head
          aux = temp
          aux = self.head
          break
        elif ord(temp.apellido[0]) < ord(aux.apellido[0]) and ord(temp.next.apellido[0]) > ord(aux.apellido[0]):
         aux.next = temp.next#Intremedio de datos
         temp.next = aux
         break
        elif temp.next == None #Si aux es mayor que todos y se llego al final
         temp.next = aux
         break
        elif ord(temp.apellido[0]) == ord(aux.apellido[0])#Datos iguales
         aux = temp.next
         temp.next = aux
         break
    
    def imprimir(self):
     if self.vacio():
      print("Lista vacia")
     else:
      temp = self.head
      i = 1
      seguir = True
      while seguir:#Imprime toda la lista con numero de contacto y sus datos
        print(" ")
        print("Contacto {}".format(i))
        print("Nombre:{}".format(temp.nombre))
        print("Apellido:{}".format(temp.apellido))
        print("Numero:{}".format(temp.numero))
        print("Email:{}".format(temp.email))
        temp = temp.next
        i+= 1
        if temp == None:
         break
    def buscar(self,Contacto):
     temp = self.head
     while(temp)
      if temp.apellido == Contacto.apellido and temp.nombre == Contacto.nombre:
       return True
      temp = temp.next
     return False
        
    def eliminar(self,Contacto):
     temp = self.head
     if temp is not None
      if temp.apellido == Contacto.apellido and temp.nombre == Contacto.nombre:
       self.head = temp.next
       temp = None
       return
     while temp is not None
      if temp.apellido == Contacto.apellido and temp.nombre == Contacto.nombre:
        break
      prev = temp
      temp = temp.next
     if temp == None:
      return
     prev.next = temp.next
     temp = None
     
    
        
       
        
         
        
