package main

import (
    "fmt"
    "strings"
)

func main() {

    // String s is split on the basis of white spaces
    // and store in a string array
    s := "GeeksforGeeks is a computer science portal !"
    v := strings.Fields(s)
    fmt.Println(v)

    // Another example by passing the string as argument
    // directly to the Fields() function
    // v = strings.Fields("I am a software developer, I love coding")
}
