FROM golang:1.24 AS builder
WORKDIR /src
COPY ./main.go .
ARG TARGETOS=linux
ARG TARGETARCH=amd64
ENV CGO_ENABLED=0
RUN GOOS=${TARGETOS} GOARCH=${TARGETARCH} \
    go build -ldflags="-s -w" -o hello main.go

FROM scratch
COPY --from=builder /src/hello /hello
ENTRYPOINT ["/hello"]
