from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


def convert_to_float(value_str):
    """This functions convert string to float"""
    suf = {"k": 1e3, "M": 1e6, "B": 1e9}
    return float(value_str[:-1]) * suf[value_str[-1]]


def main():
    """This functions displays the projection of life expectancy in relation
to the gross national product of the year 1900 for each country."""
    try:
        income_data = load(
            "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expectancy_data = load("../life_expectancy_years.csv")
        year = 1900

        income_1900 = income_data[str(year)]
        life_expectancy_1900 = life_expectancy_data[str(year)]

        plt.scatter(income_1900.values, life_expectancy_1900.values)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title(f"{year}")
        plt.xscale("log")
        plt.gca().xaxis.set_major_formatter(EngFormatter())
        plt.grid(True)
        plt.savefig("test.png")
        plt.show()
        plt.close()
    except Exception as e:
        print('Error:', e)
        exit(1)


if __name__ == "__main__":
    main()
