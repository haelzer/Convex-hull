from random import seed

from exhaustive import exhaustive
from incremental import incremental
from graham import graham
from eddyfloyd import eddyfloyd
from utils import create_points, scatter_plot


def main():
    """
    A sample main program to test our algorithms.

    @return: None
    """
    # initialize the random generator seed to always use the same set of points
    seed(0)
    # creates some points
    pts = create_points(18)
    show = True  # to display a frame
    save = False  # to save into .png files in "figs" directory
    scatter_plot(pts, [[]], title="convex hull : initial set", show=show, save=save)
    print("Points:", pts)
    # compute the hull
    hull = eddyfloyd(pts, show=show, save=save)
    print("Hull:", hull)
    scatter_plot(pts, [hull], title="convex hull : final result", show=True, save=save)


if __name__ == "__main__":
    main()