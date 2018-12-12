package main

import (
	"fmt"
	"math"
)

func hasPlant(curr map[int64]bool, m map[string]string, i int64) bool {
	s := ""
	if _, ok := curr[i-2]; ok {
		s += "#"
	} else {
		s += "."
	}
	if _, ok := curr[i-1]; ok {
		s += "#"
	} else {
		s += "."
	}
	if _, ok := curr[i]; ok {
		s += "#"
	} else {
		s += "."
	}
	if _, ok := curr[i+1]; ok {
		s += "#"
	} else {
		s += "."
	}
	if _, ok := curr[i+2]; ok {
		s += "#"
	} else {
		s += "."
	}
	//fmt.Println(s)
	val, _ := m[s]
	return val == "#"
}

func getNext(curr map[int64]bool, m map[string]string) map[int64]bool {
	res := map[int64]bool{}
	min := int64(math.MaxInt64)
	max := int64(0)
	var k int64
	for k = range curr {
		if k > max {
			max = k
		}
		if k < min {
			min = k
		}
	}
	start := int64(min - 4)
	end := int64(max + 4)
	for i := int64(start); i <= end; i++ {
		if hasPlant(curr, m, i) {
			res[i] = true
		}
	}
	return res
}

func main() {
	state := "..#..####.##.####...#....#######..#.#..#..#.#.#####.######..#.#.#.#..##.###.#....####.#.#....#.#####"
	m := map[string]string{
		"#.##.": ".",
		"#.#..": ".",
		"###.#": ".",
		"..#.#": ".",
		"....#": ".",
		".####": ".",
		"##.##": "#",
		"###..": "#",
		".###.": "#",
		"...#.": ".",
		".....": ".",
		"##..#": ".",
		".#.#.": "#",
		".#.##": "#",
		"##.#.": ".",
		"##...": ".",
		"#####": "#",
		"#...#": ".",
		"..##.": ".",
		"..###": ".",
		".#...": "#",
		".##.#": ".",
		"#....": ".",
		".#..#": ".",
		".##..": "#",
		"...##": "#",
		"#.###": ".",
		"#..#.": ".",
		"..#..": "#",
		"#.#.#": "#",
		"####.": "#",
		"#..##": ".",
	}

	curr := map[int64]bool{}
	for pos, char := range state {
		if char == '#' {
			curr[int64(pos)] = true
		}
	}
	//for i := 0; i < 20; i++ {
	for i := 0; i < 50000000000; i++ {
		//fmt.Println(curr)
		curr = getNext(curr, m)
	}

	s := int64(0)
	for k := range curr {
		s += k
	}
	fmt.Println(s)
}
