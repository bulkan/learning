package main

import (
    "code.google.com/p/go-tour/wc"
    "strings"
)

func WordCount(s string) map[string]int {
    wordcount := make(map[string]int)
    for _, word := range strings.Fields(s) {
        wordcount[word] += 1
   }
   return wordcount
}

func main() {
    wc.Test(WordCount)
}

