import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option("--number", "-n", default=1)
def sin(number):
    """"Calculates the sin of a range of numbers from 0 to 2pi in the amount of steps you give.
    
    Args: 
        number (Any): a given number
        
    Returns:
        print: a dataframe of all calculated sines
    """ 
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@cmd_group.command()
@click.option("--number", "-n", default=1)
def tan(number):
    """"Calculates the tan of a range of numbers from 0 to 2pi in the amount of steps you give.
    
    Args: 
        number (Any): a given number
        
    Returns:
        print: a dataframe of all calculated tan
    """ 
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()
