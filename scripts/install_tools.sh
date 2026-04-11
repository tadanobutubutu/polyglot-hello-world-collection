#!/bin/bash
BREW="/opt/homebrew/bin/brew"

echo "Checking and installing missing compilers/interpreters..."

# Mainstream & Others via Brew
$BREW install gnucobol gcc fpc ghc swi-prolog zig nim julia elixir crystal clojure ocaml erlang lua perl dart-sdk

# Node.js/TypeScript
$BREW install node
npm install -g typescript ts-node

# Japanese Languages (Nadeshiko is usually npm or specialized, Prodel is Windows mostly but let's see)
npm install -g nadesiko3

echo "Installation complete."
