#!/bin/bash
set -e

echo "=== PS_daily 디렉토리 구조 개편 시작 ==="

# -----------------------------------------------
# 1. 새 디렉토리 구조 생성
# -----------------------------------------------
echo "[1/8] 새 디렉토리 생성..."
mkdir -p Baekjoon
mkdir -p Programmers
mkdir -p LeetCode
mkdir -p CodeWars
mkdir -p SWEA
mkdir -p CodingTest/Samsung
mkdir -p CodingTest/Kakao
mkdir -p CodingTest/Naver
mkdir -p CodingTest/Hynix
mkdir -p CodingTest/etc
mkdir -p Templates/graph
mkdir -p Templates/tree
mkdir -p Templates/string
mkdir -p Templates/dp
mkdir -p Templates/math
mkdir -p Templates/etc
mkdir -p BookStudy
mkdir -p Practice/algorithm_concepts
mkdir -p Practice/cpp_basics

# -----------------------------------------------
# 2. BOJ/ → Baekjoon/
# -----------------------------------------------
echo "[2/8] BOJ → Baekjoon 이동..."
for f in BOJ/*; do
  [ -f "$f" ] && git mv "$f" Baekjoon/
done

# -----------------------------------------------
# 3. 1_Problems/ → Programmers, LeetCode, CodeWars 분류
# -----------------------------------------------
echo "[3/8] 1_Problems 분류 이동..."

# Programmers (prg_ 파일)
for f in 1_Problems/*prg_*; do
  [ -f "$f" ] && git mv "$f" Programmers/
done

# LeetCode (leet_ 파일)
for f in 1_Problems/leet_*; do
  [ -f "$f" ] && git mv "$f" LeetCode/
done

# CodeWars (cwars_ 파일)
for f in 1_Problems/cwars_*; do
  [ -f "$f" ] && git mv "$f" CodeWars/
done

# Book study (book_ 파일)
for f in 1_Problems/*book_*; do
  [ -f "$f" ] && git mv "$f" BookStudy/
done

# C++ 파일들 → Programmers (게임맵, 미로탈출 등)
[ -f "1_Problems/1844_게임맵.cpp" ] && git mv "1_Problems/1844_게임맵.cpp" Programmers/
[ -f "1_Problems/15993_미로탈출.cpp" ] && git mv "1_Problems/15993_미로탈출.cpp" Programmers/
[ -f "1_Problems/large_number.cpp" ] && git mv "1_Problems/large_number.cpp" Programmers/

# 나머지 → Practice
for f in 1_Problems/*; do
  [ -f "$f" ] && git mv "$f" Practice/algorithm_concepts/
done

# 1_Problems 디렉토리 삭제
[ -d "1_Problems" ] && rmdir 1_Problems 2>/dev/null || true

# -----------------------------------------------
# 4. SWexpert/ → SWEA/
# -----------------------------------------------
echo "[4/8] SWexpert → SWEA 이동..."
for f in SWexpert/*; do
  [ -f "$f" ] && git mv "$f" SWEA/
done
[ -d "SWexpert" ] && rmdir SWexpert 2>/dev/null || true

# -----------------------------------------------
# 5. Tests/ → CodingTest/
# -----------------------------------------------
echo "[5/8] Tests → CodingTest 이동..."

# Samsung
for f in Tests/samsung/*; do
  [ -f "$f" ] && git mv "$f" CodingTest/Samsung/
done

# Kakao
for f in Tests/kakao/*; do
  [ -f "$f" ] && git mv "$f" CodingTest/Kakao/
done

# Naver
for f in Tests/Naver/*; do
  [ -f "$f" ] && git mv "$f" CodingTest/Naver/
done

# Hynix
for f in Tests/hynix/*; do
  [ -f "$f" ] && git mv "$f" CodingTest/Hynix/
done

# com → etc
for f in Tests/com/*; do
  [ -f "$f" ] && git mv "$f" CodingTest/etc/
done
# .DS_Store 등 비추적 파일 정리
find Tests -name ".DS_Store" -delete 2>/dev/null || true
rm -rf Tests 2>/dev/null || true

# -----------------------------------------------
# 6. imhyo_repo/ → Templates/ (유형별 분류)
# -----------------------------------------------
echo "[6/8] imhyo_repo → Templates 이동..."

# Graph
for name in bellman_ford dfs dijkstra floyd_warshall graph topological_sort kruskal scc network_flow bipartite_match; do
  [ -f "imhyo_repo/${name}.py" ] && git mv "imhyo_repo/${name}.py" Templates/graph/
done

# Tree
for name in binary_search_tree segment_tree lca union_find; do
  [ -f "imhyo_repo/${name}.py" ] && git mv "imhyo_repo/${name}.py" Templates/tree/
done

# String
[ -f "imhyo_repo/kmp.py" ] && git mv "imhyo_repo/kmp.py" Templates/string/

# DP
[ -f "imhyo_repo/lis.py" ] && git mv "imhyo_repo/lis.py" Templates/dp/

# Math
for name in number vector; do
  [ -f "imhyo_repo/${name}.py" ] && git mv "imhyo_repo/${name}.py" Templates/math/
done

# etc
for name in permutation histogram utility; do
  [ -f "imhyo_repo/${name}.py" ] && git mv "imhyo_repo/${name}.py" Templates/etc/
done

[ -d "imhyo_repo" ] && rmdir imhyo_repo 2>/dev/null || true

# -----------------------------------------------
# 7. 루트 파일, python_algorithm_book, 8_github_gist, hong_lab, 2025 이동
# -----------------------------------------------
echo "[7/8] 나머지 파일 이동..."

# 루트 알고리즘 파일 → Templates
[ -f "bfs.py" ] && git mv "bfs.py" Templates/graph/bfs_reference.py
[ -f "dijkstar.py" ] && git mv "dijkstar.py" Templates/graph/dijkstra_practice.py
[ -f "transpose.py" ] && git mv "transpose.py" Templates/etc/matrix_rotation.py

# python_algorithm_book → BookStudy
for f in python_algorithm_book/*; do
  [ -f "$f" ] && git mv "$f" BookStudy/
done
[ -d "python_algorithm_book" ] && rmdir python_algorithm_book 2>/dev/null || true

# 8_github_gist → Practice/algorithm_concepts
# __pycache__ 먼저 삭제
rm -rf "8_github_gist/__pycache__" 2>/dev/null || true
find "8_github_gist" -name ".DS_Store" -delete 2>/dev/null || true
for f in 8_github_gist/*; do
  [ -f "$f" ] && git mv "$f" Practice/algorithm_concepts/
done
[ -d "8_github_gist" ] && rmdir 8_github_gist 2>/dev/null || true

# hong_lab → Practice/cpp_basics
# .vscode 제외
rm -rf "hong_lab/.vscode" 2>/dev/null || true
for d in hong_lab/Ex*; do
  [ -d "$d" ] && git mv "$d" Practice/cpp_basics/
done
[ -d "hong_lab" ] && rmdir hong_lab 2>/dev/null || true

# 2025 → Programmers & Practice
find "2025" -name ".DS_Store" -delete 2>/dev/null || true
rm -rf "2025/output" 2>/dev/null || true
[ -f "2025/0406_완주하지못한선수.cpp" ] && git mv "2025/0406_완주하지못한선수.cpp" Programmers/
[ -f "2025/0406체육복.cpp" ] && git mv "2025/0406체육복.cpp" Programmers/
for f in 2025/*; do
  [ -f "$f" ] && git mv "$f" Practice/algorithm_concepts/
done
[ -d "2025" ] && rmdir 2025 2>/dev/null || true

# Readme 폴더 → Templates/etc
for f in Readme/*; do
  [ -f "$f" ] && git mv "$f" Templates/etc/
done
[ -d "Readme" ] && rmdir Readme 2>/dev/null || true

# -----------------------------------------------
# 8. 정리
# -----------------------------------------------
echo "[8/8] 정리 중..."
find . -name ".DS_Store" -delete 2>/dev/null || true
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

echo ""
echo "=== 구조 개편 완료! ==="
echo ""
echo "새 구조:"
find . -maxdepth 2 -type d \
  ! -path './.git*' ! -path './.vscode*' ! -path '.' \
  | sort | sed 's/^/  /'
