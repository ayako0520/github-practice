# 自由に書き換えてPRを出す練習用のファイルです。
# メッセージを変えたり、挨拶を増やしたりしてみましょう。

def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to github-practice."


if __name__ == "__main__":
    print(greet("world"))
