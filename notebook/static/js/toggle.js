
function hide() {
  var x = document.getElementById("add-comment");
  x.style.display = "none";
}

function toggle() {
  var x = document.getElementById("add-comment");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
