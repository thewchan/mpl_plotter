import inspect
import numpy as np
import matplotlib as mpl

from matplotlib import font_manager
from matplotlib.ticker import FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LightSource

from importlib import import_module

from mpl_plotter.resources.mock_data import MockData

# from matplotlib import rc
# from matplotlib import colors
# from matplotlib import cm
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.colors import LightSource
# import matplotlib.dates as mdates
# from numpy import sin, cos
# from skimage import measure
# from pylab import floor
# from mpl_plotter.resources.functions import print_color
# from mpl_plotter.resources.colormaps import ColorMaps


class plot:

    def init(self):
        if not isinstance(self.backend, type(None)):
            try:
                mpl.use(self.backend)
            except AttributeError:
                raise AttributeError(
                    '{} backend not supported with current Python configuration'.format(self.backend))

        # matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
        # or matplotlib.backends is imported for the first time.

        self.plt = import_module("matplotlib.pyplot")

        self.run()

    def method_setup(self):
        if isinstance(self.fig, type(None)):
            if not self.plt.get_fignums():
                self.method_figure()
            else:
                self.fig = self.plt.gcf()
                self.ax = self.plt.gca()

        if isinstance(self.ax, type(None)):
            self.ax = self.fig.add_subplot(self.shape_and_position, adjustable='box', projection='3d')

    def method_figure(self):
        if not isinstance(self.style, type(None)):
            self.plt.style.use(self.style)
        self.fig = self.plt.figure(figsize=self.figsize)

    def method_style(self):
        if self.light:
            self.workspace_color = 'black' if isinstance(self.workspace_color, type(None)) else self.workspace_color
            self.workspace_color2 = (193 / 256, 193 / 256, 193 / 256) if isinstance(self.workspace_color2, type(
                None)) else self.workspace_color2
            self.style = 'classic'
        elif self.dark:
            self.workspace_color = 'white' if isinstance(self.workspace_color, type(None)) else self.workspace_color
            self.workspace_color2 = (89 / 256, 89 / 256, 89 / 256) if isinstance(self.workspace_color2,
                                                                                 type(None)) else self.workspace_color2
            self.style = 'dark_background'
        else:
            self.workspace_color = 'black' if isinstance(self.workspace_color, type(None)) else self.workspace_color
            self.workspace_color2 = (193 / 256, 193 / 256, 193 / 256) if isinstance(self.workspace_color2, type(
                None)) else self.workspace_color2
            self.style = None

    def method_legend(self):
        if self.legend is True:
            legend_font = font_manager.FontProperties(family=self.font,
                                                      weight=self.legend_weight,
                                                      style=self.legend_style,
                                                      size=self.legend_size)
            self.ax.legend(loc=self.legend_loc, prop=legend_font,
                           handleheight=self.legend_handleheight, ncol=self.legend_ncol)

    def method_resize_axes(self):
        if self.resize_axes is True:
            self.z_pad = self.z_pad if self.z_pad > (abs(self.z.max()) + abs(self.z.min())) / 16 else (abs(self.z.max()) + abs(self.z.min())) / 16
            if isinstance(self.x_bounds, type(None)):
                self.x_bounds = (self.x.min(), self.x.max())
            if isinstance(self.y_bounds, type(None)):
                self.y_bounds = (self.y.min(), self.y.max())
            if isinstance(self.z_bounds, type(None)):
                self.z_bounds = (self.z.min(), self.z.max())
            self.ax.set_xlim3d(self.x_bounds[0] - self.x_pad, self.x_bounds[1] + self.x_pad)
            self.ax.set_ylim3d(self.y_bounds[0] - self.y_pad, self.y_bounds[1] + self.y_pad)
            self.ax.set_zlim3d(self.z_bounds[0] - self.z_pad, self.z_bounds[1] + self.z_pad)

    def method_save(self):
        if self.filename:
            self.plt.savefig(self.filename, dpi=self.dpi)

    def method_show(self):
        if self.more_subplots_left is not True:
            self.fig.tight_layout()
            self.plt.show()
        else:
            print('Ready for next subplot')

    def method_background_alpha(self):
        self.ax.patch.set_alpha(1)

    def method_title(self):
        if not isinstance(self.title, type(None)):

            self.ax.set_title(self.title, y=self.title_y,
                              fontname=self.font if isinstance(self.title_font, type(None)) else self.title_font,
                              weight=self.title_weight,
                              color=self.workspace_color if isinstance(self.title_color, type(None)) else self.title_color,
                              size=self.title_size)
            self.ax.title.set_position((0.5, self.title_y))

    def method_axis_labels(self):
        if not isinstance(self.x_label, type(None)):

            self.ax.set_xlabel(self.x_label, fontname=self.font, weight=self.x_label_weight,
                               color=self.workspace_color, size=self.x_label_size, labelpad=self.x_label_pad,
                               rotation=self.x_label_rotation)
        if not isinstance(self.y_label, type(None)):

            self.ax.set_ylabel(self.y_label, fontname=self.font, weight=self.y_label_weight,
                               color=self.workspace_color, size=self.y_label_size, labelpad=self.y_label_pad,
                               rotation=self.y_label_rotation)

        if not isinstance(self.z_label, type(None)):
            if self.z_label_bold is True:
                weight = 'bold'
            else:
                weight = 'normal'
            self.ax.set_zlabel(self.z_label, fontname=self.font, weight=weight,
                               color=self.workspace_color, size=self.z_label_size, labelpad=self.z_label_pad,
                               rotation=self.z_label_rotation)

    def method_spines(self):
        spine_color = self.workspace_color
        for spine in self.ax.spines.values():
            spine.set_color(spine_color)

        top = True
        right = True
        left = True
        bottom = True

        for spine in self.spines_removed:
            self.ax.spines[spine].set_visible(False)
            if spine == 'top':
                top = False
            if spine == 'bottom':
                bottom=False
            if spine == 'left':
                left = False
            if spine == 'right':
                right = False

        self.ax.tick_params(axis='both', which='both', top=top, right=right, left=left, bottom=bottom)

    def method_ticks(self):
        #   Color
        if self.tick_color is not None:
            self.ax.tick_params(axis='both', color=self.tick_color)

            self.ax.w_xaxis.line.set_color(self.tick_color)
            self.ax.w_yaxis.line.set_color(self.tick_color)
            self.ax.w_zaxis.line.set_color(self.tick_color)
        #   Label size
        if self.tick_label_size is not None:
            self.ax.tick_params(axis='both', labelsize=self.tick_label_size)
        #   Numeral size
        for tick in self.ax.get_xticklabels():
            tick.set_fontname(self.font)
        for tick in self.ax.get_yticklabels():
            tick.set_fontname(self.font)
        for tick in self.ax.get_zticklabels():
            tick.set_fontname(self.font)
        #   Float format
        float_format = '%.' + str(self.tick_ndecimals) + 'f'
        self.ax.xaxis.set_major_formatter(FormatStrFormatter(float_format))
        self.ax.yaxis.set_major_formatter(FormatStrFormatter(float_format))
        self.ax.zaxis.set_major_formatter(FormatStrFormatter(float_format))

        # Tick number
        if self.x_tick_number is not None:
            self.ax.xaxis.set_major_locator(self.plt.MaxNLocator(self.x_tick_number, prune=self.prune))
        if self.y_tick_number is not None:
            self.ax.yaxis.set_major_locator(self.plt.MaxNLocator(self.y_tick_number, prune=self.prune))
        if self.z_tick_number is not None:
            self.ax.zaxis.set_major_locator(self.plt.MaxNLocator(self.z_tick_number, prune=self.prune))

        # Tick label pad
        if self.tick_label_pad is not None:
            self.ax.tick_params(axis='both', pad=self.tick_label_pad)

        # Tick rotation
        if self.x_tick_rotation is not None:
            self.ax.tick_params(axis='x', rotation=self.x_tick_rotation)
        if self.y_tick_rotation is not None:
            self.ax.tick_params(axis='y', rotation=self.y_tick_rotation)
        if self.z_tick_rotation is not None:
            self.ax.tick_params(axis='z', rotation=self.z_tick_rotation)

    def method_grid(self):
        if self.grid is not False:
            self.plt.grid(linestyle=self.grid_lines, color=self.grid_color)

    def method_pane_fill(self):
        # Pane fill and pane edge color
        self.ax.xaxis.pane.fill = self.pane_fill
        self.ax.yaxis.pane.fill = self.pane_fill
        self.ax.zaxis.pane.fill = self.pane_fill
        self.ax.xaxis.pane.set_edgecolor(self.tick_color)
        self.ax.yaxis.pane.set_edgecolor(self.tick_color)

    def method_scale(self):
        # Scaling
        max_scale = max(self.x_scale, self.y_scale, self.z_scale)
        x_scale = self.x_scale / max_scale
        y_scale = self.y_scale / max_scale
        z_scale = self.z_scale / max_scale

        # Reference:
        # https://stackoverflow.com/questions/30223161/matplotlib-mplot3d-how-to-increase-the-size-of-an-axis-stretch-in-a-3d-plo
        self.ax.get_proj = lambda: np.dot(Axes3D.get_proj(self.ax), np.diag([x_scale, y_scale, z_scale, 1]))


class dim_01:

    def run(self):

        self.method_style()

        self.method_setup()

        # Scale axes
        self.method_scale()

        # Mock plot
        self.mock()

        # Plot
        self.main()

        # Legend
        self.method_legend()

        # Resize axes
        self.method_resize_axes()

        # Makeup
        self.method_background_alpha()
        self.method_title()
        self.method_axis_labels()
        self.method_spines()
        self.method_ticks()
        self.method_grid()
        self.method_pane_fill()

        # Save
        self.method_save()

        self.method_show()

        return self.ax


class dim_2:

    def run(self):

        self.method_style()

        self.method_setup()

        # Scale axes
        self.method_scale()

        # Mock plot
        self.mock()

        # Plot
        self.main()

        # Plot line edges to plot color
        self.method_edges_to_rgba()

        # Legend
        self.method_legend()

        # Resize axes
        self.method_resize_axes()

        # Makeup
        self.method_background_alpha()
        self.method_title()
        self.method_axis_labels()
        self.method_spines()
        self.method_ticks()
        self.method_grid()
        self.method_pane_fill()

        # Save
        self.method_save()

        self.method_show()

        return self.ax

    def method_lighting(self):
        ls = LightSource(270, 45)
        rgb = ls.shade(self.z, cmap=cm.get_cmap(self.cmap), vert_exag=0.1, blend_mode='soft')
        return rgb

    def method_edges_to_rgba(self):
        if self.edges_to_rgba is True:
            self.graph.set_edgecolors(self.graph.to_rgba(self.graph._A))


class line(plot, dim_01):

    def __init__(self,
                 # Specifics
                 line_width=5,
                 x=None, x_scale=1,
                 y=None, y_scale=1,
                 z=None, z_scale=1,
                 # Base
                 backend='Qt5Agg', plot_label='Line', font='serif',
                 # Figure, axis
                 fig=None, ax=None, figsize=None, shape_and_position=111,
                 # Setup
                 prune=None, resize_axes=True, aspect=1, box_to_plot_pad=10, spines_removed=('top', 'right'),
                 workspace_color=None, workspace_color2=None, light=None, dark=None, pane_fill=None,
                 # Bounds
                 x_bounds=None, y_bounds=None, z_bounds=None,
                 # Pads
                 x_pad=0, y_pad=0, z_pad=0,
                 # Grid
                 grid=False, grid_color='black', grid_lines='-.',
                 # Color
                 color='darkred', cmap='RdBu_r', alpha=None,
                 # Bounds
                 # Title
                 title=None, title_weight=None, title_size=12, title_y=1.025, title_color=None, title_font=None,
                 # Labels
                 x_label=None, x_label_weight=None, x_label_size=12, x_label_pad=5, x_label_rotation=None,
                 y_label=None, y_label_weight=None, y_label_size=12, y_label_pad=5, y_label_rotation=None,
                 z_label=None, z_label_weight=None, z_label_size=12, z_label_pad=5, z_label_rotation=None,
                 # Ticks
                 x_tick_number=5, x_tick_labels=None,
                 y_tick_number=5, y_tick_labels=None,
                 z_tick_number=5, z_tick_labels=None,
                 x_tick_rotation=None, y_tick_rotation=None, z_tick_rotation=None,
                 tick_color=None, tick_label_pad=5, tick_ndecimals=1,
                 # Tick labels
                 tick_label_size=7, tick_label_size_x=None, tick_label_size_y=None, tick_label_size_z=None,
                 # Color bar
                 color_bar=False, extend='neither', shrink=0.75,
                 cb_title=None, cb_axis_labelpad=10, cb_tick_number=5,
                 cb_outline_width=None, cb_title_rotation=None, cb_title_style='normal', cb_title_size=10,
                 cb_top_title_y=1, cb_ytitle_labelpad=10, cb_title_weight='normal', cb_top_title=False,
                 cb_y_title=False, cb_top_title_pad=None, cb_top_title_x=0, cb_vmin=None, cb_vmax=None,
                 cb_ticklabelsize=10,
                 # Legend
                 legend=False, legend_loc='upper right', legend_size=13, legend_weight='normal',
                 legend_style='normal', legend_handleheight=None, legend_ncol=1,
                 # Subplots
                 more_subplots_left=True,
                 # Save
                 filename=None, dpi=None,
                 ):

        """
        Line plot class
        mpl_plotter - 3D
        """

        # Turn all instance arguments to instance attributes
        for item in inspect.signature(line).parameters:
            setattr(self, item, eval(item))

        # Coordinates
        self.x = self.x if isinstance(self.x, type(None)) or isinstance(self.x, np.ndarray) else np.array(self.x)
        self.y = self.y if isinstance(self.y, type(None)) or isinstance(self.y, np.ndarray) else np.array(self.y)
        self.z = self.z if isinstance(self.z, type(None)) or isinstance(self.z, np.ndarray) else np.array(self.z)

        self.init()

    def main(self):

        self.graph = self.ax.plot3D(self.x, self.y, self.z, alpha=self.alpha, linewidth=self.line_width,
                                    color=self.color, label=self.plot_label)

    def mock(self):
        if isinstance(self.x, type(None)) and isinstance(self.y, type(None)) and isinstance(self.z, type(None)):
            self.x = np.linspace(-2, 2, 1000)
            self.y = np.sin(self.x)
            self.z = np.cos(self.x)


class surface(plot, dim_2):

    def __init__(self,
                 # Specifics
                 x=None, x_scale=1,
                 y=None, y_scale=1,
                 z=None, z_scale=1,
                 # Specifics: surface
                 edge_color='b', edges_to_rgba=True, rstride=1, cstride=1, line_width=0,
                 # Specifics: lighting
                 lighting=False, antialiased=False, shade=False,
                 # Specifics: color
                 norm=None, c=None,
                 # Base
                 backend='Qt5Agg', plot_label='Surface', font='serif',
                 # Figure, axis
                 fig=None, ax=None, figsize=None, shape_and_position=111,
                 # Setup
                 prune=None, resize_axes=True, aspect=1, box_to_plot_pad=10, spines_removed=('top', 'right'),
                 workspace_color=None, workspace_color2=None, light=None, dark=None, pane_fill=None,
                 # Bounds
                 x_bounds=None, y_bounds=None, z_bounds=None,
                 # Pads
                 x_pad=0, y_pad=0, z_pad=0,
                 # Grid
                 grid=False, grid_color='black', grid_lines='-.',
                 # Color
                 color='darkred', cmap='RdBu_r', alpha=None,
                 # Bounds
                 # Title
                 title=None, title_weight=None, title_size=12, title_y=1.025, title_color=None, title_font=None,
                 # Labels
                 x_label=None, x_label_weight=None, x_label_size=12, x_label_pad=5, x_label_rotation=None,
                 y_label=None, y_label_weight=None, y_label_size=12, y_label_pad=5, y_label_rotation=None,
                 z_label=None, z_label_weight=None, z_label_size=12, z_label_pad=5, z_label_rotation=None,
                 # Ticks
                 x_tick_number=5, x_tick_labels=None,
                 y_tick_number=5, y_tick_labels=None,
                 z_tick_number=5, z_tick_labels=None,
                 x_tick_rotation=None, y_tick_rotation=None, z_tick_rotation=None,
                 tick_color=None, tick_label_pad=5, tick_ndecimals=1,
                 # Tick labels
                 tick_label_size=7, tick_label_size_x=None, tick_label_size_y=None, tick_label_size_z=None,
                 # Color bar
                 color_bar=False, extend='neither', shrink=0.75,
                 cb_title=None, cb_axis_labelpad=10, cb_tick_number=5,
                 cb_outline_width=None, cb_title_rotation=None, cb_title_style='normal', cb_title_size=10,
                 cb_top_title_y=1, cb_ytitle_labelpad=10, cb_title_weight='normal', cb_top_title=False,
                 cb_y_title=False, cb_top_title_pad=None, cb_top_title_x=0, cb_vmin=None, cb_vmax=None,
                 cb_ticklabelsize=10,
                 # Legend
                 legend=False, legend_loc='upper right', legend_size=13, legend_weight='normal',
                 legend_style='normal', legend_handleheight=None, legend_ncol=1,
                 # Subplots
                 more_subplots_left=True,
                 # Save
                 filename=None, dpi=None,
                 ):
        """
        Surface plot class
        mpl_plotter - 3D
        """

        # Turn all instance arguments to instance attributes
        for item in inspect.signature(surface).parameters:
            setattr(self, item, eval(item))

        # Coordinates
        self.x = self.x if isinstance(self.x, type(None)) or isinstance(self.x, np.ndarray) else np.array(self.x)
        self.y = self.y if isinstance(self.y, type(None)) or isinstance(self.y, np.ndarray) else np.array(self.y)
        self.z = self.z if isinstance(self.z, type(None)) or isinstance(self.z, np.ndarray) else np.array(self.z)

        self.init()

    def main(self):
        self.graph = self.ax.plot_surface(self.x, self.y, self.z, cmap=self.cmap,
                                          edgecolors=self.edge_color, alpha=self.alpha,
                                          rstride=self.rstride, cstride=self.cstride, linewidth=self.line_width,
                                          norm=self.norm, facecolors=self.method_lighting() if self.lighting is True else None,
                                          antialiased=self.antialiased, shade=self.shade,
                                          label=self.plot_label)
        self.graph._facecolors2d = self.graph._facecolors3d
        self.graph._edgecolors2d = self.graph._edgecolors3d

    def mock(self):
        if isinstance(self.x, type(None)) and isinstance(self.y, type(None)) and isinstance(self.z, type(None)):
            self.x, self.y, self.z = MockData().hill()


class utils:

    def floating_text(self, ax, text, font, x, y, z, size=20, weight='normal', color='darkred'):
        # Font
        font = {'family': font,
                'color': color,
                'weight': weight,
                'size': size,
                }
        # Floating text
        ax.text(x, y, z, text, size=size, weight=weight, fontdict=font)
