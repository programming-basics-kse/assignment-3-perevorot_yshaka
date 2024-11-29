import pandas as pd
import argparse


def main():
    fil_data = data[
        (data["Year"] == args.year) & ((data["Team"].str.contains(args.country)) | (data["NOC"] == args.country))
    ]
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
        count = medal_counts.get(medal)
        result.append(f"{medal}: {count}")

    result_text = "\n".join(result)
    print(result_text)
parser = argparse.ArgumentParser(description="Analyse Olympic medals.")
parser.add_argument('file', help="Which file you want to open in .tsv")
parser.add_argument("-medals", action="store_true", help="Specify to analyze medals.")
parser.add_argument("country", help="Country name (Team) or code.")
parser.add_argument("year", type=int, help="Olympic year.")
args = parser.parse_args()
try:
    data = pd.read_csv(args.file)
    main()
except FileNotFoundError:
    print(f"Файл '{args.file}' не знайдено.")
except Exception as e:
    print(f"Помилка під час завантаження файлу: {e}")


