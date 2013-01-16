package main

import (
        "fmt"
        "math"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
    return fmt.Sprintf("cannot Sqrt negative number: %v", float64(e))
}


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

func Sqrt(x float64) (float64, error) {
    if x < 0 {
        return 0, ErrNegativeSqrt(x)
    }

    guess := float64(1)
    for i := 0; i < 10; i++ {
        guess = Improve(float64(guess), x)

    }
    return guess, nil
}

func main() {
    fmt.Println(Sqrt(2))
    fmt.Println(math.Sqrt(2))
    fmt.Println(Sqrt(-2))
}
