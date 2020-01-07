
//----------------------------------------------------------------------------
//function addItem(){
        //var li = document.createElement("LI");  
        //var input = document.getElementById("btnAdd");
        //li.innerHTML = input.value;
        //input.value = "";
//
        //document.getElementById("faves").appendChild(li);
//}
//
//input.on("click", addItem());

//d3.selectAll("#btnAdd").on("click", function() {
////  // What will be logged out? What is `this` in this case?
  //console.log(this.value);
  //var item = d3.select("ul").append("li");
  //item.text(this.value)
////  // Answer: It will console log the `button` element.
//});
//
//
//d3.selectAll("li").on("click", function() {
//  // you can select the element just like any other selection
//  var listItem = d3.select(this);
//  listItem.style("color", "blue");
//
//  var listItemText = listItem.text();
//  console.log(listItemText);
//});

$(document).ready(function() {
        $("#btnFetch").click(function() {
          // disable button
          $(this).prop("disabled", true);
          // add spinner to button
          $(this).html(
            `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...`
          );
        });
    });