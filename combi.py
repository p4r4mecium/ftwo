package main

import (
	"github.com/01-edu/z01" // Importing the z01 package for character output
)

// comb generates all possible combinations of digits of length n without repetition
func comb(n int) {
	var recur func(digit int)

	// Keeps track of used digits
	used := make([]bool, 10)

	// Stores the digits of the current combination
	number := make([]int, n)

	// recur is a recursive function to generate combinations
	recur = func(digit int) {
		if digit == n {
			// If a combination of length n is formed, print it
			for x := 0; x < n; x++ {
				// Convert each digit to a character and print it
				z01.PrintRune(rune('0' + number[x]))
			}
			// Print a newline to separate each combination
			z01.PrintRune('\n')
			return
		}
		// Try all possible digits at the current position
		for i := 0; i < 10; i++ {
			if !used[i] {
				// If digit i is not used yet, use it in the combination
				number[digit] = i
				used[i] = true
				// Recur to the next position
				recur(digit + 1)
				// Backtrack: Reset the used flag for digit i
				used[i] = false
			}
		}
	}

	// Start the recursive function from position 0
	recur(0)
}

func main() {
	// Generate and print combinations of length 3
	comb(3)
}