
def builder(base, size="chico", condimentos=None):
    """
    podes hacer la bebida en una sola línea
    """
    bebida = base()
    bebida.set_size(size)

    if condimentos:
        for cond in condimentos:
            bebida = cond(bebida)
    return bebida
    return bebida

