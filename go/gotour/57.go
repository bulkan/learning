package main

import (
    "fmt"
    "net/http"
)

type String string

type Struct struct {
    Greeting string
    Punct    string
    Who      string
}


func (s String) ServeHTTP(
        w http.ResponseWriter,
        r *http.Request) {
    fmt.Fprint(w,  s)
}

func (s *Struct) str() string {
    return fmt.Sprintf("%v%v%v ", s.Greeting, s.Punct, s.Who)
}


func (s *Struct) ServeHTTP(
        w http.ResponseWriter,
        r *http.Request) {
    fmt.Fprint(w,  s.str())
}

func main() {
    // your http.Handle calls here
    http.Handle("/string", String("I'm a frayed knot."))
    http.Handle("/struct", &Struct{"Hello", ":", "Gophers!"})
    http.ListenAndServe("localhost:4000", nil)
}
