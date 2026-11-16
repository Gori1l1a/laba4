from bs4 import BeautifulSoup
import csv
import requests

countries = []
with open("countries.txt", "r") as file:
    for line in file:
        country = line.strip()
        if country != "":
            countries.append(country)

with open("countries_data.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["country", "city", "area", "population"])

    for country in countries:
        url = "https://en.wikipedia.org/wiki/" + country.replace(" ", "_")
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh)"}

        city = ""
        area = ""
        population = ""

        try:
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                infobox = soup.find("table", class_="infobox")

                if infobox:
                    section = ""

                    for row in infobox.find_all("tr"):
                        th = row.find("th")
                        td = row.find("td")

                        if th and not td:
                            section = th.text.strip().lower()

                        elif th and td:
                            for sup in td.find_all("sup"):
                                sup.decompose()

                            title = th.text.strip().lower()
                            value = td.get_text(" ").replace("\xa0", " ").strip()

                            if "capital" in title and city == "":
                                link = td.find("a")
                                if link:
                                    city = link.text.strip()
                                else:
                                    city = value.split("(")[0].strip()

                            elif "total" in title and section.startswith("area") and area == "":
                                if "km" in value:
                                    number = value.split("km")[0].split()[-1]
                                    area = number.replace(",", "").split(".")[0]

                            elif section.startswith("population") and population == "":
                                if "density" not in title and "rank" not in title:
                                    words = value.split()
                                    for i in range(len(words)):
                                        word = words[i].replace(",", "")
                                        if word[0].isdigit():
                                            number = float(word)
                                            if i + 1 < len(words) and words[i + 1] == "million":
                                                number = number * 1000000
                                            population = str(int(number))
                                            break
            else:
                print(country, ": статус ответа", response.status_code)
        except Exception as error:
            print(country, ": ошибка", error)

        writer.writerow([country, city, area, population])