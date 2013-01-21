package main

import (
    "code.google.com/p/go-tour/tree"
    "fmt"
)


// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *tree.Tree, ch chan int) {
    if t.Left != nil {
        Walk(t.Left, ch)
    }

    ch <- t.Value
    if t.Right != nil {
        Walk(t.Right, ch)
    }


}

// Same determines whether the trees
// t1 and t2 contain the same values.
/*func Same(t1, t2 *tree.Tree) bool*/

func main() {
    ch := make(chan int)
    t := tree.New(1)
    fmt.Println(t.String())
    go Walk(t, ch)
    for i := 1; i <= 10; i++  {
        fmt.Println(<-ch)
    }
}
