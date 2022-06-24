from utils import determinant, distance


def graham(points, show=False, save=False, detailed=False):
    
    #Fonction pour calculer le pivot
    def ordre_pivot(A, B):
       return (A[1] < B[1]) or (A[1] == B[1] and A[0] <= B[0])
   
    def calcul_pivot(s):
       m = s[0]
       for x in s:
           if ordre_pivot(x, m): 
               m = x
       return m
   
    #Fonctions pour trier selon l'angle formé par un point avec le pivot et l'axe des abscisses
    def ordre_angle(A,B,pivot): #On définit la relaiton d'ordre associée
       d=determinant(pivot,A,B)
       if d>0: return True
       elif d <0 : return False
       else : return distance(pivot,A)<=distance(pivot,B) #cas d'égalité, on regarde la distance au pivot
      
        
    def fusion(t1,t2,pivot): #On écrit un algo de tri par comparaison optimal (tri fusion ici) avec notre nouvelle relation d'ordre
       if t1==[]:
           return t2
       elif t2==[]:
           return t1
       else:
           if ordre_angle(t1[0],t2[0],pivot):
               return [t1[0]] + fusion(t1[1:],t2,pivot)
           else:
               return [t2[0]] + fusion(t1,t2[1:],pivot)
    def tri_fusion(T,pivot): #O(nlog(n))
       if len(T)<=1:
           return T
       else:
           c = len(T)//2
           return fusion(tri_fusion(T[0:c],pivot),tri_fusion(T[c:],pivot),pivot)
       
    #Prétraitement de l'algorithme
    S=[]
    pivot=calcul_pivot(points)
    l=tri_fusion(points,pivot) #On commence avec la liste triée
    S.append(l[0]) #On inirialise avec les trois premiers points
    S.append(l[1])
    S.append(l[2])
    #On fait tourner l'algorithme
    for k in range(3,len(l)):
        while determinant(S[-2],S[-1],l[k])<0:
            S.pop()
        S.append(l[k])

    return S #On retourne l'enveloppe convexe

#Complexité en temps en O(nlog(n)) à cause du tri.
#Complexité en espace en O(n)