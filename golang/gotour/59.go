package main

import (
    "io"
    "os"
    "strings"
)

type rot13Reader struct {
    r io.Reader
}

func (rot *rot13Reader) Read(p []byte) (n int, err error) {
    rn, err := rot.r.Read(p)

    if err != nil {
        return rn, err
    }

    // loop over each char that is read
    for i := 0; i < rn; i++ {
        switch {
            case p[i] >= 'A' && p[i] <= 'Z':
                p[i] = 'A' + (p[i]-'A'+13)%26
            case p[i] >= 'a' && p[i] <= 'z':
                p[i] = 'a' + (p[i]-'a'+13)%26
            }
        }

    return rn, err
}


func main() {
    s := strings.NewReader("Lbh penpxrq gur pbqr!\n")
    r := rot13Reader{s}

    /*The following two line
    buf := make([]byte, 5)
    /*t.Read(buf)
    fmt.Println(buf)*/
    io.Copy(os.Stdout, &r)
}
