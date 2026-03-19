const http = require('http');

http.createServer((req, res) => {
  res.end("Docker Compose Build Lab. Hello From Rishu");
}).listen(3000);
