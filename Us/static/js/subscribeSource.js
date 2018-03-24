// alert("Connected");
var sources = [
 {
   "FIELD1": "huffingtonpost",
   "FIELD2": "http://www.huffingtonpost.com"
 },
 {
   "FIELD1": "cnn",
   "FIELD2": "http://www.cnn.com"
 },
 {
   "FIELD1": "time",
   "FIELD2": "http://www.time.com"
 },
 {
   "FIELD1": "ted",
   "FIELD2": "http://www.ted.com"
 },
 {
   "FIELD1": "pandodaily",
   "FIELD2": "http://pandodaily.com"
 },
 {
   "FIELD1": "cnbc",
   "FIELD2": "http://www.cnbc.com"
 },
 {
   "FIELD1": "mlb",
   "FIELD2": "http://www.mlb.com"
 },
 {
   "FIELD1": "pcmag",
   "FIELD2": "http://www.pcmag.com"
 },
 {
   "FIELD1": "foxnews",
   "FIELD2": "http://www.foxnews.com"
 },
 {
   "FIELD1": "theatlantic",
   "FIELD2": "http://theatlantic.com"
 },
 {
   "FIELD1": "bbc",
   "FIELD2": "http://www.bbc.co.uk"
 },
 {
   "FIELD1": "vice",
   "FIELD2": "http://www.vice.com"
 },
 {
   "FIELD1": "elle",
   "FIELD2": "http://www.elle.com"
 },
 {
   "FIELD1": "vh1",
   "FIELD2": "http://www.vh1.com"
 },
 {
   "FIELD1": "espnf1",
   "FIELD2": "http://espnf1.com"
 },
 {
   "FIELD1": "espn",
   "FIELD2": "http://espn.com"
 },
 {
   "FIELD1": "npr",
   "FIELD2": "http://www.npr.org"
 },
 {
   "FIELD1": "sfgate",
   "FIELD2": "http://www.sfgate.com"
 },
 {
   "FIELD1": "nypost",
   "FIELD2": "http://www.nypost.com"
 },
 {
   "FIELD1": "reuters",
   "FIELD2": "http://www.reuters.com"
 },
 {
   "FIELD1": "scientificamerican",
   "FIELD2": "http://www.scientificamerican.com"
 },
 {
   "FIELD1": "miamiherald",
   "FIELD2": "http://www.miamiherald.com"
 },
 {
   "FIELD1": "nydailynews",
   "FIELD2": "http://www.nydailynews.com"
 },
 {
   "FIELD1": "newscientist",
   "FIELD2": "http://www.newscientist.com"
 },
 {
   "FIELD1": "bigstory",
   "FIELD2": "http://bigstory.ap.org"
 },
 {
   "FIELD1": "ebony",
   "FIELD2": "http://www.ebony.com"
 },
 {
   "FIELD1": "thedailystar",
   "FIELD2": "http://thedailystar.com"
 },
 {
   "FIELD1": "technologyreview",
   "FIELD2": "http://www.technologyreview.com"
 },
 {
   "FIELD1": "theverge",
   "FIELD2": "http://www.theverge.com"
 },
 {
   "FIELD1": "nba",
   "FIELD2": "http://www.nba.com"
 },
 {
   "FIELD1": "cbssports",
   "FIELD2": "http://www.cbssports.com"
 },
 {
   "FIELD1": "betabeat",
   "FIELD2": "http://betabeat.com"
 },
 {
   "FIELD1": "tmz",
   "FIELD2": "http://www.tmz.com"
 },
 {
   "FIELD1": "tcnewsnet",
   "FIELD2": "http://tcnewsnet.com"
 },
 {
   "FIELD1": "latimes",
   "FIELD2": "http://www.latimes.com"
 },
 {
   "FIELD1": "c-span",
   "FIELD2": "http://www.c-span.org"
 },
 {
   "FIELD1": "style",
   "FIELD2": "http://www.style.com"
 },
 {
   "FIELD1": "escapistmagazine",
   "FIELD2": "http://www.escapistmagazine.com"
 },
 {
   "FIELD1": "thestreet",
   "FIELD2": "http://www.thestreet.com"
 },
 {
   "FIELD1": "ew",
   "FIELD2": "http://www.ew.com"
 },
 {
   "FIELD1": "nj",
   "FIELD2": "http://www.nj.com"
 },
 {
   "FIELD1": "msn",
   "FIELD2": "http://msn.com"
 },
 {
   "FIELD1": "thedailyreporter",
   "FIELD2": "http://thedailyreporter.com"
 },
 {
   "FIELD1": "economist",
   "FIELD2": "http://www.economist.com"
 },
 {
   "FIELD1": "phys",
   "FIELD2": "http://phys.org"
 },
 {
   "FIELD1": "glam",
   "FIELD2": "http://www.glam.com"
 },
 {
   "FIELD1": "perezhilton",
   "FIELD2": "http://perezhilton.com"
 },
 {
   "FIELD1": "usmagazine",
   "FIELD2": "http://www.usmagazine.com"
 },
 {
   "FIELD1": "aol",
   "FIELD2": "http://aol.com"
 },
 {
   "FIELD1": "cbsnews",
   "FIELD2": "http://www.cbsnews.com"
 },
 {
   "FIELD1": "tennis",
   "FIELD2": "http://www.tennis.com"
 },
 {
   "FIELD1": "washingtonian",
   "FIELD2": "http://washingtonian.com"
 },
 {
   "FIELD1": "sciencedaily",
   "FIELD2": "http://www.sciencedaily.com"
 },
 {
   "FIELD1": "foxsports",
   "FIELD2": "http://foxsports.com"
 },
 {
   "FIELD1": "popularmechanics",
   "FIELD2": "http://www.popularmechanics.com"
 },
 {
   "FIELD1": "macworld",
   "FIELD2": "http://www.macworld.com"
 },
 {
   "FIELD1": "thinkprogress",
   "FIELD2": "http://thinkprogress.org"
 },
 {
   "FIELD1": "mtv",
   "FIELD2": "http://www.mtv.com"
 },
 {
   "FIELD1": "discovery",
   "FIELD2": "http://discovery.com"
 },
 {
   "FIELD1": "people",
   "FIELD2": "http://www.people.com"
 },
 {
   "FIELD1": "thedailybeast",
   "FIELD2": "http://thedailybeast.com"
 },
 {
   "FIELD1": "hollywood",
   "FIELD2": "http://www.hollywood.com"
 },
 {
   "FIELD1": "medium",
   "FIELD2": "http://medium.com"
 },
 {
   "FIELD1": "engadget",
   "FIELD2": "http://www.engadget.com"
 },
 {
   "FIELD1": "usnews",
   "FIELD2": "http://www.usnews.com"
 },
 {
   "FIELD1": "billboard",
   "FIELD2": "http://www.billboard.com"
 },
 {
   "FIELD1": "nationalgeographic",
   "FIELD2": "http://nationalgeographic.com"
 },
 {
   "FIELD1": "purseblog",
   "FIELD2": "http://www.purseblog.com"
 },
 {
   "FIELD1": "giantbomb",
   "FIELD2": "http://www.giantbomb.com"
 },
 {
   "FIELD1": "automobilemag",
   "FIELD2": "http://www.automobilemag.com"
 },
 {
   "FIELD1": "thechronicle",
   "FIELD2": "http://thechronicle.com.au"
 },
 {
   "FIELD1": "tbnweekly",
   "FIELD2": "http://tbnweekly.com"
 },
 {
   "FIELD1": "techreport",
   "FIELD2": "http://techreport.com"
 },
 {
   "FIELD1": "thedailyfix",
   "FIELD2": "http://thedailyfix.com"
 },
 {
   "FIELD1": "animenewsnetwork",
   "FIELD2": "http://www.animenewsnetwork.com"
 },
 {
   "FIELD1": "realclearpolitics",
   "FIELD2": "http://www.realclearpolitics.com"
 },
 {
   "FIELD1": "usatoday",
   "FIELD2": "http://usatoday.com"
 },
 {
   "FIELD1": "techspot",
   "FIELD2": "http://www.techspot.com"
 },
 {
   "FIELD1": "discovermagazine",
   "FIELD2": "http://discovermagazine.com"
 },
 {
   "FIELD1": "arstechnica",
   "FIELD2": "http://arstechnica.com"
 },
 {
   "FIELD1": "foreignpolicy",
   "FIELD2": "http://foreignpolicy.com"
 },
 {
   "FIELD1": "redstate",
   "FIELD2": "http://www.redstate.com"
 },
 {
   "FIELD1": "marketwatch",
   "FIELD2": "http://www.marketwatch.com"
 },
 {
   "FIELD1": "eurogamer",
   "FIELD2": "http://www.eurogamer.net"
 },
 {
   "FIELD1": "cbn",
   "FIELD2": "http://cbn.com"
 },
 {
   "FIELD1": "parade",
   "FIELD2": "http://www.parade.com"
 },
 {
   "FIELD1": "bbcamerica",
   "FIELD2": "http://www.bbcamerica.com"
 },
 {
   "FIELD1": "washingtonindependent",
   "FIELD2": "http://washingtonindependent.com"
 },
 {
   "FIELD1": "drudgereport",
   "FIELD2": "http://drudgereport.com"
 },
 {
   "FIELD1": "beta.na.leagueoflegends",
   "FIELD2": "http://beta.na.leagueoflegends.com"
 },
 {
   "FIELD1": "aajtak",
   "FIELD2": "https://aajtak.intoday.in/"
 },
 {
   "FIELD1": "hindustan-times",
   "FIELD2": "https://www.hindustantimes.com/"
 }
];
console.log(sources.length);
var index = document.getElementsByClassName("subscribe__table")[0];

for(i=0; i<sources.length;i++){
	index.innerHTML+="<tr>"+"<td>"+sources[i]['FIELD1']+"</td><td>"+sources[i]['FIELD2']+"</td>"+"</tr>";
	// console.log(sources[i]);
}
console.log(index);