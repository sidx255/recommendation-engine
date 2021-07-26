const searchInput = document.getElementById("searchValue");
const searchButton = document.getElementById("search_button");

document.addEventListener('DOMContentLoaded', function() {
  if(result){
    const table = document.getElementById("recTable");
    var recoms = result.recommendations;
    for(var i=0;i<recoms.length;i++){
      if(i%2==0){
        var row = table.insertRow(-1);  
      }
      var cell = row.insertCell(-1);
      cell.innerHTML = "<b>" + recoms[i] + "</b>";
    }
  }
});

searchInput.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    searchButton.click();
  }
});
