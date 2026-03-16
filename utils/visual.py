from rich.table import Table
from rich.console import Console
# import plotext as plt
import matplotlib.pyplot as plt

STYLE_COLOR = {"train": "blue", "valid": "green", "test": "red"}


def show_table(history):
    # Extract metrics and modes
    metrics = history["test"].keys()
    modes = history.keys()

    # Show table
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Epoch")
    for mode in modes:
        for metric in metrics:
            table.add_column(
                f"{mode.capitalize()} {metric.upper()}", style=STYLE_COLOR[mode]
            )
    for epoch in range(len(history["test"]["loss"])):
        row = [str(epoch + 1)]
        for mode in modes:
            for metric in metrics:
                value = history[mode][metric][epoch]
                row.append(f"{value:.3f}")
        table.add_row(*row)
    console.print(table)


# def show_plot(history):
#     # Extract metrics and modes
#     metrics = history["test"].keys()
#     modes = history.keys()

#     # Show plot for each metric
#     plt.clf()  # Clear any previous plot data
#     plt.plot_size(200, 20)
#     plt.subplots(1, len(metrics))
#     for i, metric in enumerate(metrics):
#         epochs = [epoch + 1 for epoch in range(len(history["test"]["loss"]))]
#         plt.subplot(1, i + 1)

#         # Plotting's settings
#         plt.title(f"{metric.upper()} vs Epoch")
#         plt.xticks(epochs)

#         # Plot data
#         for mode in modes:
#             plt.plot(
#                 epochs,
#                 history[mode][metric],
#                 color=STYLE_COLOR[mode],
#                 label=f"{mode.capitalize()} {metric.upper()}",
#             )

#     # Show all plots
#     plt.show()




def show_plot(history, plot_name):
    # Extract metrics and modes
    metrics = history["test"].keys()
    modes = history.keys()

    # Create a figure for the plots
    num_metrics = len(metrics)
    fig, axes = plt.subplots(1, num_metrics, figsize=(5 * num_metrics, 5))

    if num_metrics == 1:
        axes = [axes]  # Ensure axes is iterable for a single metric

    for i, metric in enumerate(metrics):
        epochs = [epoch + 1 for epoch in range(len(history["test"]["loss"]))]
        ax = axes[i]

        # Plot settings
        ax.set_title(f"{metric.upper()} vs Epoch")
        ax.set_xlabel("Epoch")
        ax.set_ylabel(metric.upper())
        ax.set_xticks(epochs)

        # Plot data
        for mode in modes:
            ax.plot(
                epochs,
                history[mode][metric],
                color=STYLE_COLOR[mode],
                label=f"{mode.capitalize()} {metric.upper()}",
            )
        ax.legend()

    # Save the plot as an image file
    plt.tight_layout()
    plt.savefig(plot_name)
    plt.show()


def show_simple_history_plot(history, plot_name="history.png"):

    metrics = history.keys()
    epochs = range(1, len(next(iter(history.values()))) + 1)

    fig, axes = plt.subplots(1, len(metrics), figsize=(5 * len(metrics), 5))

    if len(metrics) == 1:
        axes = [axes]

    for ax, metric in zip(axes, metrics):
        ax.plot(epochs, history[metric], marker="o")
        ax.set_title(metric.replace("_", " ").title())
        ax.set_xlabel("Epoch")
        ax.set_ylabel(metric.replace("_", " ").title())
        ax.set_xticks(epochs)

    plt.tight_layout()
    plt.savefig(plot_name)
    plt.show()