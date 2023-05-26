package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"
)

func handler(w http.ResponseWriter, r *http.Request) {
	reminders := []string{
		"Dentist appointment at 3pm",
		"Dinner at 7pm",
	}
	fmt.Fprint(w, strings.Join(reminders, "\n"), r.URL.Path[1:])
}

func main() {
	http.HandleFunc("/", handler)
	log.Println("hue-reminders is listening on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
