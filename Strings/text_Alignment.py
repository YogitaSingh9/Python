'''In Python, a string of text can be aligned left, right and center.
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H '''
thick=int(input())
c='H'
for i in range(thick):
    print((c*i).rjust(thick-1)+c+(c*i).ljust(thick-1))
for i in range(thick+1):
    print((c*thick).center(thick*2)+(c*thick).center(thick*6))
for i in range((thick+1)//2):
    print((c*thick*5).center(thick*6))
for i in range(thick+1):
        print((c*thick).center(thick*2)+(c*thick).center(thick*6))    
for i in range(thick):
        print(((c*(thick-i-1)).rjust(thick)+c+(c*(thick-i-1)).ljust(thick)).rjust(thick*6)) 
