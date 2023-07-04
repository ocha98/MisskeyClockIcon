import os
import datetime
from dotenv import load_dotenv
from misskey import Misskey
from MisskeyClockIcon.util import time_rotate_image

load_dotenv()
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]

def main():
    api = Misskey("misskey.io", i=ACCESS_TOKEN)

    # 現在のアバターidを取得
    avatar_id = api.i()["avatarId"]

    # 回転させたアイコンを作成
    tmp_save_path = f"/tmp/icon.png" # 一時保存場所

    timezone = datetime.timezone(datetime.timedelta(hours = 9))
    date = datetime.datetime.now(tz = timezone)
    fillcolor = (115, 174, 232)
    if 21 <= date.hour < 24 or 0 <= date.hour < 7:
        time_rotate_image("img/night.png", tmp_save_path, timezone, fillcolor = fillcolor)
    else:
        time_rotate_image("img/normal.png", tmp_save_path, timezone, fillcolor = fillcolor)

    try:
        # アイコンをアップロード
        with open(tmp_save_path, "rb") as f:
            resu = api.drive_files_create(f)
            new_avatar_id = resu["id"]
        
        # アイコンを設定
        api.i_update(avatar_id = new_avatar_id)

        # 古いアイコンを削除
        api.drive_files_delete(avatar_id)

    except:
        raise 

    finally:
        # 一時ファイルを削除
        os.remove(tmp_save_path)
