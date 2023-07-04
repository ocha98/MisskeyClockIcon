# これは何？
Misskeyのアカウントのアイコンを時刻に応じて回転させるプログラム。

アナログ時計の短針の位置にアイコンを回転させます。

Azure Functionsのtimer triggerで１時間毎に実行しています。

# 使い方
環境変数`ACCESS_TOKEN`に発行したアクセストークンを設定してください。

imgフォルダに画像を置きます。７時から21時前まで、normal.pngを、21時から7字前までnight.pngを利用します。

画像はPNGを想定しています。

# その他
⚠️新しいアイコンに設定される時、古いアイコンは削除されます。⚠️

アイコンはミスキーのドライブにicon.pngとして保存されます。