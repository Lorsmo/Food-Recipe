var numberRecipes =  d3.select("#number-recipes");

function docsearch() {

  var inputElement1 = d3.select("#word-search2");
  var js_search_term = inputElement1.property("value");
  console.log(js_search_term);

  d3.json(`/readfull/${js_search_term}`).then((response) => {
      console.log('ran search.');
      console.log(response);
      console.log(response.length);

      numberRecipes.html("");
      numberRecipes.text(response.length);

       var tbody = d3.select(".table").select("tbody");
       tbody.html("");
       response.forEach((x) => {

          var row = tbody.append("tr");
          
          Object.entries(x).forEach(([key, value]) => {
            //if(key == '_dir' || key == 'filename' || key == 'date' || key == 'president' || key == 'title'){ 
            if(key == 'name'){
                var cell = row.append("td");
                cell.text(value);
            }
         });
      });


      $("tr:not(:has(th))").mouseover(function () {
        $(this).addClass("hover");
        });
 
      $("tr:not(:has(th))").mouseleave(function () {
        $(this).removeClass("hover");
        });

    });
};

function objectLength(obj) {
  var result = 0;
  for(var prop in obj) {
    if (obj.hasOwnProperty(prop)) {
      result++;
    }
  }
  return result;
}

// jQuery script
$(document).ready(function(){
  $("div.docsList table").delegate('tr', 'click', function() {
      var currentRow=$(this).closest("tr"); // get the current row
      var fp1=currentRow.find("td:eq(0)").text(); // get current row 1st TD value
      var fp2=currentRow.find("td:eq(2)").text();
      var js_filepath = fp1.concat('/', fp2, '.txt')


      $.ajax({
        url : js_filepath,
        dataType: "text",
        success : function (data) {
            //$(".gfg").html(data);
            // var text = d3.select(".gfg").select("p");
            // text.html("")
            document.getElementById("fulltext").innerHTML = ""
            $("#fulltext").append(`${data}`)
        }
      });

    });

  //  $("tr:not(:has(th))").mouseover(function () {
  //      $(this).addClass("hover");
  //      });

  //  $("tr:not(:has(th))").mouseleave(function () {
  //      $(this).removeClass("hover");
  //      });
      
  $( function() {
      $( "#tabs" ).tabs();
      plistsetup();
  } );

});

// When the user clicks on <div>, open the popup
function myFunction(aaa) {
  var popup = document.getElementById(aaa);
  popup.classList.toggle("show"); 
}

  


$('.carousel').carousel({
  interval: 4000
})














