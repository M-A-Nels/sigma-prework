from datetime import datetime

def get_dob():
    date = input("Enter date of birth (DD-MM-YYYY): ")

    try:
        # Attempt to convert into date time object in correct format
        d_o_b = datetime.strptime(date, "%d-%m-%Y")
        return d_o_b
    except ValueError:
        print("Invalid Date format please enter DD-MM-YYYY. DD and MM have optional leading 0 i.e 01 = 1")
        return 


def calc_age():
    d_o_b = None
    while d_o_b is None:
        d_o_b = get_dob()
    current_date = datetime.now()

    time_diff = current_date - d_o_b #Returns in days and time difference
    return time_diff.days // 365 # Converts to years using days ignores time

if __name__ == "__main__":
    age = calc_age()
    print(age)