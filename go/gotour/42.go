package main

import (
        "fmt"
        "math"
)

func Avg(a, b float64) float64 {
    return ((a + b) / 2.0)
}

func Improve(guess, x float64) float64 {
    return Avg(guess, (x / guess))
}

func good_enough(guess, x float64) bool {
    d := math.Abs((guess * guess) - x)
    return d < 0.001
}

func Sqrt(x float64) float64 {
    guess := float64(1)
    for i := 0; i < 10; i++ {
        guess = Improve(float64(guess), x)

    }
    return guess
}

func main() {
    fmt.Println(Sqrt(2))
    fmt.Println(math.Sqrt(2))
}
