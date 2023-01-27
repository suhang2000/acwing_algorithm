package main

import (
	"bufio"
	"fmt"
	"os"
)

type node struct {
	y, z int
}

var (
	n, m int
	g    [][]node
)

func spfa() (res int) {
	dq := make([]int, 0)
	dist := make([]int, n+1)
	state := make([]bool, n+1)
	dq = append(dq, 1)
	dist[1] = 0
	for i := 2; i <= n; i++ {
		dist[i] = 0x3f3f3f3f
	}
	state[1] = true

	for len(dq) > 0 {
		x := dq[0]
		dq = dq[1:]
		state[x] = false
		for _, nd := range g[x] {
			y, z := nd.y, nd.z
			if dist[y] > dist[x]+z {
				dist[y] = dist[x] + z
				if !state[y] {
					state[y] = true
					dq = append(dq, y)
				}
			}
		}
	}

	return dist[n]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n, &m)
	g = make([][]node, n+1)
	//for i := 0; i < n; i++ {
	//	g[i] = make([]node, 0)
	//}
	for i := 0; i < m; i++ {
		var x, y, z int
		fmt.Fscan(in, &x, &y, &z)
		g[x] = append(g[x], node{y, z})
	}

	res := spfa()
	if res == 0x3f3f3f3f {
		fmt.Println("impossible")
	} else {
		fmt.Println(res)
	}
}
