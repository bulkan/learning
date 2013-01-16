package main

import (
    "image"
    "code.google.com/p/go-tour/pic"
)


type Image struct{}

func Pic(dx, dy int) [][]uint8 {
    s := make([][]uint8, dy)

    for y := 0; y < dy; y++ {
        s[y] = make([]uint8, dx)
        for x := 0; x < dx ; x++ {
            s[y][x] = uint8(y^x * y+4/2 )
        }
    }
    return s
}

func main() {
    m := Image{}
    pic.ShowImage(m)
}
