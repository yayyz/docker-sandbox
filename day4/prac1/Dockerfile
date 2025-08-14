# Build Stage
FROM golang:1.24 AS builder
WORKDIR /src
COPY ./main.go .
RUN go build -o hello ./main.go

# Runtime Stage
FROM gcr.io/distroless/base
COPY --from=builder /src/hello /bin/hello
CMD ["/bin/hello"]
