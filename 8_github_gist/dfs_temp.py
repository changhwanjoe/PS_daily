def findCircleNum(A):
    count = 0
    visited = set()

    def dfs(student):
        if student in visited:
            return

        visited.add(student)
        for i, friend in enumerate(A[student]):
            if friend:
                dfs(i)

    for student in range(len(A)):
        # Note we want to track circles, student without any friend won't count
        if student not in visited and any(A[student]):
            dfs(student)
            count += 1

    return count