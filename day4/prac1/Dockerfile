FROM golang:1.24 AS builder
WORKDIR /src
COPY ./main.go .
RUN go build -o /bin/hello ./main.go

FROM debian:bullseye-slim
COPY --from=builder /bin/hello /bin/hello
CMD ["/bin/hello"]