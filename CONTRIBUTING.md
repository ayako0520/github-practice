# 参加ガイド（CONTRIBUTING）

このリポジトリでプルリクエスト（PR）を出す・マージするまでの手順です。GitHubに慣れていない人向けに、できるだけ細かく書いています。

## 1. Fork するか、直接ブランチを切るか

- **Forkする場合**（自分のアカウントにコピーを作って作業する、一般的なOSSの流れ）
  1. このページ右上の「Fork」ボタンを押す
  2. 自分のアカウントにコピーされたリポジトリをクローンする
     ```
     git clone https://github.com/<あなたのアカウント>/github-practice.git
     ```
- **Collaboratorとして直接ブランチを切る場合**（Write権限がある人向け）
  ```
  git clone https://github.com/ayako0520/github-practice.git
  cd github-practice
  git checkout -b your-name/fix-typo
  ```

## 2. 変更する

何でもOKです。迷ったら以下から選んでください。

- `docs/glossary.md` の誤字・説明不足を直す
- `docs/self-introduction.md` に自己紹介を1段落追加する
- `examples/hello.js` や `examples/hello.py` の出力メッセージを変えてみる
- READMEやこのファイルの説明をわかりやすく直す

## 3. コミットしてpush

```
git add .
git commit -m "用語集のtypoを修正"
git push origin your-name/fix-typo
```

（Forkした場合は `git push origin your-name/fix-typo` で自分のFork先にpushされます）

## 4. プルリクエストを作成する

1. GitHub上でリポジトリを開くと「Compare & pull request」ボタンが出るので押す
2. タイトルと説明を書く（何を直したか一言でOK）
3. base repository が `ayako0520/github-practice` の `main` になっていることを確認して作成

## 5. レビュー・マージ

- 他の参加者のPRを見て、コメントを付けてみましょう（褒めるだけでもOK）
- 自分のPRを自分でマージする練習も歓迎です。「Merge pull request」ボタンを押すだけです
- コンフリクト（衝突）が起きたら、慌てず質問Issueを立ててください

## よくある質問

**Q. 間違えてmainに直接pushしてしまった**
A. このリポジトリは練習用なので気にしなくてOKです。気になる場合はIssueで相談してください。

**Q. PRがコンフリクトすると出た**
A. 先に他の人のPRがマージされて、同じ場所を直そうとした時によく起きます。自分のブランチで `git pull origin main` してから解消してみましょう。
