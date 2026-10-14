# Konkursy Telegram Level Invest

Oba konkursy są uruchamiane automatycznie przez GitHub Actions z gałęzi `main` tego repozytorium.

| Konkurs | Termin w Europe/Warsaw | Workflow |
| --- | --- | --- |
| Tygodniowy | poniedziałki o 11:35 | [weekly_contest.yml](.github/workflows/weekly_contest.yml) |
| Miesięczny | 1., 10., 15., 25. i 30. dnia miesiąca o 12:00 | [weekly_contest2.yml](.github/workflows/weekly_contest2.yml) |

Zmiana czasu letniego i zimowego jest obsługiwana automatycznie. Dzień 30 jest pomijany w lutym.
Oba workflow korzystają z istniejącego, sprawdzonego sekretu `TELEGRAM_TOKEN` w tym repozytorium.
Do automatycznego uruchamiania nie jest potrzebny zewnętrzny token GitHub z cron-job.org.
Poprzednie dwa zadania konkursowe w cron-job.org zostały wyłączone po migracji.

## Pliki konkursów

Konkurs miesięczny używa skryptu `weekly_contest2.py` i grafiki z tego repozytorium.
Konkurs tygodniowy pobiera skrypt `weekly_contest.py`, grafikę oraz zależności z gałęzi `main`
repozytorium [Level-In-level-invest-telegram-bot-4](https://github.com/Level-In/Level-In-level-invest-telegram-bot-4).
Harmonogram tygodniowy jest wyłącznie tutaj; repozytorium bot-4 pozostaje źródłem plików.

## Test i ręczna wysyłka

W Actions → wybrany konkurs → Run workflow opcja `dry_run` jest domyślnie zaznaczona.
Sprawdza grafikę, token Telegram oraz członkostwo i uprawnienia w pięciu grupach bez wysyłania wiadomości.
Odznacz `dry_run` wyłącznie wtedy, gdy chcesz natychmiast wysłać konkurs do wszystkich grup.
Zmiana pliku workflow uruchamia ten sam test automatycznie. Zmiana lokalnych plików konkursu miesięcznego również uruchamia jego test.
Zaplanowany przebieg przechodzi sprawdzenie, a następnie wysyła grafikę i tekst.

## Ograniczenia GitHub

GitHub może opóźnić lub pominąć uruchomienie przy dużym obciążeniu.
W publicznym repozytorium harmonogram jest automatycznie wyłączany po 60 dniach bez aktywności w repozytorium.
Dokumentacja: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule
