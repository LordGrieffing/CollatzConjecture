import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator



def collatzStorm(x):

    step = 0
    while x != 1:

        if x%2 == 1:
            x = 3*x + 1

        else:
            x = x/2

        step = step + 1

    return step



def main():

    # Prompt user to input the maximum number we will check
    End = 0
    while True:
        try:
            End = int(input("Please input the max number we will check to: "))
            if End <= 0:
                print("You have to select a positive whole number")
            else:
                break
        except ValueError:
            print("You have to select a positive whole number")

    # Build a dataframe
    df = pd.DataFrame(columns=['Start', 'Steps'])

    # Check the Collatz function all the way up to the user input
    for i in range(End):
        steps = collatzStorm(i+1)
        df.loc[i] = [i+1, steps]


    # Print dataframe
    print(df)

    # Plot the results
    sns.lineplot(x='Start', y='Steps', data=df)
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    # Display plot
    plt.show()




if __name__ == "__main__":
    main()