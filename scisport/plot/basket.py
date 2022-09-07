from textwrap import fill
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def basketplot(length=94, width=50):
    '''
        in feet
    '''
    linecolor = 'black'

    fig = plt.figure(figsize=(length / 2, width / 2))
    ax = fig.add_subplot(1, 1, 1)

    rect = plt.Rectangle((0, 0), length, width, color='#8EDD83')
    ax.add_patch(rect)

    # base
    plt.plot([0, 0], [0, width], color=linecolor)
    plt.plot([0, length], [0, 0], color=linecolor)
    plt.plot([length, length], [0, width], color=linecolor)
    plt.plot([0, length], [width, width], color=linecolor)
    plt.plot([length/2, length/2], [0, width], color=linecolor)


    # circle
    cCircle = plt.Circle((length / 2, width/2), 6, color=linecolor, fill=None)
    lCircle = plt.Circle((19, width/2), 6, color=linecolor, fill=None)
    rCircle = plt.Circle((length - 19, width/2), 6, color=linecolor, fill=None)

    ax.add_patch(cCircle)
    ax.add_patch(lCircle)
    ax.add_patch(rCircle)

    lRect = plt.Rectangle((0, (width - 16) / 2),
                          19, 16, color=linecolor, fill=None)
    rRect = plt.Rectangle((length-19, (width - 16) / 2),
                          19, 16, color=linecolor, fill=None)
    ax.add_patch(lRect)
    ax.add_patch(rRect)

    # three point line
    plt.plot([0, 14], [3, 3], color=linecolor)
    plt.plot([0, 14], [width - 3, width - 3], color=linecolor)
    plt.plot([length - 14, length], [3, 3], color=linecolor)
    plt.plot([length - 14, length], [width - 3, width - 3], color=linecolor)

    lArc = Arc((14, width/2), height=width - 6, width=28, angle=0,
               theta1=270, theta2=90, color=linecolor)
    rArc = Arc((length - 14, width/2), height=width - 6, width=28, angle=0,
               theta1=90, theta2=270, color=linecolor)

    ax.add_patch(lArc)
    ax.add_patch(rArc)

    plt.plot([4, 4], [(width / 2) - 3, (width / 2) + 3], color=linecolor)
    plt.plot([length - 4, length - 4], [(width / 2) - 3, (width / 2) + 3], color=linecolor)

    rsCircle = plt.Circle((5.5, width/2), 0.7, color=linecolor, fill=None)
    lsCircle = plt.Circle((length - 5.5, width/2), 0.7, color=linecolor, fill=None)

    ax.add_patch(rsCircle)
    ax.add_patch(lsCircle)



    plt.axis('off')
    return ax, fig