import pandas as pd
import json
import os

_RAW_SEASON_STATS = "raw_season_stats"
_CLEAN_SEASON_STATS = "clean_season_stats"
_CLEAN_PROJECTED_STATS = "clean_projected_season_stats"
_SEASON_APPEARENCES = "season_appearences"
_RAW_PLAYER_GAME_LOGS = "raw_player_logs"
_LINEUPS = "lineups"

def write_csv(df, path):
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    df.to_csv(path + ".csv")

def write_json(d, path):
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    json.dump(d, open(path + ".json", "w"))

def try_read_json(path):
    try:
        if os.path.exists(path + ".json"):
            return json.load(open(path + ".json", "r"))
        return False
    except Exception as e:
        print(path)
        raise e

def read_raw_season_stats(year: int):
    return json.load(open(f"{year}/{_RAW_SEASON_STATS}.json", "r"))

def write_raw_season_stats(year: int, stats):
    write_json(stats, f"{year}/{_RAW_SEASON_STATS}")

def read_season_appearences(year):
    return pd.read_csv(f"{year}/{_SEASON_APPEARENCES}.csv", index_col=0)

def write_season_appearences(logs, year):
    write_csv(logs, f"{year}/{_SEASON_APPEARENCES}")

def write_raw_game_logs(logs, player, year):
    write_json(logs, f"{year}/{_RAW_PLAYER_GAME_LOGS}/{player}")

def try_read_raw_game_logs(player, year):
    return try_read_json(f"{year}/{_RAW_PLAYER_GAME_LOGS}/{player}")

def read_clean_season_stats(year: int):
    return pd.read_csv(f"{year}/{_CLEAN_SEASON_STATS}.csv", index_col=0)

def write_clean_season_stats(year: int, stats):
    write_csv(stats, f"{year}/{_CLEAN_SEASON_STATS}")

def read_clean_projected_season_stats(year: int):
    return pd.read_csv(f"{year}/{_CLEAN_PROJECTED_STATS}", index_col=0)

def write_clean_projected_season_stats(year: int, stats):
    write_csv(stats, f"{year}/{_CLEAN_PROJECTED_STATS}")

def write_lineups(lineups, year, week):
    write_csv(lineups, f"{year}/{_LINEUPS}/{week}")

def read_lineups(year, week):
    return pd.read_csv(f"{year}/{_LINEUPS}/{week}.csv", index_col=0)