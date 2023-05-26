FROM golang:1.12 AS builder
ADD ./main.go main.go

# Fetch dependencies
RUN go get -d -v
# Build image as a truly static Go binary
RUN CGO_ENABLED=0 GOOS=linux go build -o /hue-reminders -a -tags netgo -ldflags '-s -w'

FROM scratch
MAINTAINER Gigi Sayfan <the.gigi@gmail.com>
COPY --from=builder /hue-reminders /hue-reminders
EXPOSE 8080
ENTRYPOINT ["/hue-reminders"]

