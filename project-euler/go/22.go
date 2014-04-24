package main

//Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

//For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

//What is the total of all the name scores in the file?

import (
    "fmt"
    "io/ioutil"
    "log"
    "strings"
    "sort"
)

func readNames(path string)([]string, error){
    fData, err := ioutil.ReadFile(path)
    if err != nil {
        return nil, err
    }

    lines := strings.Split(string(fData), ",")

    var names []string

    for _, n := range lines {
        names = append(names, strings.Trim(n, "\""))
    }

    return names, nil

}


func main(){
    fmt.Println("problem 22")

    names, err := readNames("names.txt")
    if err != nil {
        log.Fatalf("readNames: %s", err)
    }

    alphabet :=  map[string]int {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }

    sort.Strings(names)

    total := 0

    for i, name := range names {

        nameSum := 0

        // calculate the points for name
        for _, c := range name {
            nameSum += alphabet[strings.ToLower(string(c))]
        }

        nameSum *= (i + 1);

        total += nameSum

        //fmt.Println(i, name)
    }

    fmt.Println(total)
    
}
