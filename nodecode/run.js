const fs = require('fs');
const http = require('http');
const express = require('express');
const url = require('url');
var qs = require('querystring');
var md5 = require('md5');
const { exit } = require('process');
const axios = require('axios').default;
var bodyParser = require('body-parser')
const app = express();



const httpAgent = new http.Agent({ keepAlive: true });


const httpServer = http.createServer(app);

var jsonParser = bodyParser.json()

app.post('/meydan/api/pushMonitorResult',jsonParser, (req, res) => {
    console.log(req.body);

    // var urlParts = url.parse(req.url, true),
    //     urlParams = urlParts.query, 
    //     urlPathname = urlParts.pathname,
    //     body = '',
    //     reqInfo = {};
    // reqInfo.urlPathname = urlPathname;
    // reqInfo.urlParams = urlParams; 
    // reqInfo.body = qs.parse(body);

    // reqInfo.urlParts = urlParts;
    // var Info = JSON.stringify(reqInfo)
    // console.log(reqInfo);
    // res.writeHead(200, {'Content-type':'application/json'});
    // var data = JSON.stringify(JSON.parse('{"status":100}'));
    // console.log("URL : " + reqInfo.urlPathname);
    // console.log("URL Parameter : " + JSON.stringify(body));
    // var userName = "admin";
    // var passWord = "admin";
    // var parame = JSON.stringify(reqInfo.urlParams);
    // console.log(reqInfo.urlParams.name,reqInfo.urlParams.eid)

    //res.end(reqInfo.urlParams.name);

    //console.log('Received Message:', topic, payload.toString());
    // axios.get("http://13.52.238.152:5055/?id=9705001673&lat=23.0&lon=25.0&timestamp=1648415734&alarm=sos", { httpAgent }).then(function (response) {
    //     console.log(response.data);
    // })
    // .catch(function (error) {
    //     console.log(error);
    // })
    // .then(function () {
    // });
    //var ParsedData = JSON.parse(payload)
	//console.log('Received Message:', topic, payload.toString(),JSON.parse(payload).timestamp,payload.timestamp);
    
	// axios.post("http://13.52.238.152:5055", { httpAgent, params: req}).then(function (response) {
	// console.log(response.data);
	// })
	// .catch(function (error) {
	// console.log(error);
	// })
	// .then(function () {
	// });
  
    // axios.post("http://localhost:8082/api/devices",{
	// 		"name": reqInfo.urlParams.name,
	// 		"uniqueId": reqInfo.urlParams.eid,
    //   //"category":"bicycle",
    //   //"groupId":2
	// 	  },{headers: {
	// 			'Authorization': authenticateUser(userName, passWord)
	// 		  }
	// 	  }).then(function (response) {
	// 		console.log(response.data);
	// 	  })
	// 	  .catch(function (error) {
	// 		console.log(error);
	// 	  })
	// 	  .then(function () {
	// 	  });
    res.end(data);
  })

  


httpServer.listen(8080, () => {
    console.log('HTTPS Server running on port 8080');
});

//app.listen(port, () => console.log(`listening on port ${port}!`));