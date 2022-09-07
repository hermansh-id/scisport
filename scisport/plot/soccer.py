import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def soccerplot(length = 120, width=90):
    
    linecolor = 'black'

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    rect = plt.Rectangle((0, 0), length, width, color='#8EDD83')
    ax.add_patch(rect)


    # base 
    plt.plot([0, 0], [0, width], color=linecolor)
    plt.plot([0, length], [0, 0], color=linecolor)
    plt.plot([length, length], [0, width], color=linecolor)
    plt.plot([0, length], [width, width], color=linecolor)
    plt.plot([length/2, length/2], [0, width], color=linecolor)

    # penalty area 1
    ux1 = (width - 44) / 2
    plt.plot([18, 18], [ux1, ux1+44], color=linecolor)
    plt.plot([0, 18], [ux1, ux1], color=linecolor)
    plt.plot([0, 18], [ux1+44, ux1+44], color=linecolor)

    # penalty area 2
    plt.plot([length - 18, length - 18], [ux1, ux1+44], color=linecolor)
    plt.plot([length - 18, length], [ux1, ux1], color=linecolor)
    plt.plot([length - 18, length], [ux1+44, ux1+44], color=linecolor)

    # goal area
    ux2 = (width - 12) / 2
    plt.plot([6, 6], [ux2, ux2+12], color=linecolor)
    plt.plot([0, 6], [ux2, ux2], color=linecolor)
    plt.plot([0, 6], [ux2+12, ux2+12], color=linecolor)

    # goal area 2
    plt.plot([length - 6, length - 6], [ux2, ux2+12], color=linecolor)
    plt.plot([length - 6, length], [ux2, ux2], color=linecolor)
    plt.plot([length - 6, length], [ux2+12, ux2+12], color=linecolor)

    # circle
    cCircle = plt.Circle((length / 2, width/2), 10, color=linecolor, fill=None)
    cSpot = plt.Circle((length / 2, width/2), 0.8, color=linecolor)
    lSpot = plt.Circle((12, width/2), 0.8, color=linecolor)
    rSpot = plt.Circle((length - 12, width/2), 0.8, color=linecolor)

    ax.add_patch(cCircle)
    ax.add_patch(cSpot)
    ax.add_patch(lSpot)
    ax.add_patch(rSpot)

    # arc
    lArc = Arc((18, width/2), height=12, width=12, angle=0,
               theta1=270, theta2=90, color=linecolor)
    rArc = Arc((length - 18, width/2), height=12, width=12, angle=0,
               theta1=90, theta2=270, color=linecolor)

    ax.add_patch(lArc)
    ax.add_patch(rArc)

    plt.axis('off')
    return ax, fig


if __name__ == '__main__':
    fig, ax = soccerplot()

    plt.title('Shots Map')
    plt.show()
