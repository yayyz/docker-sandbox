FROM golang:1.24
WORKDIR /src
COPY ./main.go .
RUN go build -o /bin/hello ./main.go
CMD ["/bin/hello"]
