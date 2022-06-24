from utils import polar_quicksort,determinant,distance_from_point_to_line

def eddyfloyd(E, show=False, save=False, detailed=False):
    E1,E2,pmin,pmax=découpage(E) #on coupe notre liste en deux et on calcule pmin pmax. O(n)
    E1=enveloppe_inf(E1,pmin,pmax) #Calcul de l’enveloppe inférieure (droite) sur E1 de pmin à pmax.
    E2=enveloppe_sup(E2,pmin,pmax) #Calcul de l’enveloppe supérieure (gauche) sur E2 de pmax à pmin 
    return (polar_quicksort(E1+E2,pmax)) #L’enveloppe finale est obtenue par raccordement des deux sous-enveloppes. O(nlog(n))


def découpage(E): #On découpe E en les deux ensembles E1 et E2. On retourne E1 , E2 et les deux points d'abscisse minimale et maximale pmin et pmax qui appartiennent à l'enveloppe. Complexité en O(n).
    n=len(E)
    pmin,pmax=E[0],E[1]
    #On trouve pmin et pmax; O(n)
    for k in range (2,n):
        if pmax[0]<E[k][0]:
            pmax=E[k]
        elif pmin[0]>E[k][0]:
            pmin=E[k]
    E1= []
    E2= []
    for k in range (n):
        if determinant(pmin,E[k],pmax)>0:
            E2.append(E[k])
        elif determinant(pmin,E[k],pmax)<0:
            E1.append(E[k])
    return E1,E2,pmin,pmax

   
def enveloppe_inf(Ei,pmin,pmax): #Complexité en O(n)
    n=len(Ei)
    if n < 2 : #cas de base.
        return(Ei+[pmin]+[pmax])
    else :
        p=Ei[0]
        d=distance_from_point_to_line(p,[pmin,pmax])
        #On récupère le point p le plus éloigné du segment [pmin,pmax]. p appartient à l'enveloppe convexe.
        for k in range(n):
            if distance_from_point_to_line(Ei[k],[pmin,pmax])>d:
                p=Ei[k]
                d=distance_from_point_to_line(Ei[k],[pmin,pmax])
        #On calcule Ei1 et Ei2 situés respectivement à droite des segments [pmin,p] et [p,pmax] de manière récursive.
        Ei1,Ei2=[],[]
        for k in range(n):
            if determinant(pmin,Ei[k],p)<0:
                Ei1.append(Ei[k])
            elif determinant(p,Ei[k],pmax)<0:
                Ei2.append(Ei[k])
        return(enveloppe_inf(Ei1,pmin,p)+enveloppe_inf(Ei2,p,pmax))
    

def enveloppe_sup(Ei,pmin,pmax): #Même chose pour l'enveloppe supérieure, rien ne change hormis le signe du déterminant à considérer.
    n=len(Ei)
    if n < 2 : #cas de base.
        return(Ei+[pmin]+[pmax])
    else :
        p=Ei[0]
        d=distance_from_point_to_line(p,[pmin,pmax])
        #On récupère le point p le plus éloigné du segment [pmin,pmax]. p appartient à l'enveloppe convexe.
        for k in range(n):
            if distance_from_point_to_line(Ei[k],[pmin,pmax])>d:
                p=Ei[k]
                d=distance_from_point_to_line(Ei[k],[pmin,pmax])
        #On calcule Ei1 et Ei2 situés respectivement à droite des segments [pmin,p] et [p,pmax] de manière récursive.
        Ei1,Ei2=[],[]
        for k in range(n):
            if determinant(pmin,Ei[k],p)>0:
                Ei1.append(Ei[k])
            elif determinant(p,Ei[k],pmax)>0:
                Ei2.append(Ei[k])
        return(enveloppe_sup(Ei1,pmin,p)+enveloppe_sup(Ei2,p,pmax))