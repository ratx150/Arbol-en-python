class Nodo():
	def __init__ (self,valor,izq=None,der=None):
		self.valor=valor
		self.izquierda=izq
		self.derecha=der

def enOrden(arbol):
	if arbol==None:
		return ""
	else:
		return enOrden(arbol.izquierda)+arbol.valor+enOrden(arbol.derecha)

def buscar(arbol,valor):
	if arbol==None:
		return False
	elif arbol.valor==valor:
		return True
	else:
		return buscar(arbol.izquierda) or buscar(arbol.derecha)

def evaluar(arbol):
	if arbol.valor=='+':
		return evaluar(arbol.izquierda)+evaluar(arbol.derecha)
	elif arbol.valor=='-':
		return evaluar(arbol.izquierda)-evaluar(arbol.derecha)
	elif arbol.valor=='*':
		return evaluar(arbol.izquierda)*evaluar(arbol.derecha)
	elif arbol.valor=='/':
		return evaluar(arbol.izquierda)/evaluar(arbol.derecha)
	else:
		return int(arbol.valor)

print (evaluar(Nodo('+',Nodo('6'),Nodo('-',Nodo('9'),Nodo('7')))))
