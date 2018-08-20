console.log("My chrome extension");

var description,keywords;
var metas = document.getElementsByTagName('meta');

for (var i=0;i<metas.length; i++) {
  if (metas[i].name.toLowerCase() == "description") {
    description = metas[i].content;
  }

  if (metas[i].name.toLowerCase() == "keywords") {
    keywords = metas[i].content;
  }
}


myFile = {
	"email":"satantia@teksystems.com",
	"timestamp": new Date().toString().substr(0,),
	"metadata": {
		"title":document.title,
		"url":document.URL,
		"description":description,
		"keywords":keywords,
		"host":document.location.host
	}
}


console.log(myFile);