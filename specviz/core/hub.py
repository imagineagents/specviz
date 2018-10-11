from qtpy.QtWidgets import QApplication


class Hub:
    def __init__(self, workspace, *args, **kwargs):
        self._workspace = workspace

    @property
    def workspace(self):
        """The active workspace."""
        return self._workspace

    @property
    def model(self):
        """The data item model of the active workspace."""
        return self.workspace.model

    @property
    def proxy_model(self):
        """The proxy model of the active workspace."""
        return self.workspace.proxy_model

    @property
    def plot_window(self):
        """The currently selected plot window of the workspace."""
        return self.workspace.current_plot_window

    @property
    def plot_windows(self):
        """The currently selected plot window of the workspace."""
        return self.workspace.mdi_area.subWindowList()

    @property
    def plot_widget(self):
        """The plot widget of the currently active plot window."""
        return self.workspace.current_plot_window.plot_widget

    @property
    def plot_item(self):
        """The currently selected plot item."""
        if self.workspace is not None:
            return self.workspace.current_item

    @property
    def plot_items(self):
        """Returns the currently selected plot item."""
        return self.proxy_model.items

    @property
    def visible_plot_items(self):
        """Plotted data that are currently visible."""
        if self.plot_widget is not None:
            return self.plot_widget.listDataItems()

    @property
    def selected_region(self):
        """The currently active ROI on the plot."""
        return self.plot_window.plot_widget.selected_region

    @property
    def selected_region_bounds(self):
        """The bounds of currently active ROI on the plot."""
        return self.plot_window.plot_widget.selected_region_bounds

    @property
    def data_item(self):
        """The data item of the currently selected plot item."""
        if self.plot_item is not None:
            return self.plot_item.data_item

    @property
    def data_items(self):
        """List of all data items held in the data item model."""
        return self.model.items