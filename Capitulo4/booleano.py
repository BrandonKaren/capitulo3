can_fly=bool(input("¿puede volar?"))
is_human=bool(input("¿es humano?"))
has_mask=bool(input("¿tiene mascara?"))

if can_fly==True and is_human==True and has_mask==True: 
    print("iroman")
elif can_fly==True and is_human==True and has_mask==False:
    print("captain marvel")

if can_fly==True and is_human==False and has_mask==True:
    print("ronan accuser")

if can_fly==True and is_human==False and has_mask==False:
    print("vision")
    
if can_fly==False and is_human==True and has_mask==True:
    print("spiderman")
    
if can_fly==False and is_human==True and has_mask==False:
    print("hulk")
    
if can_fly==False and is_human==False and has_mask==True:
    print("black bolt")
    if can_fly==False and is_human==False and has_mask== False:
        print("thanos")