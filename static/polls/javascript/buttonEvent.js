window.onload = function(){
  $(document).off("click").on("click", ".hope_subject", function(){
    alert("강의 담기가 완료되었습니다.");

    var tdArr = new Array();
    var tr = $(this).parent().parent();
    var td = tr.children();

    td.each(function(i){
      tdArr.push(td.eq(i).text());
    });

    var jsonString = JSON.stringify(tdArr);
    $.ajax({
        type : "POST",
        url : 'http://127.0.0.1:8000/polls/subjectlookup/',
        data : jsonString,
        dataType : 'json',
        error : function(xhr, status, error){
        }
    });
  })
}
