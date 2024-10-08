from matplotlib import pyplot as plt


def output_plots(us, n_output, dt, T_cold, T_hot):
    # Create figure
    # Output 4 figures at these timesteps

    fig_counter = 0
    fig = plt.figure()

    for n, u in enumerate(us):
        if n in n_output:
            fig_counter += 1
            ax = fig.add_subplot(220 + fig_counter)
            im, ax = create_plot(ax, u, T_cold, T_hot)
            ax.set_axis_off()
            ax.set_title('{:.1f} ms'.format(n * dt * 1000))

    # Plot output figures
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)

    return fig


def create_plot(ax, u, T_cold, T_hot):
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    return im, ax
