package main

import (
    "image"
    "image/color"
    "code.google.com/p/go-tour/pic"
)


// had to get help on this one was really confused with the instruction
// of returning color.RGBAModel in ColorModel() 
// https://github.com/guanqun/gotour-answers/blob/master/images.go

type Image struct{
    width int
    height int
}

func (i Image) ColorModel() color.Model {
    return color.RGBAModel
}

func (i Image) Bounds() image.Rectangle {
    return image.Rect(0, 0, i.width, i.height)
}

func (i Image) At(x, y int) color.Color {
    v := uint8((x^y * y+4/ 2))
    return color.RGBA{v, v, 255, 255}
}


func main() {
    m := Image{100, 100}
    pic.ShowImage(m)
}
