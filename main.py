from aPila import automataPila
from interfaz import ventana

if __name__ == "__main__":
    lista_estados = [['p','#'],['p','z'],['p','x'],['q','#'],['q','z'],['q','x']]
    lista_simbolos = ['z','x','c','λ']
    estado_inicial = 'p'
    estado_final = 'r'
    matriz_transicion = [
        [['p','#z'],['p','#x'],['q','#'],[None]],
        [['p','zz'],['p','zx'],['q','z'],[None]],
        [['p','xz'],['p','xx'],['q','x'],[None]],
        [[None],[None],[None],['r','#']],
        [['q','λ'],[None],[None],[None]],
        [[None],['q','λ'],[None],[None]],    
    ]
    pilaVacia = ['#']
    aP = automataPila(estado_inicial,estado_final,lista_simbolos,lista_estados,matriz_transicion,pilaVacia)
    #aP._comprobarPalabra('aacaa')
    
    
    ventana(aP)._runApp()