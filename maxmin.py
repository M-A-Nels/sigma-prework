def min_max(int_array):
    sorted_array = sorted(int_array)
    return [sorted_array[0],sorted_array[-1]]

def input_array():
    array = input('Enter a list of integers separated by commas i.e "1,12": ')
    try:
        int_array = [int(num.strip()) for num in array.split(',')]
        return int_array
    except ValueError:
        print('Invalid List format')
        return

if __name__ == "__main__":
    print("Program designed on assumption input is always an integer array.")
    print("Tests:")

    print("Input [2, 4, 1, 0, 2, -1]")
    print(f"Output {min_max([2, 4, 1, 0, 2, -1])}")
    print()
    print("Input [20, 50, 12, 6, 14, 8]")
    print(f"Output {min_max([20, 50, 12, 6, 14, 8])}")
    print()
    print("Input [100,-100]")
    print(f"Output {min_max([-100, 100])}")
    print()

    print("Try your own")
    int_array = None
    while int_array is None:
        int_array = input_array()
    print(min_max(int_array))
