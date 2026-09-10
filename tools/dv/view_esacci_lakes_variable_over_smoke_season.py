r"""
view_esacci_lakes_variable_over_smoke_season.py

Written by William Chuter-Davies
"""

# Standard Library Imports
import argparse
import sys

from pathlib import Path

# Related Third-party Imports
import matplotlib.pyplot as plt
import numpy             as np
import pandas            as pd

# Local Application/Library Specific Imports
from lib.esacci_lakes.utils.io   import (
    add_argument_esacci_lakes_variable,
    add_argument_hylak_field,
    add_argument_esacci_lakes_hylak_fields_csv_path,
    argument_esacci_lakes_variable_is_in_esacci_lakes_variables,
    argument_hylak_field_is_in_hylak_fields,
    argument_esacci_lakes_hylak_fields_csv_path_exists,
    read_esacci_lakes_hylak_fields_csv
)
from lib.esacci_lakes.utils.math import merge_dfs_on_esacci_lakes_id
from lib.esacci_lakes.vars       import (
    ESACCI_LAKES_VARIABLES,
    HYLAK_FIELDS
)
from lib.io.vars                 import (
    RETURN_FAILURE,
    RETURN_SUCCESS
)
from lib.math.utils              import filter_df_by_column_bounds
from lib.plot.utils              import force_ax_xtick_visibility

PROG = "view_esacci_lakes_variable_over_smoke_season.py"


def add_argument_esacci_lakes_variable_over_high_smoke_season_csv_path(
    parser: argparse.ArgumentParser
) -> None:
    """
    Adds a `esacci_lakes_variable_over_high_smoke_season_csv_path`
    argument to a :class:`ArgumentParser`.

    Parameters
    ----------
    parser : :class:`ArgumentParser`
        The parser

    Returns
    -------
    None

    Notes
    -----
    Argument `esacci_lakes_variable_over_high_smoke_season_csv_path` is
    of type :class:`Path`.
    """
    parser.add_argument(
        "esacci_lakes_variable_over_high_smoke_season_csv_path",
        type=Path,
        help="""path to some csv file produced by comp_esacci_lakes_variable_over_smoke_season.py"""
    )


def argument_esacci_lakes_variable_over_high_smoke_season_csv_path_exists(
    esacci_lakes_variable_over_high_smoke_season_csv_path: Path,
    *,
    loud:                                                  bool = False
) -> bool:
    """
    Validates `esacci_lakes_variable_over_high_smoke_season_csv_path`.

    Parameters
    ----------
    esacci_lakes_variable_over_high_smoke_season_csv_path :
    :class:`pathlib.Path`
        The argument
        `esacci_lakes_variable_over_high_smoke_season_csv_path`

    loud : bool
        If `True`, prints an error message to stdout. default=False

    Returns
    -------
    `True` if
    `esacci_lakes_variable_over_high_smoke_season_csv_path` exists.
    `False` otherwise.
    """
    if esacci_lakes_variable_over_high_smoke_season_csv_path.exists():
        return True

    if loud:
        print(f"""error: argument esacci_lakes_variable_over_high_smoke_season_csv_path: no such file or directory: {esacci_lakes_variable_over_high_smoke_season_csv_path}""")

    return False


def read_esacci_lakes_variable_over_high_smoke_season_csv(
    esacci_lakes_variable_over_high_smoke_season_csv_path: Path
) -> pd.DataFrame:
    """
    Reads `esacci_lakes_variable_over_high_smoke_season_csv_path` into
    a :class:`pandas.DataFrame`.

    Parameters
    ----------
    esacci_lakes_variable_over_high_smoke_season_csv_path :
    :class:`pathlib.Path`
        The path to some csv file as produced by
        comp_esacci_lakes_variable_over_smoke_season.py

    Returns
    -------
    A :class:`pandas.DataFrame`.
    """
    return pd.read_csv(
        esacci_lakes_variable_over_high_smoke_season_csv_path,
        index_col="esacci_lakes_id"
    )


def add_argument_esacci_lakes_variable_over_low_smoke_season_csv_path(
    parser: argparse.ArgumentParser
) -> None:
    """
    Adds a `esacci_lakes_variable_over_low_smoke_season_csv_path`
    argument to a :class:`ArgumentParser`.

    Parameters
    ----------
    parser : :class:`ArgumentParser`
        The parser

    Returns
    -------
    None

    Notes
    -----
    Argument `esacci_lakes_variable_over_low_smoke_season_csv_path` is
    of type :class:`Path`.
    """
    parser.add_argument(
        "esacci_lakes_variable_over_low_smoke_season_csv_path",
        type=Path,
        help="""path to some csv file produced by comp_esacci_lakes_variable_over_smoke_season.py"""
    )


def argument_esacci_lakes_variable_over_low_smoke_season_csv_path_exists(
    esacci_lakes_variable_over_low_smoke_season_csv_path: Path,
    *,
    loud:                                                 bool = False
) -> bool:
    """
    Validates `esacci_lakes_variable_over_low_smoke_season_csv_path`.

    Parameters
    ----------
    esacci_lakes_variable_over_low_smoke_season_csv_path :
    :class:`pathlib.Path`
        The argument
        `esacci_lakes_variable_over_low_smoke_season_csv_path`

    loud : bool
        If `True`, prints an error message to stdout. default=False

    Returns
    -------
    `True` if `esacci_lakes_variable_over_low_smoke_season_csv_path`
    exists. `False` otherwise.
    """
    if esacci_lakes_variable_over_low_smoke_season_csv_path.exists():
        return True

    if loud:
        print(f"""error: argument esacci_lakes_variable_over_low_smoke_season_csv_path: no such file or directory: {esacci_lakes_variable_over_low_smoke_season_csv_path}""")

    return False


def read_esacci_lakes_variable_over_low_smoke_season_csv(
    esacci_lakes_variable_over_low_smoke_season_csv_path: Path
) -> pd.DataFrame:
    """
    Reads `esacci_lakes_variable_over_low_smoke_season_csv_path` into a
    :class:`pandas.DataFrame`.

    Parameters
    ----------
    esacci_lakes_variable_over_low_smoke_season_csv_path :
    :class:`pathlib.Path`
        The path to some csv file as produced by
        comp_esacci_lakes_variable_over_smoke_season.py

    Returns
    -------
    A :class:`pandas.DataFrame`.
    """
    return pd.read_csv(
        esacci_lakes_variable_over_low_smoke_season_csv_path,
        index_col="esacci_lakes_id"
    )


def build_parser(
) -> argparse.ArgumentParser:
    """
    Builds a :class:`ArgumentParser`.

    Returns
    -------
    A :class:`ArgumentParser`.
    """
    parser = argparse.ArgumentParser(
        prog=PROG,
        usage="%(prog)s [options]",
        description=""""""
    )

    # Positional arguments
    add_argument_esacci_lakes_variable(parser)
    add_argument_esacci_lakes_variable_over_high_smoke_season_csv_path(parser)
    add_argument_esacci_lakes_variable_over_low_smoke_season_csv_path(parser)
    add_argument_hylak_field(parser)
    add_argument_esacci_lakes_hylak_fields_csv_path(parser)

    return parser


def arguments_are_valid(
    args: argparse.Namespace
) -> bool:
    """
    Validates `args`.

    Returns
    -------
    `True` if all arguments are successfully validated. `False`
    otherwise.
    """
    if not argument_esacci_lakes_variable_is_in_esacci_lakes_variables(
        args.esacci_lakes_variable,
        loud=True
    ):
        return False

    if not argument_esacci_lakes_variable_over_high_smoke_season_csv_path_exists(
        args.esacci_lakes_variable_over_high_smoke_season_csv_path,
        loud=True
    ):
        return False

    if not argument_esacci_lakes_variable_over_low_smoke_season_csv_path_exists(
        args.esacci_lakes_variable_over_low_smoke_season_csv_path,
        loud=True
    ):
        return False

    if not argument_hylak_field_is_in_hylak_fields(
        args.hylak_field,
        loud=True
    ):
        return False

    if not argument_esacci_lakes_hylak_fields_csv_path_exists(
        args.esacci_lakes_hylak_fields_csv_path,
        loud=True
    ):
        return False

    return True


def get_lower_bounds_lakes_df(
    df:          pd.DataFrame,
    hylak_field: str
) -> pd.DataFrame:
    """
    Returns `df` filtered to lakes at or below `hylak_field`'s lower
    bound.

    Parameters
    ----------
    df : :class:`pandas.DataFrame`
        The :class:`pandas.DataFrame`

    hylak_field : :class:`str`
        The HydroLAKES field id

    Returns
    -------
    A :class:`pandas.DataFrame`.

    Notes
    -----
    Internal `HYLAK_FIELDS` lookup assumes `hylak_field` has a non-`None`
    `lower_bound`.
    """
    return filter_df_by_column_bounds(
        df=df,
        column=hylak_field,
        lower=None,
        upper=HYLAK_FIELDS[hylak_field].lower_bound
    )


def get_upper_bounds_lakes_df(
    df:          pd.DataFrame,
    hylak_field: str
) -> pd.DataFrame:
    """
    Returns `df` filtered to lakes at or above `hylak_field`'s upper
    bound.

    Parameters
    ----------
    df : :class:`pandas.DataFrame`
        The :class:`pandas.DataFrame`

    hylak_field : :class:`str`
        The HydroLAKES field id

    Returns
    -------
    A :class:`pandas.DataFrame`.

    Notes
    -----
    Internal `HYLAK_FIELDS` lookup assumes `hylak_field` has a non-`None`
    `upper_bound`.
    """
    return filter_df_by_column_bounds(
        df=df,
        column=hylak_field,
        lower=HYLAK_FIELDS[hylak_field].upper_bound,
        upper=None
    )


def plot_lakes_df_scatterplot(
    ax:       plt.Axes, # type: ignore
    lakes_df: pd.DataFrame,
    color:    str,
    label:    str | None = None
) -> None:
    """
    Plots a scatterplot of `lakes_df`'s week columns onto `ax`, limited
    to weeks in [-3, 20].

    Parameters
    ----------
    ax : :class:`matplotlib.axes.Axes`
        The axes to plot onto

    lakes_df : :class:`pandas.DataFrame`
        The :class:`pandas.DataFrame`

    color : :class:`str`
        The point color

    label : :class:`str`
        The legend label

    Returns
    -------
    None

    Notes
    -----
    Internal `pandas.DataFrame.filter` call assumes `lakes_df` has one
    or more columns named "w_{n}", where `n` is a week number. Only
    columns whose week number `n` is in [-3, 20] are plotted.
    """
    prefix = "w_"

    for label_, ser in lakes_df.filter(like=prefix).items():
        n = int(label_.removeprefix(prefix)) # type: ignore

        if (
            n < -3 
            or n > 20
        ):
            continue

        ax.scatter(
            x=[n] * len(ser),
            y=ser,
            label=label,
            color=color,
            edgecolors="none",
            alpha=0.1
        )


def plot_lakes_df_lineplot(
    ax:       plt.Axes, # type: ignore
    lakes_df: pd.DataFrame,
    color:    str,
    label:    str | None = None
) -> None:
    """
    Plots a line of `lakes_df`'s week columns' medians onto `ax`,
    limited to weeks in [-3, 20].

    Parameters
    ----------
    ax : :class:`matplotlib.axes.Axes`
        The axes to plot onto

    lakes_df : :class:`pandas.DataFrame`
        The :class:`pandas.DataFrame`

    color : :class:`str`
        The line color

    label : :class:`str`
        The legend label

    Returns
    -------
    None

    Notes
    -----
    Internal `pandas.DataFrame.filter` call assumes `lakes_df` has one
    or more columns named "w_{n}", where `n` is a week number. Only
    columns whose week number `n` is in [-3, 20] are plotted.
    """
    prefix = "w_"
    x      = []
    y      = []

    for label_, ser in lakes_df.filter(like=prefix).items():
        n = int(label_.removeprefix(prefix)) # type: ignore

        if (
            n < -3 
            or n > 20
        ):
            continue

        x.append(n)
        y.append(ser.median())

    ax.plot(
        x,
        y,
        label=label,
        color=color,
        marker="o"
    )


def plot_on_upper_bounds_lakes_ax(
    upper_bounds_lakes_ax: plt.Axes, # type: ignore
    upper_high_lakes_df:   pd.DataFrame,
    upper_low_lakes_df:    pd.DataFrame
) -> None:
    """
    Plots `upper_high_lakes_df` and `upper_low_lakes_df` onto
    `upper_bounds_lakes_ax`.

    Parameters
    ----------
    upper_bounds_lakes_ax : :class:`matplotlib.axes.Axes`
        The axes to plot onto

    upper_high_lakes_df : :class:`pandas.DataFrame`
        Upper-bounds-depth lakes during a high smoke season

    upper_low_lakes_df : :class:`pandas.DataFrame`
        Upper-bounds-depth lakes during a low smoke season

    Returns
    -------
    None
    """
    plot_lakes_df_scatterplot(
        upper_bounds_lakes_ax,
        upper_high_lakes_df,
        color="#FF0000"
    )
    plot_lakes_df_lineplot(
        upper_bounds_lakes_ax,
        upper_high_lakes_df,
        color="#FF0000",
        label="High Smoke Season (Median)"
    )

    plot_lakes_df_scatterplot(
        upper_bounds_lakes_ax,
        upper_low_lakes_df,
        color="#0000FF"
    )
    plot_lakes_df_lineplot(
        upper_bounds_lakes_ax,
        upper_low_lakes_df,
        color="#0000FF", 
        label="Low Smoke Season (Median)"
    )


def plot_on_lower_bounds_lakes_ax(
    lower_bounds_lakes_ax: plt.Axes, # type: ignore
    lower_high_lakes_df:   pd.DataFrame,
    lower_low_lakes_df:    pd.DataFrame
) -> None:
    """
    Plots `lower_high_lakes_df` and `lower_low_lakes_df` onto
    `lower_bounds_lakes_ax`.

    Parameters
    ----------
    lower_bounds_lakes_ax : :class:`matplotlib.axes.Axes`
        The axes to plot onto

    lower_high_lakes_df : :class:`pandas.DataFrame`
        Lower-bounds-depth lakes during a high smoke season

    lower_low_lakes_df : :class:`pandas.DataFrame`
        Lower-bounds-depth lakes during a low smoke season

    Returns
    -------
    None
    """
    plot_lakes_df_scatterplot(
        lower_bounds_lakes_ax,
        lower_high_lakes_df,
        color="#FF0000"
    )
    plot_lakes_df_lineplot(
        lower_bounds_lakes_ax,
        lower_high_lakes_df,
        color="#FF0000",
        label="High Smoke Season (Median)"
    )
    
    plot_lakes_df_scatterplot(
        lower_bounds_lakes_ax,
        lower_low_lakes_df,
        color="#0000FF"
    )
    plot_lakes_df_lineplot(
        lower_bounds_lakes_ax,
        lower_low_lakes_df,
        color="#0000FF",
        label="Low Smoke Season (Median)"
    )


def set_upper_bounds_lakes_ax_properties(
    upper_bounds_lakes_ax: plt.Axes, # type: ignore
    esacci_lakes_variable: str,
    hylak_field:           str
) -> None:
    """
    Sets `upper_bounds_lakes_ax`'s properties, including its title,
    x-axis label, and y-axis label.

    Parameters
    ----------
    upper_bounds_lakes_ax : :class:`matplotlib.axes.Axes`
        The axes to set properties on

    esacci_lakes_variable : :class:`str`
        The ESA CCI Lakes variable id

    hylak_field : :class:`str`
        The HydroLAKES field id

    Returns
    -------
    None
    """
    upper_bounds_lakes_ax.set_title(f"""Weekly {ESACCI_LAKES_VARIABLES[esacci_lakes_variable].long_name} Anomaly for lakes with {HYLAK_FIELDS[hylak_field].long_name} >= {HYLAK_FIELDS[hylak_field].upper_bound}{HYLAK_FIELDS[hylak_field].units}""")
    upper_bounds_lakes_ax.set_xlabel("Week relative to start of smoke season")
    upper_bounds_lakes_ax.set_ylabel(f"""{ESACCI_LAKES_VARIABLES[esacci_lakes_variable].long_name} ({ESACCI_LAKES_VARIABLES[esacci_lakes_variable].units}) Anomaly""")
    upper_bounds_lakes_ax.set_xticks(np.arange(-3, 21).tolist())
    
    force_ax_xtick_visibility(upper_bounds_lakes_ax)


def set_lower_bounds_lakes_ax_properties(
    lower_bounds_lakes_ax: plt.Axes, # type: ignore
    esacci_lakes_variable: str,
    hylak_field:           str
) -> None:
    """
    Sets `lower_bounds_lakes_ax`'s properties, including its title,
    x-axis label, and y-axis label.

    Parameters
    ----------
    lower_bounds_lakes_ax : :class:`matplotlib.axes.Axes`
        The axes to set properties on

    esacci_lakes_variable : :class:`str`
        The ESA CCI Lakes variable id

    hylak_field : :class:`str`
        The HydroLAKES field id

    Returns
    -------
    None
    """
    lower_bounds_lakes_ax.set_title(f"""Weekly {ESACCI_LAKES_VARIABLES[esacci_lakes_variable].long_name} Anomaly for lakes with {HYLAK_FIELDS[hylak_field].long_name} <= {HYLAK_FIELDS[hylak_field].lower_bound}{HYLAK_FIELDS[hylak_field].units}""")
    lower_bounds_lakes_ax.set_xlabel("Week relative to start of smoke season")
    lower_bounds_lakes_ax.set_ylabel(f"""{ESACCI_LAKES_VARIABLES[esacci_lakes_variable].long_name} ({ESACCI_LAKES_VARIABLES[esacci_lakes_variable].units}) Anomaly""")
    lower_bounds_lakes_ax.set_xticks(np.arange(-3, 21).tolist())
    
    force_ax_xtick_visibility(lower_bounds_lakes_ax)


def main(
) -> int:
    """
    Orchestration layer.

    Returns
    -------
    0 if program completes successfully. 1 otherwise.
    """
    args = build_parser().parse_args()
    
    if not arguments_are_valid(args): 
        return RETURN_FAILURE

    variable_over_high_smoke_season_df = read_esacci_lakes_variable_over_high_smoke_season_csv(args.esacci_lakes_variable_over_high_smoke_season_csv_path)
    variable_over_low_smoke_season_df  = read_esacci_lakes_variable_over_low_smoke_season_csv(args.esacci_lakes_variable_over_low_smoke_season_csv_path)
    hylak_fields_df                    = read_esacci_lakes_hylak_fields_csv(args.esacci_lakes_hylak_fields_csv_path)

    variable_over_high_smoke_season_hylak_fields_df = merge_dfs_on_esacci_lakes_id(
        variable_over_high_smoke_season_df,
        hylak_fields_df
    )
    variable_over_low_smoke_season_hylak_fields_df  = merge_dfs_on_esacci_lakes_id(
        variable_over_low_smoke_season_df,
        hylak_fields_df
    )

    upper_high_lakes_df = get_upper_bounds_lakes_df(
        variable_over_high_smoke_season_hylak_fields_df,
        args.hylak_field
    )
    upper_low_lakes_df  = get_upper_bounds_lakes_df(
        variable_over_low_smoke_season_hylak_fields_df,
        args.hylak_field
    )
    lower_high_lakes_df = get_lower_bounds_lakes_df(
        variable_over_high_smoke_season_hylak_fields_df,
        args.hylak_field
    )
    lower_low_lakes_df  = get_lower_bounds_lakes_df(
        variable_over_low_smoke_season_hylak_fields_df,
        args.hylak_field
    )

    _, (upper_bounds_lakes_ax, lower_bounds_lakes_ax) = plt.subplots(
        nrows=2,
        ncols=1,
        sharex=True,
        sharey=True
    )

    plot_on_upper_bounds_lakes_ax(
        upper_bounds_lakes_ax,
        upper_high_lakes_df,
        upper_low_lakes_df
    )
    plot_on_lower_bounds_lakes_ax(
        lower_bounds_lakes_ax,
        lower_high_lakes_df,
        lower_low_lakes_df
    )

    set_upper_bounds_lakes_ax_properties(
        upper_bounds_lakes_ax,
        args.esacci_lakes_variable,
        args.hylak_field
    )
    set_lower_bounds_lakes_ax_properties(
        lower_bounds_lakes_ax,
        args.esacci_lakes_variable,
        args.hylak_field
    )

    lower_bounds_lakes_ax.legend()
    upper_bounds_lakes_ax.legend()
    plt.tight_layout()
    plt.show()
    
    return RETURN_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
