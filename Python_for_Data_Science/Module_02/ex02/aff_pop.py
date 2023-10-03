from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


def convert_to_float(value_str):
    """This functions convert string to float"""
    suf = {"k": 1e3, "M": 1e6, "B": 1e9}
    return float(value_str[:-1]) * suf[value_str[-1]]


def main():
    """This functions displays the country information of your campus versus
other country of your choice."""
    try:
        country_name = "France"
        other_country = "United Kingdom"
        data = load("../population_total.csv")
        print(data)
        france_data = data.loc[data["country"] == country_name]
        other_data = data.loc[data["country"] == other_country]

        x = data.columns[1:].astype(int)
        y_data = [convert_to_float(val) for val in france_data.values[0][1:]]
        y_other = [convert_to_float(val) for val in other_data.values[0][1:]]
        print("Year  Population")
        for year, population1, population2 in zip(x, y_data, y_other):
            print(f"{year}   {population1:.0f}   {population2:.0f}")
        plt.plot(x, y_data, label=f"{country_name} Population")
        plt.plot(x, y_other, label=f"{other_country} Population")
        plt.xlim(1850, 2050)
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title(f"Population Comparison: {country_name} vs. {other_country}")
        plt.legend()
        plt.gca().yaxis.set_major_formatter(EngFormatter())
        plt.grid(True)
        plt.savefig("test.png")
        plt.show()
        plt.close()
    except Exception as e:
        print('Error:', e)
        exit(1)


if __name__ == "__main__":
    main()
