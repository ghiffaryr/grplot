def check_padding(x, y, fig, hpad, wpad, pad):
    if hpad is not None or wpad is not None:
        if hpad is None:
            raise Exception('hpad argument must not be None!')
        elif wpad is None:
            raise Exception('wpad argument must not be None!')
        else:
            fig.tight_layout(h_pad=hpad, w_pad=wpad)
    elif pad is not None:
        fig.tight_layout(pad=pad)
    else:
        pass
    return fig