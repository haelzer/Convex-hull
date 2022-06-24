from utils import determinant


def incremental(points, show=False, save=False, detailed=False):
   S=sorted(points) #Prétraitement: on trie les points selon leur abscisse. O'(nlog(n))
   n=len(S)
   C=[[None,None] for i in range(n)] #Pointeurs sur le prédécesseur/successeur de chaque sommet i. C'est l'équivalent d'une liste doublement chaînée, C[i] donne le prédécesseur et successeur du sommet i.
   
   C[0]=[1,1] #Initialisation de la liste avec les deux premiers points
   C[1]=[0,0]
   
   for i in range(2,n):
       s,sind=S[i-1],(i-1) #s=p(i-1)
       while determinant(s,S[i],S[C[sind][1]])>0: #tant que succ(s) est à droite du segment [pi,s]
           s,sind=S[C[sind][1]],C[sind][1]   #s=succ(s)
           
       p,pind=S[i-1],(i-1) #p=p(i-1)
       while determinant(S[C[pind][0]],S[i],p)>0:  #tant que pred(p) est à droite du segment [p,pi]
           p,pind=S[C[pind][0]],C[pind][0]  #p=pred(p)
           
       #On supprime la partie entre s et p
       C[pind][1]=i
       C[i][0]=pind
       C[i][1]=sind
       C[sind][0]=i
       
   #on reconstitue la liste des sommets de l'enveloppe en parcourant les successeurs sur C à partir du sommet de départ.
   check=[False]*n
   res=[] #on stocke l'enveloppe convexe ici
   k=0
   while not check[k]: #jusqu'à ce que l'on ferme l'enveloppe
       res.append(S[k])
       check[k]=True
       k=C[k][1] #on prend le successeur
   return res

#On montre que la complexité en temps est en O(nlog(n)) grâce au prétraitement (la preuve est déjà faite dans les slides du cours)
#La complexité en espace est O(n) pour le stockage de C et du résultat (l'enveloppe).