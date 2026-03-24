const http = require('http');
const url = require('url')
const axios = require('axios');
const API_KEY='2d01eae68a34757b57d78aacac77e1f4';
const server = http.createServer(async(req,res)=>{
    console.log("req rcvd: ", req.url);
    const parsedUrl = url.parse(req.url,true);
    const city = parsedUrl.query.city;
    if(!city){
        res.writeHead(400,{'Content-Type':'application/json'});
        return res.end(JSON.stringify({error: 'City parameter missing'}));
    }
    try{
        const weatherUrl=`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`;
        const response = await axios.get(weatherUrl);
        const data ={
            city:response.data.name,
            temperature:response.data.main.temp,
            humidity:response.data.main.humidity,
            description:response.data.weather[0].description
        };
        res.writeHead(200,{'Content-Type':'application/json'});
        res.end(JSON.stringify(data));
    }
    catch (error){
        console.error("API Error:",error.message);
        res.writeHead(500,{'Content-Type':'application/json'});
        res.end(JSON.stringify({error:'Failed to fetch weather data'}));
    }
});
server.listen(3000,'127.0.0.1',()=>{
    console.log('weather server running at http://127.0.0.1:3000');
});
//  http://127.0.0.1:3000/?city=kochi