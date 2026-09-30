package main

import (
	"fmt"
	"net/http"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {

	httpRequests := prometheus.NewCounter(
		prometheus.CounterOpts{
			Name: "http_requests_total",
			Help: "Total number of HTTP requests received.",
		},
	)

	prometheus.MustRegister(httpRequests)

	http.HandleFunc("/{$}", func(w http.ResponseWriter, r *http.Request) {
		httpRequests.Inc()
		fmt.Fprintln(w, "Hello from our DDoS protection backend!")
	})

	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		httpRequests.Inc()
		fmt.Fprintln(w, "OK")
	})

	http.Handle("/metrics", promhttp.Handler())

	http.ListenAndServe(":8080", nil)
}
