// Fetch api data and update element from json
fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
  .then((response) => response.json())
  .then((data) => {
    $("div#character").text(data.name);
  });
 

