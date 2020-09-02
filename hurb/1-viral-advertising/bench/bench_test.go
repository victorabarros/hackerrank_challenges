package bench

import "testing"

func benchmarkCumulativeWithMemo(b *testing.B, day int) {
	for ii := 0; ii < b.N; ii++ {
		cumulativeWithMemo(day)
	}
}

func benchmarkCumulativeWithoutMemo(b *testing.B, day int) {
	for ii := 0; ii < b.N; ii++ {
		cumulativeWithoutMemo(day)
	}
}

func BenchmarkCumulative10(b *testing.B)   { benchmarkCumulativeWithMemo(b, 1000) }
func BenchmarkCumulative1000(b *testing.B) { benchmarkCumulativeWithMemo(b, 100000) }

func BenchmarkCumulativeWithoutMemo10(b *testing.B)   { benchmarkCumulativeWithoutMemo(b, 1000) }
func BenchmarkCumulativeWithoutMemo1000(b *testing.B) { benchmarkCumulativeWithoutMemo(b, 100000) }
