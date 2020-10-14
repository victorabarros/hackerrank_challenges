// https://www.hackerrank.com/challenges/contacts/problem
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

var (
	contacts  = []string{}
	results   = []int{}
	stdout, _ = os.Create(os.Getenv("OUTPUT_PATH"))
	writer    = bufio.NewWriterSize(stdout, 1024*1024)
	comands   = map[string](func(string)){
		// https://stackoverflow.com/questions/6769020/go-map-of-functions
		"add":  add,
		"find": find,
	}
)

func add(name string) {
	contacts = append(contacts, name)
}

func find(name string) {
	var n int
	for _, contact := range contacts {
		if strings.HasPrefix(contact, name) {
			n++
		}
	}
	fmt.Fprintf(writer, "%d\n", n)
	results = append(results, n)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)
	checkError(err)
	defer stdout.Close()
	queriesRows, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)

	for queriesRowItr := 0; queriesRowItr < int(queriesRows); queriesRowItr++ {
		queriesRowTemp := strings.Split(readLine(reader), " ")

		comand, name := queriesRowTemp[0], queriesRowTemp[1]
		comands[comand](name)
	}

	// result := results
	// for resultItr, resultItem := range result {
	// 	fmt.Fprintf(writer, "%d", resultItem)
	// 	if resultItr != len(result)-1 {
	// 		fmt.Fprintf(writer, "\n")
	// 	}
	// }
	// fmt.Fprintf(writer, "\n")

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
