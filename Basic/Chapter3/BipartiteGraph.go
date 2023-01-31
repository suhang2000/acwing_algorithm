package main

import "fmt"

var (
	graph [][]int
	color []int
)

func main() {
	var n, m int
	_, _ = fmt.Scan(&n, &m)
	graph = make([][]int, n+1)
	for i := 0; i < m; i++ {
		var u, v int
		_, _ = fmt.Scan(&u, &v)
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	color = make([]int, n+1)

	flag := true
	for i := 1; i <= n; i++ {
		if color[i] == 0 {
			if !dfs(i, 1) {
				flag = false
				break
			}
		}
	}
	if flag {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}

func dfs(x, c int) bool {
	if color[x] != 0 {
		return color[x] == c
	}
	color[x] = c
	for _, v := range graph[x] {
		if !dfs(v, 3-c) {
			return false
		}
	}
	return true
}
