import matplotlib.pyplot as plt
import seaborn as sns


# Objects included in this file:

# Functions included in this file:
# # plot_empty
# # plot_heatmap
# # plot_barh


def plot_empty(xlabel=None, ylabel=None,
               title=None,
               figsize=(8,5),
               color=None):
    """Convenience function
    """
    fig = plt.figure(figsize=figsize, dpi=80)
    
    ax = fig.gca()
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=16)
    
    return fig, ax


def plot_heatmap(df, xlabel=None, ylabel=None, title=None,
                 xticklabels=None, yticklabels=None,
                 color=plt.cm.Blues,
                 order=None, figsize=(8, 5)):
    """
    """
    fig = plt.figure(figsize=figsize, dpi=80)
    
    if order:
        df = df[order]
    sns.heatmap(df, cmap=color, annot=True, square=True, fmt='d')
    
    ax = fig.gca()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticklabels(xticklabels)
    ax.set_yticklabels(yticklabels)
    ax.set_title(title, fontsize = 18)
    return fig, ax


def plot_barh(df, x, y, xerr=None, color='#8d1a93',
             xlabel=None, yticklabels=None, title=None,
             figsize=(8, 5)):
    """
    """
    fig, ax = plt.subplots(figsize=figsize)

    if xerr:
        ax.barh(df[y], df[x], xerr=df[xerr], align='center', color=color, capsize=3)
    else:
        ax.barh(df[y], df[x], align='center', color=color, capsize=3)

    ax.set_yticks(df[y])
    if yticklabels:
        ax.set_yticklabels(yticklabels, fontsize=12)
    else:
        ax.set_yticklabels(df[y], fontsize=12)
    
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_title(title, fontsize=16)
    
    return fig, ax
