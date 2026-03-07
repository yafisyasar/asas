const http=require('http')
const PORT=5001;
const server=http.createServer((req,res)=>
{
    res.setHeader('content-Type','text/html');
    if(req.url=='/'){
        res.statusCode=200; //cannot call writeHeader more than once
        res.write("<h1>Home Page</h1>");
        res.write("<p>welcome to Node.js routing example<p>");
                    }

     else if(req.url==='/about'){
         res.statusCode=200; 
        res.write("<h1>academy of arts</h1>");
        res.write("<p>welcome to Node.js routing example<p>");

     }

      else if(req.url==='/contact'){
        res.statusCode=200;
        res.write("<h1>Contact Page</h1>")
        res.write("<p>email:123@gmail.com</p>");
        
       }

       else{
        res.statusCode=404;
        res.write("<h1> 404-Page not found</h1>");
             
       }
       res.end();

       });
    server.listen(PORT,()=>{
        console.log(`routing server running at http://localhost:${PORT}`);
    });
    