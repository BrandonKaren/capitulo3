from operator import truediv


can_fly=bool(input("¿puede volar?"))
is_human=bool(input("¿es humano?"))
has_mask=bool(input("¿tiene mascara?"))

if can_fly=='Si' and is_human=='Si' and has_mask=='Si': 
    print("iroman")
elif can_fly=='Si' and is_human=='Si' and has_mask=='No':
    print("captain marvel")

if can_fly=='Si' and is_human=='No' and has_mask=='Si':
    print("ronan accuser")

if can_fly=='si' and is_human=='no' and has_mask=='no':
    print("vision")
    
if can_fly=='no' and is_human=='si' and has_mask=='si':
    print("spiderman")
    
if can_fly=='no' and is_human=='si' and has_mask=='no':
    print("hulk")
    
if can_fly=='no' and is_human=='no' and has_mask=='si':
    print("black bolt")
    if can_fly=='si' and is_human=='no' and has_mask== 'no':
        print("thanos")
