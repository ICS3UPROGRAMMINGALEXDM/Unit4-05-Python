#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Gets amount of numbers to add from user.
# Gets numbers from user. Displays equation as well as sum.


def main():
    # Get number of numbers to add together
    max_num = input("Enter the amount of numbers you would like to add together: ")
    try:
        max_numint = int(max_num)
        if max_numint <= 0:
            print("Maximum amount must be a whole and positive number.")
        else:
            # sets everythig to what they need to be
            counter = 0
            n_sum = 0
            equation = ""
            # Loops until max number is reached
            while counter < max_numint:
                u_num = input("Enter a whole and positive number: ")
                try:
                    num = int(u_num)
                    if num <= 0:
                        print("Please ensure number is whole and positive")
                        continue
                    # Update sum
                    n_sum += num
                    # update counter
                    counter += 1
                    # updates the equation
                    if counter < max_numint:
                        equation += u_num + " + "
                    else:
                        equation += u_num + " = "

                except ValueError:
                    print("Please ensure number is positive and whole")
            print("{}{}".format(equation, n_sum))

    except ValueError:
        print(
            "Maximum amount must be a positive and whole NUMBER. Did not receive that."
        )


if __name__ == "__main__":
    main()
