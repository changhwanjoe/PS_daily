# 📘 PS_daily — 알고리즘 문제 풀이 저장소

> 매일 꾸준히 알고리즘 문제를 풀고 기록하는 개인 학습 레포지토리입니다.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C++-17-00599C?logo=cplusplus&logoColor=white)](https://isocpp.org/)
[![C](https://img.shields.io/badge/C-99-A8B9CC?logo=c&logoColor=white)](https://en.wikipedia.org/wiki/C99)
[![Java](https://img.shields.io/badge/Java-11-ED8B00?logo=openjdk&logoColor=white)](https://openjdk.org/)

---

## 📌 프로젝트 소개

이 레포지토리는 다양한 온라인 저지와 코딩 테스트 플랫폼의 문제 풀이를 모아둔 곳입니다.  
알고리즘 유형별 학습, 기업 코딩테스트 대비, 그리고 자료구조 템플릿 관리를 목적으로 합니다.

### 🛠 기술 스택

| 언어 | 용도 |
|------|------|
| **Python** | 주력 언어. 프로그래머스, LeetCode, BOJ, 코딩테스트 풀이 |
| **C/C++** | SWEA, BOJ, 기업 코딩테스트 풀이 |
| **Java** | SWEA 일부 문제 풀이 |

### 📚 주요 학습 자료

- *이것이 코딩테스트다* (나동빈 저)
- *파이썬 알고리즘 인터뷰* (박상길 저)

---

## 📂 디렉토리 구조

```
PS_daily/
│
├── Baekjoon/               # 백준 온라인 저지 (20문제)
│   ├── boj_11729_hanoey.py        # 하노이 탑 - 재귀
│   ├── boj_14500_테트로미노.py      # 삼성 기출 - 브루트포스
│   ├── boj_17070.cpp              # 파이프 옮기기 - DP
│   └── ...
│
├── Programmers/             # 프로그래머스 (21문제)
│   ├── 0124_prg_완주하지못한선수.py  # 해시
│   ├── 0218_prg_더맵게.py          # 힙
│   ├── 0219_prg_N으로표현.py       # DP
│   └── ...
│
├── LeetCode/                # 릿코드 (6문제)
│   ├── leet_200_NumberOfIslands.py  # DFS
│   ├── leet_743_NetworkDelayTime.py # Dijkstra
│   └── ...
│
├── CodeWars/                # 코드워즈 (6문제)
│   ├── cwars_5kyu_SimplePigLatin.py
│   └── ...
│
├── SWEA/                    # SW Expert Academy (39문제)
│   ├── (D1~D4) 난이도별 문제
│   └── C / C++ / Java / Python
│
├── CodingTest/              # 기업 코딩테스트 기출
│   ├── Samsung/                    # 삼성 SW 역량테스트 (42문제)
│   │   ├── 16236_아기상어.py
│   │   ├── 19237_AdultShark.py
│   │   ├── 23291_fishbowl.py
│   │   └── ...
│   ├── Kakao/                      # 카카오 블라인드 채용 (21문제)
│   ├── Naver/                      # 네이버 (7문제)
│   ├── Hynix/                      # SK하이닉스 (15문제)
│   └── etc/                        # 기타 기업
│
├── Templates/               # 🧩 알고리즘 템플릿 & 레퍼런스
│   ├── graph/                      # 그래프 알고리즘
│   │   ├── bfs_reference.py        # BFS/DFS 다양한 구현
│   │   ├── dijkstra.py             # 다익스트라 최단경로
│   │   ├── bellman_ford.py         # 벨만-포드
│   │   ├── floyd_warshall.py       # 플로이드-워셜
│   │   ├── kruskal.py              # 크루스칼 MST
│   │   ├── topological_sort.py     # 위상 정렬
│   │   ├── scc.py                  # 강한 연결 요소
│   │   ├── network_flow.py         # 네트워크 플로우
│   │   └── bipartite_match.py      # 이분 매칭
│   ├── tree/                       # 트리 자료구조
│   │   ├── segment_tree.py         # 세그먼트 트리 (Lazy Propagation)
│   │   ├── binary_search_tree.py   # 이진 탐색 트리
│   │   ├── union_find.py           # Union-Find (분리 집합)
│   │   └── lca.py                  # 최소 공통 조상
│   ├── string/                     # 문자열 알고리즘
│   │   └── kmp.py                  # KMP 매칭
│   ├── dp/                         # 동적 프로그래밍
│   │   └── lis.py                  # 최장 증가 부분 수열
│   ├── math/                       # 수학
│   │   ├── number.py               # 소수, 약수 등
│   │   └── vector.py               # 벡터 연산
│   └── etc/                        # 기타
│       ├── matrix_rotation.py      # 행렬 회전/전치
│       ├── permutation.py          # 순열/조합
│       └── histogram.py            # 히스토그램
│
├── BookStudy/               # 📖 교재 학습 코드
│   ├── 1로만들기.py                 # DP - 이코테
│   ├── 아기상어.py                   # BFS + 시뮬레이션
│   ├── 음료수얼려먹기.py              # DFS/BFS - 이코테
│   ├── 전보.py                      # Dijkstra - 이코테
│   └── ...
│
└── Practice/                # 🔧 연습 & 실습
    ├── algorithm_concepts/         # 알고리즘 개념 구현
    │   ├── DFS_BFS.py
    │   ├── dijkstra.py
    │   ├── dynamic_programming.py
    │   ├── Knapsack problem.py
    │   └── ...
    └── cpp_basics/                 # C++ 프로그래밍 기초
        ├── Ex01_HelloWorld/
        ├── Ex08_Pointer/
        └── ...
```

---

## 📊 문제 풀이 현황

### 플랫폼별 현황

| 플랫폼 | 풀이 수 | 주요 언어 | 비고 |
|--------|---------|----------|------|
| 백준 (BOJ) | 20 | Python, C++ | 구간합, 하노이탑, 테트로미노, DP |
| 프로그래머스 | 21 | Python, C++ | 해시, 힙, 그리디, DP, BFS |
| LeetCode | 6 | Python | DFS, Dijkstra, 조합, 순열 |
| SWEA | 39 | C, C++, Java, Python | D1~D4 난이도 |
| CodeWars | 6 | Python | 5kyu~7kyu |
| 삼성 기출 | 42 | Python | 구현, 시뮬레이션 |
| 카카오 기출 | 21 | Python | 2021 BLIND 등 |
| **총합** | **~155+** | | |

### 알고리즘 유형별 분류

| 유형 | 관련 문제 | 위치 |
|------|----------|------|
| **그래프 탐색 (BFS/DFS)** | 섬의 개수, 음료수 얼려먹기, 미로탈출, 게임맵 | `Programmers/`, `BookStudy/` |
| **최단 경로 (Dijkstra)** | Network Delay Time, 전보, 보급로 | `LeetCode/`, `SWEA/` |
| **동적 프로그래밍 (DP)** | N으로 표현, 1로 만들기, 바닥공사 | `Programmers/`, `BookStudy/` |
| **그리디 (Greedy)** | 큰 수 만들기, 체육복 | `Programmers/` |
| **힙 (Heap)** | 더 맵게 | `Programmers/` |
| **해시 (Hash)** | 완주하지 못한 선수, 베스트앨범 | `Programmers/`, `CodingTest/Hynix/` |
| **시뮬레이션** | 아기상어, 어른상어, 원판돌리기, 마법사상어 | `CodingTest/Samsung/` |
| **백트래킹** | 테트로미노, Combination Sum | `Baekjoon/`, `LeetCode/` |
| **문자열** | 옹알이, Simple Pig Latin, KMP | `Programmers/`, `Templates/string/` |
| **트리/자료구조** | 세그먼트 트리, BST, 펜윅 트리 | `Templates/tree/` |

---

## 🧩 알고리즘 템플릿 목록

`Templates/` 디렉토리에 자주 사용되는 알고리즘 템플릿을 관리합니다.

| 알고리즘 | 파일 | 시간 복잡도 |
|---------|------|-----------|
| BFS / DFS | `graph/bfs_reference.py` | O(V + E) |
| 다익스트라 | `graph/dijkstra.py` | O(E log V) |
| 벨만-포드 | `graph/bellman_ford.py` | O(VE) |
| 플로이드-워셜 | `graph/floyd_warshall.py` | O(V³) |
| 위상 정렬 | `graph/topological_sort.py` | O(V + E) |
| 크루스칼 MST | `graph/kruskal.py` | O(E log E) |
| SCC | `graph/scc.py` | O(V + E) |
| 이분 매칭 | `graph/bipartite_match.py` | O(VE) |
| 네트워크 플로우 | `graph/network_flow.py` | O(V²E) |
| 세그먼트 트리 | `tree/segment_tree.py` | O(log N) per query |
| 이진 탐색 트리 | `tree/binary_search_tree.py` | O(log N) avg |
| Union-Find | `tree/union_find.py` | O(α(N)) ≈ O(1) |
| LCA | `tree/lca.py` | O(log N) per query |
| KMP | `string/kmp.py` | O(N + M) |
| LIS | `dp/lis.py` | O(N log N) |

---

## 🏷 파일명 규칙

| 출처 | 형식 | 예시 |
|------|------|------|
| 백준 | `boj_{번호}_{제목}.py` | `boj_14500_테트로미노.py` |
| 프로그래머스 | `{날짜}_prg_{제목}.py` | `0218_prg_더맵게.py` |
| LeetCode | `leet_{번호}_{제목}.py` | `leet_200_NumberOfIslands.py` |
| SWEA | `({난이도})_{번호}_{제목}.{ext}` | `(D3)_1206_Flatten.cpp` |
| CodeWars | `cwars_{난이도}kyu_{제목}.py` | `cwars_5kyu_SimplePigLatin.py` |

---

## 🚀 실행 방법

```bash
# Python 풀이 실행
python3 Programmers/0218_prg_더맵게.py

# C++ 풀이 컴파일 및 실행
g++ -std=c++17 -o sol Baekjoon/boj_17070.cpp && ./sol
```

---

## 📝 학습 노트

### 자주 사용하는 Python 입출력 최적화

```python
import sys
input = sys.stdin.readline  # 빠른 입력

# 2차원 배열 입력
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
```

### BFS 템플릿

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True
```

### Dijkstra 템플릿

```python
import heapq

def dijkstra(graph, start, distance):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
```

---

## 📄 License

이 레포지토리는 개인 학습 목적으로 운영됩니다.