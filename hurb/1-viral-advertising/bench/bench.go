package bench

import "math"

var (
	sharedMemo     = map[int]float64{1: 5.0}
	likedMemo      = map[int]float64{1: 2.0}
	cumulativeMemo = map[int]float64{1: 2.0}
)

func sharedWithMemo(day int) float64 {
	resp, ok := sharedMemo[day]
	if !ok {
		resp = math.Floor(sharedWithMemo(day-1)/2) * 3
		sharedMemo[day] = resp
	}
	return resp
}

func likedWithMemo(day int) float64 {
	resp, ok := likedMemo[day]
	if !ok {
		resp = math.Floor(sharedWithMemo(day) / 2)
		likedMemo[day] = resp
	}
	return resp
}

func cumulativeWithMemo(day int) float64 {
	resp, ok := cumulativeMemo[day]
	if !ok {
		resp = cumulativeWithMemo(day-1) + likedWithMemo(day)
		cumulativeMemo[day] = resp
	}
	return resp
}

func sharedWithoutMemo(day int) float64 {
	resp, ok := sharedMemo[day]
	if !ok {
		resp = math.Floor(sharedWithoutMemo(day-1)/2) * 3
		// sharedMemo[day] = resp
	}
	return resp
}

func likedWithoutMemo(day int) float64 {
	resp, ok := likedMemo[day]
	if !ok {
		resp = math.Floor(sharedWithoutMemo(day) / 2)
		// likedMemo[day] = resp
	}
	return resp
}

func cumulativeWithoutMemo(day int) float64 {
	resp, ok := cumulativeMemo[day]
	if !ok {
		resp = cumulativeWithoutMemo(day-1) + likedWithoutMemo(day)
		// cumulativeMemo[day] = resp
	}
	return resp
}
