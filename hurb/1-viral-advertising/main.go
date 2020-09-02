package main

// https://www.hackerrank.com/contests/desafio-algoritmos-2808/challenges/strange-advertising

import (
	"fmt"
	"math"
)

var (
	sharedMemo     = map[int]float64{1: 5.0}
	likedMemo      = map[int]float64{1: 2.0}
	cumulativeMemo = map[int]float64{1: 2.0}
)

// Complete the viralAdvertising function below.
func viralAdvertising(n int32) int32 {
	day := int(n)
	sh := shared(day)
	lik := liked(day)
	cumu := cumulative(day)

	fmt.Printf("%d\t%.0f\t%.0f\t%.0f\n", n, sh, lik, cumu)
	return int32(cumu)
}

func shared(day int) float64 {
	resp, ok := sharedMemo[day]
	if !ok {
		resp = math.Floor(shared(day-1)/2) * 3
		sharedMemo[day] = resp
	}
	return resp
}

func liked(day int) float64 {
	resp, ok := likedMemo[day]
	if !ok {
		resp = math.Floor(shared(day) / 2)
		likedMemo[day] = resp
	}
	return resp
}

func cumulative(day int) float64 {
	resp, ok := cumulativeMemo[day]
	if !ok {
		resp = cumulative(day-1) + liked(day)
		cumulativeMemo[day] = resp
	}
	return resp
}

func main() {
	// reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	// stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	// checkError(err)

	// defer stdout.Close()

	// writer := bufio.NewWriterSize(stdout, 1024*1024)

	// nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	// checkError(err)
	// n := int32(nTemp)

	for ii := 1; ii < 6; ii++ {
		n := int32(ii)
		_ = viralAdvertising(n)
		// result := viralAdvertising(n)

		// fmt.Fprintf(writer, "%d\n", result)
	}

	fmt.Println(sharedMemo)
	fmt.Println(likedMemo)
	fmt.Println(cumulativeMemo)

	// writer.Flush()
}

// func readLine(reader *bufio.Reader) string {
// 	str, _, err := reader.ReadLine()
// 	if err == io.EOF {
// 		return ""
// 	}

// 	return strings.TrimRight(string(str), "\r\n")
// }

// func checkError(err error) {
// 	if err != nil {
// 		panic(err)
// 	}
// }
