function checkAddr() {
	if ( !newpro.frmPasswd1.value ) {
		alert('패스워드를 입력하세요.')
		newpro.frmPasswd1.focus()
		return
	}

	if ( !newpro.frmPasswd2.value ) {
		alert('패스워드를 다시 입력하세요.')
		newpro.frmPasswd2.focus()
		return
	}

	if ( newpro.frmPasswd1.value != newpro.frmPasswd2.value ) {
		alert('패스워드가 일치하지 않습니다.')
		newpro.frmPasswd2.value = ''
		newpro.frmPasswd2.focus()
		return
	}

	if ( !newpro.frmProName.value ) {
		alert('성명을 입력하세요.')
		newpro.frmProName.focus()
		return
	}

	if ( !newpro.frmBirthMD.value ) {
		alert('생년월일을 입력하세요.')
		newpro.frmBirthMD.focus()
		return
	}
	else if(newpro.frmBirthMD.value && newpro.frmBirthMD.value.length != 6){
    alert('생년월일 여섯자리를 입력하세요.')
    newpro.frmBirthMD.value = ""
    newpro.frmBirthMD.focus()
    return
  }

  if ( !newpro.frmSocialNum.value ) {
		alert('주민등록번호 뒷자리를 입력하세요.')
		newpro.frmSocialNum.focus()
		return
	}
	else if(newpro.frmSocialNum.value && newpro.frmSocialNum.value.length != 7){
    alert('뒷자리 일곱자리를 입력하세요.')
    newpro.frmSocialNum.value = ""
    newpro.frmSocialNum.focus()
    return
  }

	if ( !newpro.frmDepartment.value ) {
		alert('소속학과를 입력하세요.')
		newpro.frmDepartment.focus()
		return
	}

  if ( !newpro.frmAddress.value ) {
    alert('주소를 입력하세요.')
    newpro.frmAddress.focus()
    return
  }

	if ( !newpro.phoneFirst.value ) {
		alert('핸드폰번호를 입력하세요.')
		newpro.phoneFirst.focus()
		return
	}

  if ( !newpro.middle_num.value ) {
		alert('핸드폰번호를 입력하세요.')
		newpro.middle_num.focus()
		return
	}

  if ( !newpro.end_num.value ) {
		alert('핸드폰번호를 입력하세요.')
		newpro.end_num.focus()
		return
	}

	if ( !newpro.frmEmail.value ) {
		alert('이메일주소를 입력하세요.')
		newpro.frmEmail.focus()
		return
	}

	newpro.submit()
}

function findAddrId(){
	if(!findId.frmBirthMD.value){
		alert('주민등록번호 앞자리를 입력하세요.')
		findId.frmBirthMD.focus()
		return
	}
	else if (findId.frmBirthMD.value && findId.frmBirthMD.value.length != 6){
		alert('주민등록번호 앞자리 여섯자리를 입력하세요.')
		findId.frmBirthMD.value = ''
		findId.frmBirthMD.focus()
		return
	}

	if(!findId.frmSocialNum.value){
		alert('주민등록번호 뒷자리를 입력하세요.')
		findId.frmSocialNum.focus()
		return
	}
	else if (findId.frmSocialNum.value && findId.frmSocialNum.value.length !=7){
		alert('주민등록번호 뒷자리 일곱자리를 입력하세요.')
		findId.frmSocialNum.value = ''
		findId.frmSocialNum.focus()
		return
	}

	findId.submit()
}

function findAddrPw(){
	if(!findPw.frmId.value){
		alert('아이디를 입력하세요.')
		findPw.frmId.focus()
		return
	}

	if(!findPw.frmBirthMD.value){
		alert('주민등록번호 앞자리를 입력하세요.')
		findPw.frmBirthMD.focus()
		return
	}
	else if (findPw.frmBirthMD.value && findPw.frmBirthMD.value.length != 6){
		alert('주민등록번호 앞자리 여섯자리를 입력하세요.')
		findPw.frmBirthMD.value = ''
		findPw.frmBirthMD.focus()
		return
	}

	if(!findPw.frmSocialNum.value){
		alert('주민등록번호 뒷자리를 입력하세요.')
		findPw.frmSocialNum.focus()
		return
	}
	else if (findPw.frmSocialNum.value && findPw.frmSocialNum.value.length !=7){
		alert('주민등록번호 뒷자리 일곱자리를 입력하세요.')
		findPw.frmSocialNum.value = ''
		findPw.frmSocialNum.focus()
		return
	}

	findPw.submit()
}
