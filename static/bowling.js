function myFunction(){
    var x = document.getElementById("myTopnav");
    if(x.className === "topnav"){
        x.className += "responsive";
    } else{
        x.xlassName = "topnav";
    }
}
function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  function validateForm() {
    let x = document.forms["member_form"]["DName","DPhone","DEmail"].value;
    if (x == "") {
      alert("Velden zijn verplicht!");
      return false;
    }
  }