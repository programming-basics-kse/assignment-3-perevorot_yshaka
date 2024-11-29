
<<<<<<< HEAD
import argparse
import pandas as pd

=======
>>>>>>> efe88dfb625432306981bb492a74293964a2b583
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
    elif args.medal:
        fil_data = data[(data["Year"] == args.year) & ((data["Team"].str.contains(args.country)) | (data["NOC"] == args.country))]
        if fil_data.empty:
            print("Немає даних для вказаної країни чи року.")
            return
        medalists = fil_data[["Name", "Event", "Medal"]].dropna().head(10)
        medal_counts = fil_data["Medal"].value_counts()
        result = []
        result.append("Перші 10 медалістів:")
        for i, row in medalists.iterrows():
            result.append(f"{row['Name']} - {row['Event']} - {row['Medal']}")
        result.append("\nСумарна кількість медалей:")
        for medal in ["Gold", "Silver", "Bronze"]:
            count = medal_counts.get(medal, 0)
            result.append(f"{medal}: {count}")
        result_text = "\n".join(result)
        print(result_text)
parser = argparse.ArgumentParser(description="Аналіз медалей олімпіад.")
parser.add_argument('file')
parser.add_argument("-medals", action="store_true")
parser.add_argument("country", nargs="?")
parser.add_argument("year", nargs="?", type=int)
parser.add_argument("-total", type=int)
args = parser.parse_args()
try:
    data = pd.read_csv(args.file)
    main()
except FileNotFoundError:
    print(f"Файл '{args.file}' не знайдено.")
except Exception as e:
    print(f"Помилка під час завантаження файлу: {e}")