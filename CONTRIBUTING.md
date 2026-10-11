# 参加ガイド（CONTRIBUTING）

このリポジトリでプルリクエスト（PR）を出す・マージするまでの手順です。GitHubに慣れていない人向けに、できるだけ細かく書いています。
全体の流れは [ROADMAP.md](./ROADMAP.md)、クリック単位の図解は [docs/guide.html](./docs/guide.html) も参照してください。

## 0. Write権限を1回だけリクエストする

**自分のPRを自分でマージしたい人だけ**、最初に1回これをやってください（見るだけ・Forkして試すだけなら不要です）。

1. [Issues タブ](https://github.com/ayako0520/github-practice/issues/new/choose) を開く
2. 「アクセス申請（Collaborator登録）」テンプレートを選ぶ
3. 自分のGitHubユーザー名を書いて送信する
4. 運営から Collaborator 招待が届くので、メールまたはGitHubの通知から「Accept invitation」を押す

これで「Merge pull request」ボタンが使えるようになります。申請前にPRを出すところまでは誰でもできるので、先に2〜4章を進めてしまって構いません。

## 1. Fork するか、直接ブランチを切るか

- **Forkする場合**（自分のアカウントにコピーを作って作業する、一般的なOSSの流れ。Write権限がなくてもできます）
  1. このページ右上の「Fork」ボタンを押す
  2. 自分のアカウントにコピーされたリポジトリをクローンする
     ```
     git clone https://github.com/<あなたのアカウント>/github-practice.git
     ```
- **Collaboratorとして直接ブランチを切る場合**（0章でWrite権限をもらった人向け）
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
- `TEXTBOOK.md` の説明が分かりにくいところを直す

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
  - ボタンが見えない・押せない場合は、0章のアクセス申請がまだの可能性があります
- コンフリクト（衝突）が起きたら、慌てず質問Issueを立てるか、[TEXTBOOK.md](./TEXTBOOK.md) の第7章を見てください

## よくある質問

**Q. 間違えてmainに直接pushしてしまった**
A. このリポジトリは練習用なので気にしなくてOKです。気になる場合はIssueで相談してください。

**Q. PRがコンフリクトすると出た**
A. 先に他の人のPRがマージされて、同じ場所を直そうとした時によく起きます。自分のブランチで `git pull origin main` してから解消してみましょう。

**Q. 「Merge pull request」ボタンが出ない・押せない**
A. Write権限（Collaborator）がまだ付与されていません。0章の手順でアクセス申請を出してください。
