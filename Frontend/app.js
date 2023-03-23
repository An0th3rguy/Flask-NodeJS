const http = require('http');

const hostname = '0.0.0.0';
const port = 80;

async function getData(url){
  const response = await fetch(url);
  return await response.json();
}

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  getData("http://backend:5000").then(data => {
    console.log(data);
  });
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});