# ① 部品を読み込む（2行）：load_dotenv と OpenAI
from openai import OpenAI
from dotenv import load_dotenv
# ② .env を読み込む（1行）
load_dotenv()
# ③ OpenAIと話す窓口（クライアント）を作り、変数に入れる（1行）
client = OpenAI()
# ④ 窓口に問い合わせを送り、結果を変数に入れる（数行）
#    → client.responses.create に model= と input= を渡す
response = client.responses.create(
    model="gpt-5.4-nano",
    input="先週注文したシャツがまだ届きません。いつ届きますか？"
)
# ⑤ 結果から返事の文章を取り出して表示する（1行）
print(response.output_text)
