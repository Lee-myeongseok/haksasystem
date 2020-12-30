window.onload = (function(){
  $('#idAdd li').on('click', function(){
    var elementClass = $(this).attr('class');

    var url;
    var name;
    var option;

    if(elementClass == "newProfessor")
    {
      url = "http://127.0.0.1:8000/polls/newpro/";
      name = "popupPro";
      option = "width = 500, height = 500, top = 100, left = 200, location = no";
    }
    else if (elementClass == "findIdPw")
    {
      url = "http://127.0.0.1:8000/polls/findidpw/";
      name = "popupFind";
      option = "width = 500, height = 250, top = 100, left = 200, location = no";
    }

    window.open(url, name, option);
  })
});
