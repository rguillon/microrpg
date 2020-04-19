

def get_modifier(str: name):
    modifiers = {   'Longue portée' :   2,
                    'Très longe portée' : 4,
                    'Discrèt' : 3,
                    'Indétectable' : 4,
                    'Usage unique' : 0.2 }
    return modifiers[name]
 
