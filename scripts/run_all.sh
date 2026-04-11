#!/bin/bash

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting Polyglot Hello World Execution Test...${NC}\n"

function run_test() {
    local lang_name=$1
    local cmd=$2
    local file_path=$3

    echo -n "Running $lang_name... "
    if command -v $(echo $cmd | awk '{print $1}') >/dev/null 2>&1; then
        output=$(eval "$cmd $file_path" 2>&1)
        if [[ $output == *"Hello, World!"* ]]; then
            echo -e "${GREEN}SUCCESS${NC}"
        else
            echo -e "${RED}FAILED${NC} (Unexpected output)"
            echo "  Output: $output"
        fi
    else
        echo -e "${YELLOW}SKIPPED${NC} (Command not found)"
    fi
}

# --- Popular ---
run_test "Python" "python3" "langs/popular/python/hello.py"
run_test "JavaScript (Node)" "node" "langs/popular/javascript/hello.js"
run_test "Ruby" "ruby" "langs/popular/ruby/hello.rb"
run_test "Go" "go run" "langs/popular/go/hello.go"
run_test "Rust" "rustc -o hello_rust && ./hello_rust && rm hello_rust" "langs/popular/rust/hello.rs"
run_test "PHP" "php" "langs/popular/php/hello.php"

# --- Functional ---
run_test "Haskell" "runghc" "langs/functional/haskell/hello.hs"
run_test "Lisp (Scheme)" "gosh" "langs/functional/scheme/hello.scm"

# --- Japanese ---
run_test "Nadeshiko" "nako3" "langs/japanese/nadeshiko/hello.nako3"

# --- Esoteric ---
# (Needs interpreters, usually custom)
run_test "Brainfuck" "bf" "langs/esoteric/brainfuck/hello.bf"

# --- Domain ---
run_test "Shell" "bash" "langs/domain/shell/hello.sh"

echo -e "\n${YELLOW}Done.${NC}"
