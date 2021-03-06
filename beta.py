from numpy import clip
def apply_beta_transform(d, beta, imagearray):
    """
    moltiplicare per il coefficiente β solo le frequenze c_kl con k + l ≥ d (sto assumendo
    che le frequenze partano da 0: se d = 0 le modifico tutte, se d = N +M −2 modifico
    solo la più alta, cioè quella con k = N −1, l = M −1).
    """
    h = imagearray.shape[0]
    w = imagearray.shape[1]
    for k in range(0,h):
        for l in range(0,w):
            if k+l >= d:
                imagearray[k,l]*=beta
                
    return

def norm(f):
    """
    arrotondare ff all’intero più vicino, mettere a zero i valori negativi e a 255 quelli
    maggiori di 255 in modo da avere una immagine ammissibile
    """
    clip(f, 0, 255)