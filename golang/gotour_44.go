package main

/* Implelement Pic.

It should return a slice of length dy, each element of which is
a slice of dx 8-bit unsigned integers. When you run the program,
it will display your picture, interpreting the integers as grayscale
(well, bluescale) values.

The choice of image is up to you. Interesting functions
include x^y, (x+y)/2, and x*y.

(You need to use a loop to allocate each []uint8 inside the [][]uint8.)

(Use uint8(intValue) to convert between types.)*/

import (
    /*"code.google.com/p/go-tour/pic"*/
    "fmt"
)

func Pic(dx, dy int) [][]uint8 {
    s := make([][]uint8, dy)

    for y := 0; y <=dy; y++ {
        s[y] = uint8(10)
        for x := 0; x <=dx; x++ {
            s[y] = uint8(10)
        }
    }
    return s
}


func main() {
    /*pic.Show(Pic)*/
    fmt.Println(Pic(3,5))
}
