import argparse
import pandas as pd

def main():
    if args.total:
        fil_data = data[data["Year"] == args.total]
        if fil_data.empty:
            print(f"Немає даних для року {args.total}.")
            return
        countries_medals = fil_data.groupby("Team")["Medal"].value_counts().unstack(fill_value=0)

        result = [f"Країни-медалісти {args.total}:"]
        for country, medals in countries_medals.iterrows():
            result.append(f"{country} - золото: {medals.get('Gold', 0)}, срібло: {medals.get('Silver', 0)}, бронза: {medals.get('Bronze', 0)}")

        result_text = "\n".join(result)
        print(result_text)


    elif args.medals:
        fil_data = data[(data["Year"] == args.year) & ((data["Team"].str.contains(args.country)) | (data["NOC"] == args.country))]
        if fil_data.empty:
            print("Немає даних для вказаної країни чи року.")
            return
        medalists = fil_data[["Name", "Event", "Medal"]].dropna().head(10)
        medal_counts = fil_data["Medal"].value_counts()
        result = []
        result.append("Перші 10 медалістів:")
        for _, row in medalists.iterrows():
            result.append(f"{row['Name']} - {row['Event']} - {row['Medal']}")
        result.append("\nСумарна кількість медалей:")
        for medal in ["Gold", "Silver", "Bronze"]:
            count = medal_counts.get(medal, 0)
            result.append(f"{medal}: {count}")
        result_text = "\n".join(result)
        print(result_text)


    elif args.overall:
        result = []
        for country in args.overall:
            country_data = data[(data["Team"].str.contains(country, na=False)) | (data["NOC"] == country)]
            if country_data.empty:
                result.append(f"{country}: Немає даних.")
                continue

            medals_by_year = country_data.groupby("Year")["Medal"].count()
            if medals_by_year.empty:
                result.append(f"{country}: Немає медалей.")
                continue

            best_year = medals_by_year.idxmax()
            best_count = medals_by_year.max()
            result.append(f"{country}: Рік {best_year}, медалей: {best_count}")

        print("\n".join(result))
        return

parser = argparse.ArgumentParser(description="Аналіз медалей олімпіад.")
parser.add_argument('file')
parser.add_argument("year",nargs="?", type=int)
parser.add_argument("country",nargs="?",type=str)
parser.add_argument("-overall", nargs="+", help="Список країн для аналізу.")
parser.add_argument("-total", type=int)
parser.add_argument("-medals", action="store_true")
args = parser.parse_args()
try:
    data = pd.read_csv(args.file)
    main()
except FileNotFoundError:
    print(f"Файл '{args.file}' не знайдено.")
except Exception as e:
    print(f"Помилка під час завантаження файлу: {e}")
