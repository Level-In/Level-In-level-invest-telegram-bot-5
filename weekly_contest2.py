import os
import sys

import requests


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    print("Brak zmiennej środowiskowej TELEGRAM_TOKEN")
    sys.exit(1)


CHAT_IDS = [
    "-1004231126426",
    "-1004249984029",
    "-1003932802265",
]


PHOTO_PATH = "konkurs_miesieczny.png"


MESSAGE_TEXT = """🏆 KONKURS MIESIĘCZNY

Im więcej mieszkań wynajmiesz w danym miesiącu, tym większa premia trafia do Ciebie! 💸

🟢 7 mieszkań to premia 700 zł

⚫ 10 mieszkań to premia 1 200 zł

🟡 12 mieszkań to premia 1 500 zł

🔵 15 mieszkań to premia 1 800 zł

🩷 20 mieszkań to premia 2 500 zł

🟣 25 mieszkań to aż 3 500 zł premii 🤩🔥

Każda kolejna umowa może oznaczać wejście na wyższy poziom. Nie zatrzymuj się po osiągnięciu pierwszego progu. Celuj wyżej, działaj konsekwentnie i walcz o maksymalną nagrodę! 🚀🏅

📌 Warunki konkursu miesięcznego

✅ Konkurs obejmuje mieszkania wynajęte w danym miesiącu rozliczeniowym

✅ Umowy muszą być przygotowane poprawnie, bez błędów formalnych i braków

✅ Rezygnacje nie są wliczane do wyniku

✅ Liczby przy kwotach oznaczają liczbę mieszkań wynajętych w danym miesiącu

🚀 DZIAŁAMY PO WYNIKI

Nie odliczaj dni. Nie czekaj na idealny moment. To Ty tworzysz okazje! 🔥

Każdy telefon może otworzyć drzwi do spotkania.
Każde spotkanie może zakończyć się umową.
Każda podpisana umowa przybliża Cię do wyższego wyniku i większej premii! 💰

🎯 Wyznacz konkretny cel

📞 Zwiększ aktywność i wykorzystuj każdą szansę

🤝 Buduj zaufanie dzięki najwyższej jakości obsługi

📝 Dbaj o kompletność i poprawność dokumentów

🏆 Celuj w najwyższy próg premiowy

Twój wynik zależy od Twoich działań.
Włącz pełną moc, przejmij inicjatywę i sięgnij po dodatkowe pieniądze! 💪🔥💸"""


def check_photo_exists() -> bool:
    if os.path.exists(PHOTO_PATH):
        print(f"Znaleziono grafikę: {PHOTO_PATH}")
        return True

    print(f"Nie znaleziono grafiki: {PHOTO_PATH}")
    print("Pliki widoczne w repozytorium:")

    for file_name in os.listdir("."):
        print(file_name)

    return False


def send_photo(chat_id: str) -> bool:
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"

    try:
        with open(PHOTO_PATH, "rb") as photo:
            response = requests.post(
                url,
                data={
                    "chat_id": chat_id,
                },
                files={
                    "photo": photo,
                },
                timeout=30,
            )

        print(f"PHOTO CHAT_ID={chat_id} STATUS={response.status_code}")
        print(f"PHOTO RESPONSE={response.text}")

        if response.ok:
            print(f"Grafika wysłana do {chat_id}")
            return True

        print(f"Błąd wysyłki grafiki do {chat_id}")
        return False

    except FileNotFoundError:
        print(f"Nie znaleziono pliku grafiki: {PHOTO_PATH}")
        return False

    except requests.RequestException as error:
        print(f"Błąd połączenia przy wysyłce grafiki do {chat_id}: {error}")
        return False


def send_text(chat_id: str) -> bool:
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    try:
        response = requests.post(
            url,
            json={
                "chat_id": chat_id,
                "text": MESSAGE_TEXT,
                "disable_web_page_preview": True,
            },
            timeout=30,
        )

        print(f"TEXT CHAT_ID={chat_id} STATUS={response.status_code}")
        print(f"TEXT RESPONSE={response.text}")

        if response.ok:
            print(f"Tekst wysłany do {chat_id}")
            return True

        print(f"Błąd wysyłki tekstu do {chat_id}")
        return False

    except requests.RequestException as error:
        print(f"Błąd połączenia przy wysyłce tekstu do {chat_id}: {error}")
        return False


def main() -> None:
    if not check_photo_exists():
        sys.exit(1)

    success_count = 0

    for chat_id in CHAT_IDS:
        print("=" * 60)
        print(f"Wysyłam konkurs miesięczny do grupy: {chat_id}")

        photo_ok = send_photo(chat_id)

        if not photo_ok:
            print(f"Grafika nie została wysłana do {chat_id}. Nie wysyłam samego tekstu.")
            continue

        text_ok = send_text(chat_id)

        if photo_ok and text_ok:
            success_count += 1
            print(f"Komplet wysłany poprawnie do {chat_id}")
        else:
            print(f"Nie wysłano kompletu do {chat_id}")

    print("=" * 60)
    print(f"Wysłano grafikę i tekst do {success_count}/{len(CHAT_IDS)} grup.")

    if success_count != len(CHAT_IDS):
        print("Nie wszystkie grupy dostały komplet. Sprawdź uprawnienia bota do wysyłania zdjęć.")
        sys.exit(1)


if __name__ == "__main__":
    main()
