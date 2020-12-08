
var num = [
  {'department':'컴퓨터공학과','subject':'C언어의 기초','score':'3','professor':'홍길동','time':'(월요일 14시-16시)','place':'공학관 102호','total':'50'},
  {'department':'토목공학과','subject':'토목 공학','score':'3','professor':'김가인','time':'(화요일 14시-16시)','place':'공학관 103호','total':'30'},
  {'department':'경영학과','subject':'경제와 경영','score':'3','professor':'이규비','time':'(수요일 14시-16시)','place':'문학관 104호','total':'40'},
  {'department':'경제학과','subject':'무역 경제','score':'3','professor':'박다온','time':'(목요일 14시-16시)','place':'문학관 202호','total':'45'},
  {'department':'국어학과','subject':'국어 맞춤법','score':'3','professor':'최다히','time':'(금요일 14시-16시)','place':'문학관 302호','total':'37'},
  {'department':'간호학과','subject':'인체 탐구','score':'3','professor':'황나샘','time':'(월요일 09시-13시)','place':'의학관 303호','total':'55'},
  {'department':'자동차정비학과','subject':'자동차구조','score':'3','professor':'유려온','time':'(화요일 13시-16시)','place':'기계관 102호','total':'20'},
  {'department':'기계공학과','subject':'기계의 이해','score':'3','professor':'민보예','time':'(수요일 12시-16시)','place':'공학관 102호','total':'25'},
  {'department':'영어영문학과','subject':'영어 문법','score':'3','professor':'신보나','time':'(목요일 10시-13시)','place':'공학관 102호','total':'30'},
  {'department':'정보통신학과','subject':'운영체제','score':'3','professor':'윤려온','time':'(월요일 14시-16시)','place':'공학관 102호','total':'40'},
];
document.write("<table style=\"padding-top:220px;\">");
  document.write("<table id=\"subjectTBL\" style=\"overflow:auto;\">");
    document.write("<th>"+"희망"+"<br>"+"과목"+"</th>");
    document.write("<th>"+"학과"+"</th>");
    document.write("<th>"+"과목명"+"</th>");
    document.write("<th>"+"학점"+"</th>");
    document.write("<th>"+"담당교수"+"</th>");
    document.write("<th>"+"강의시간"+"</th>");
    document.write("<th>"+"강의실"+"</th>");
    document.write("<th>"+"총인원"+"</th>");

    for(i=0;i<num.length;i++)
    {
      document.write("<tr>");
        document.write("<td style=\"width:100px\">"+"<input type=\"button\" class=\"hope_subject\" value=\"수강신청\" />"+"</td>")
        document.write("<td style=\"width:120px\">"+num[i].department+"</td>");
        document.write("<td style=\"width:120px\">"+num[i].subject+"</td>");
        document.write("<td style=\"width:40px\">"+num[i].score+"</td>");
        document.write("<td style=\"width:80px\">"+num[i].professor+"</td>");
        document.write("<td style=\"width:150px\">"+num[i].time+"</td>");
        document.write("<td style=\"width:70px\">"+num[i].place+"</td>");
        document.write("<td style=\"width:50px\">"+num[i].total+"</td>");
      document.write("</tr>");
    }
    document.write("</table>");
  document.write("</table>");
