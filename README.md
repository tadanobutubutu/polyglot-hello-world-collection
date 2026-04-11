# 🌍 Polyglot Hello World Collection

様々なプログラミング言語による「Hello World」プログラムの集大成です。
有名言語から、歴史的なレガシー言語、そして脳を刺激する難解なジョーク言語まで、カテゴリー別に整理されています。

> [!TIP]
> このリポジトリは、Antigravity AI によって自動構築されました。
> 各言語のランタイムがインストールされている環境であれば、`scripts/run_all.sh` で一斉に実行テストを行うことができます。

---

## 📂 カテゴリー別リスト

### 1. 有名言語 (Popular)
現代のソフトウェア開発で最も広く使われている言語たちです。

| 言語 | ファイルパス | コード（抜粋） |
| :--- | :--- | :--- |
| **Python** | `langs/popular/python/hello.py` | `print("Hello, World!")` |
| **JavaScript** | `langs/popular/javascript/hello.js` | `console.log("Hello, World!");` |
| **Rust** | `langs/popular/rust/hello.rs` | `fn main() { println!(...) }` |
| **Go** | `langs/popular/go/hello.go` | `fmt.Println("Hello, World!")` |
| **Java** | `langs/popular/java/HelloWorld.java` | `System.out.println(...)` |
| **C / C++** | `langs/popular/c/hello.c` / `.cpp` | `printf(...)` / `std::cout` |
| **Ruby / PHP** | `langs/popular/ruby/hello.rb` / `.php` | `puts` / `echo` |

### 2. レガシー・歴史的言語 (Legacy)
計算機の歴史を築いてきた、あるいはエンタープライズの現場で今なお現役の言語たちです。

| 言語 | ファイルパス | 特徴 |
| :--- | :--- | :--- |
| **COBOL** | `langs/legacy/cobol/hello.cbl` | 事務処理用の歴史ある言語 |
| **Fortran** | `langs/legacy/fortran/hello.f` | 科学技術計算の先駆者 |
| **BASIC** | `langs/legacy/basic/hello.bas` | 初心者向け言語の原点 |
| **Assembly** | `langs/legacy/asm/hello_mac.asm` | ハードウェアに最も近いコード |

### 3. ジョーク・難解言語 (Esoteric)
実用性ではなく、芸術性や極限の難易度を追求した言語たちです。

| 言語 | ファイルパス | 難易度 |
| :--- | :--- | :--- |
| **Brainfuck** | `langs/esoteric/brainfuck/hello.bf` | 8つの記号のみで構成 |
| **Malbolge** | `langs/esoteric/malbolge/hello.mal` | 地獄の名を冠する史上最難関 |
| **Whitespace** | `langs/esoteric/whitespace/hello.ws` | 空白とタブと改行のみ |
| **Lolcode** | `langs/esoteric/lolcode/hello.lol` | 猫のミームから生まれた言語 |
| **Antigravity**| `langs/esoteric/antigravity/hello.ag`| カスタム言語 |

### 4. 日本語プログラミング言語 (Japanese)
日本語の自然な語順や語彙で記述できる、日本生まれの言語たちです。

| 言語 | ファイルパス | コード例 |
| :--- | :--- | :--- |
| **なでしこ** | `langs/japanese/nadeshiko/hello.nako3` | `「Hello, World!」と表示。` |
| **プロデル** | `langs/japanese/prodel/hello.pdl` | `「Hello, World!」を表示する` |
| **ドリトル** | `langs/japanese/dolittle/hello.dtl` | `「Hello, World!」を作る。` |

### 5. 研究用・関数型 (Functional / Research)
数学的な美しさや、新しい計算モデルを追求する言語たちです。

| 言語 | ファイルパス | タイプ |
| :--- | :--- | :--- |
| **Haskell** | `langs/functional/haskell/hello.hs` | 純粋関数型 |
| **Lisp (Scheme)** | `langs/functional/scheme/hello.scm` | S式による柔軟な構文 |
| **Prolog** | `langs/functional/prolog/hello.pl` | 論理プログラミング |

---

## 🚀 実行方法

一部の言語は事前にコンパイラ/インタプリタのインストールが必要です。
macOS 環境であれば、以下のスクリプトで一括セットアップを試みることができます。

```bash
./scripts/install_tools.sh
```

実行テスト:
```bash
./scripts/run_all.sh
```

---

## 🛡️ License
MIT License. Created with ❤️ by Antigravity.
